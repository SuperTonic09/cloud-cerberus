#### Version 202102
### Coding Exercise: Staff Security Engineer

This sample project aims to demonstrate how to validate a given set of controls on a system —using Python.

# Cloud Cerberus
Often referred to as the Hound of Hades, Cerberus is multi-headed dog that safeguards the gates of the Underworld; In this case, he serves as inspiration to protect our resources residing on three of the well known cloud providers: AWS, AZ, GCP.

## Environment 
For this proof of concept, we will be evaluating the following environment(s):
- Microsoft Azure _(details TBD)_

## Approach
The NIST Special Publication (SP) 800-210, [General Access Control Guidance for Cloud Systems](https://csrc.nist.gov/publications/detail/sp/800-210/final), served as the initial reference for this assignment, as it represents a comprehensive understanding of security challenges in cloud systems, in all three service delivery models —Infrastructure as a Service (IaaS), Platform as a Service (PaaS), and Software as a Service (SaaS). Although while the appendix provides a table map for the control families as listed in NIST SP 800-53, after analyzing these, one will find that the guidance provided can still be quite broad, and not prescriptive to a particular provider specific configuration. And thus to make each case example easier to illustrate, we may express our interpretations of the NIST Cybersecurity Framework (CSF) as a mapping to other frameworks and standards where applicable —for example CIS Controls, or Cloud Controls Matrix (CCM). This is not meant to avoid any definitions from our initial requirements, but instead facilitate our implementation where such sub-controls are written more explicitly. The later was fundamental in our research, as we prepared for this activity.


## Usage
`python3 cerberus.py`

## Future Enhancement Considerations
- Split the main code into smaller modules.
- Devise a mechanism to input a list, or policy sets, as a dynamic collection —rather than static checks.
- Leverage cloud native solutions that map compliance domains and controls to NIST SP 800-53, like Azure Policy Regulatory Compliance built-in initiative definitions.
- Expanding on the above, research if technical equivalents are feasible for Amazon Web Services, and Google Cloud Platform.
- _TBC_

## Author
[Roberto Sosa](https://github.com/SuperTonic09)

