# NZHTS-Tools
Tools for using the NZHTS

**Python Script for parsing out the codesets from a Questionnaire template**

Developed this script so we could extract the Snomed codesets from a Questionnaire. Requires credentials to access the service (mailto:standards@tewhatuora.govt.nz)
This takes the .json as an input and iterates over each of the "valueset" objects and then outputs all of the codes as a list in a UTF-8 .txt file.

Usecase:

Creating a vector store for a GPT-4o model to complete a valid questionnaire response with the expected codesets.


Example Query Strings in NZHTS:

List substances and products:

`https://nzhts.digital.health.nz/fhir/ValueSet/$expand?url=http://snomed.info/sct?fhir_vs=ecl/< 105590001 or < 20373873005`


Expand a defined value set:

`https://nzhts.digital.health.nz/fhir/ValueSet/$expand?url=http://snomed.info/sct?fhir_vs=ecl/<<27624003`


Filter an ECL value set on a clinical term "Aspirin":

`https://nzhts.digital.health.nz/fhir/ValueSet/$expand?url=http://snomed.info/sct?fhir_vs=ecl/<< 763158003&filter=aspirin`
 
 




Feedback: mailto:jon.herries@tewhatuora.govt.nz
