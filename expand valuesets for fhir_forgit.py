import requests
import json
from tkinter import Tk, filedialog
import os

# OAuth2 details
token_url = "https://authenticate.nzhts.digital.health.nz/auth/realms/nzhts/protocol/openid-connect/token"
client_id = "healthnz"
client_secret = "[Enter your client secret here]"

# File picker dialog
Tk().withdraw()
json_path = filedialog.askopenfilename(
    title="Select JSON file with answerValueSet URLs",
    filetypes=[("JSON files", "*.json")]
)
if not json_path:
    print("No file selected.")
    exit()

# Load JSON and extract answerValueSet URLs
with open(json_path, "r", encoding="utf-8") as f:
    data = json.load(f)

# Find all answerValueSet URLs (recursive search)
def find_answer_value_sets(obj):
    urls = []
    if isinstance(obj, dict):
        for k, v in obj.items():
            if k == "answerValueSet" and isinstance(v, str):
                urls.append(v)
            else:
                urls.extend(find_answer_value_sets(v))
    elif isinstance(obj, list):
        for item in obj:
            urls.extend(find_answer_value_sets(item))
    return urls

valueset_urls = find_answer_value_sets(data)
if not valueset_urls:
    print("No answerValueSet URLs found.")
    exit()

# Get OAuth2 token
token_data = {
    "grant_type": "client_credentials",
    "client_id": client_id,
    "client_secret": client_secret
}
token_response = requests.post(token_url, data=token_data, verify=False)
token_response.raise_for_status()
access_token = token_response.json()["access_token"]
headers = {"Authorization": f"Bearer {access_token}"}

# After loading json_path
input_dir = os.path.dirname(json_path)
input_base = os.path.splitext(os.path.basename(json_path))[0]
output_path = os.path.join(input_dir, f"{input_base}_codeset.txt")

# Remove the output file picker section and use output_path directly
print(f"Output will be saved to: {output_path}")

# Iterate and append results
with open(output_path, "w", encoding="utf-8") as out_f:
    for vs_url in valueset_urls:
        expand_url = (
            "https://nzhts.digital.health.nz/fhir/ValueSet/$expand"
            f"?url={vs_url}"
        )
        print(f"Expanding: {vs_url}")
        expand_response = requests.get(expand_url, headers=headers, verify=False)
        expand_response.raise_for_status()
        expanded = expand_response.json()
        codes = []
        for item in expanded.get("expansion", {}).get("contains", []):
            code = item.get("code")
            display = item.get("display")
            if code and display:
                codes.append(f"{code}: {display}")
        # Write section header and codes
        out_f.write(f"ValueSet: {vs_url}\n")
        for line in codes:
            out_f.write(line + "\n")
        out_f.write("\n")

print(f"All ValueSets expanded and saved to {output_path}")