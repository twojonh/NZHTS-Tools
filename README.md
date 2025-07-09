# NZHTS-Tools
Tools for using the NZHTS

**Python Script for parsing out the codesets from a Questionnaire template**
Developed this script so we could extract the Snomed codesets from a Questionnaire. Requires credentials to access the service (mailto:standards@tewhatuora.govt.nz)
This takes the .json as an input and iterates over each of the "valueset" objects and then outputs all of the codes as a list in a UTF-8 .txt file.

Usecase:

Creating a vector store for a GPT-4o model to complete a valid questionnaire response with the expected codesets.

Feedback: mailto:jon.herries@tewhatuora.govt.nz
