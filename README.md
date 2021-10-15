#### Version 202102
### Coding Exercise: Staff Security Engineer

This sample project aims to demonstrate how to validate a given set of controls on a system —using Python.

# Cloud Cerberus
Often referred to as the Hound of Hades, Cerberus is multi-headed dog that safeguards the gates of the Underworld; In this case, he serves as inspiration to protect our resources residing on three of the well known cloud providers: AWS, AZ, GCP.

## Environment 
For this proof of concept, we will be evaluating the following environment(s):

- Microsoft Azure
```
{
    "id": "/subscriptions/63a7f75b-08dc-47f7-b481-b39c22b031f6/resourceGroups/datacakes",
    "name": "datacakes",
    "location": "eastus",
    "tags": {
        "env": "dev",
        "owner": "robertos"
    },
    "properties": {
        "provisioningState": "Succeeded"
    }
}
```

## Approach
The [General Access Control Guidance for Cloud Systems](https://csrc.nist.gov/publications/detail/sp/800-210/final) served as the initial reference for this assignment, as it represents a comprehensive understanding of security challenges in cloud systems, for all three service delivery models —Infrastructure as a Service (IaaS), Platform as a Service (PaaS), and Software as a Service (SaaS). Although, while the appendix provides a layout for the control families listed in NIST SP 800-53, after analyzing these, one will find that the guidance provided can still be quite broad, and not particularly prescriptive (in terms of programmatic conditions) to a provider specific configuration. And thus, to make each case example easier to illustrate, we also considered expressing our interpretations of the Cybersecurity Framework (CSF) as a mapping to other standards where applicable —for example CIS Controls, or Cloud Controls Matrix (CCM). This was not meant to avoid any definitions from our initial requirements, but instead to facilitate our implementation where such sub-controls are written more explicitly. The later was fundamental during our research process, as we prepared for this activity.

## Prerequisites
The Azure Command-Line Interface ([CLI](https://docs.microsoft.com/en-us/cli/azure/install-azure-cli)) allows the execution of commands through the terminal —for macOS run:
`brew update && brew install azure-cli`

## Usage
`cloud-cerberus % ./hound.py`

## NIST Prescribed Terminology
- Each Security Control Assessment will return a value of: “Satisfied” or “Other Than Satisfied”

## Future Enhancement Considerations
- If absolutely required to call Azure CLI from Python, we would need to implement a function to properly parse `.invoke()` —as it always returns the error code as output.
- Devise a mechanism to input a list, or policy sets, as a dynamic collection —rather than static checks.
- Leverage cloud native solutions that map compliance domains and controls to NIST SP 800-53, like Azure Policy Regulatory Compliance built-in initiative definitions.
- Expanding on the above, research if technical equivalents are feasible for Amazon Web Services, and Google Cloud Platform.
- Consider adopting [Az.Cli](https://markwarneke.me/2021-03-14-Query-Azure-Resources-Using-Python/)
- Since this demo is running [locally](https://docs.microsoft.com/en-us/azure/developer/python/azure-sdk-authenticate#identity-when-running-the-app-locally), we are constrained from assigning a [managed identity](https://docs.microsoft.com/en-us/azure/active-directory/managed-identities-azure-resources/overview). 

## Author
[Roberto Sosa](https://github.com/SuperTonic09)

## (Others) To Do
- Review applicable licenses: Apache, or MIT

## References
- [Details of the NIST SP 800-53 Rev. 4 Regulatory Compliance built-in initiative](https://docs.microsoft.com/en-us/azure/governance/policy/samples/nist-sp-800-53-r4)
- [Configure your local Python dev environment for Azure](https://docs.microsoft.com/en-us/azure/developer/python/configure-local-development-environment?tabs=cmd)

## (Optional) Start Environment
```
python3 -m venv .venv 
source .venv/bin/activate
```
## Notes on The Azure SDK for Python
- The use of `azure.cli.core` is not as easy to read, for the purpose of adopting examples, as the management REST API.
- Additionally, it appears that most of the community simply leverages the standard shell commands as-is.
- While the use of the `subprocess` solution may not be as portable, the `pypi azure-cli` will bloat the requirements over time.
- That's because the Azure SDK for Python is composed of over 180 individual libraries that relate to specific Azure services.
