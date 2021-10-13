# Performs Security Control Assessments

import json
import subprocess


def test_case_1():
    """Account Management
    
    ID: NIST SP 800-53 Rev. 4 AC-2
    Description: It is recommended to designate up to 3 subscription owners 
    in order to reduce the potential for breach by a compromised owner.

    Possible Remediating Actions:
    az role assignment create --role "Owner" --assignee <USER> --subscription <ID>
    """

    az_accounts = subprocess.check_output('az account list', shell=True)
    subscriptions = json.loads(az_accounts)

    print(json.dumps(subscriptions, indent=4, sort_keys=True))

    # Since each account can have multiple subscriptions, parse a final id list
    sid_list = []
    for id in range(len(subscriptions)):
        sid_list.append(subscriptions[id]['id'])

    for id in range(len(sid_list)):
        az_role_args = 'az role assignment list --subscription ' + sid_list[id] \
            + ' --role "Owner" --query \'[*].principalName\''
        
        az_role_check = subprocess.check_output(az_role_args, shell=True)
        sub_owner_list = json.loads(az_role_check)
        owner_count = len(sub_owner_list)
        
        print('\nSubscription ID:', sid_list[id])
        print(json.dumps(sub_owner_list, indent=4, sort_keys=True), '\n')

        print('Total number of owners identified:', owner_count, '\n')

        test_result = owner_count <= 3

        if test_result:
            print('Security Control Assessment: “Satisfied”\n')
        else:
            print('Security Control Assessment: “Other Than Satisfied”\n')

    return test_result

def test_case_2():
    """Access Enforcement
    
    ID: NIST SP 800-53 Rev. 4 AC-3
    Description: Although SSH itself provides an encrypted connection, 
    using passwords with SSH still leaves the VM vulnerable to brute-force attacks. 
    The most secure option for authenticating to an Azure Linux virtual machine over SSH 
    is with a public-private key pair, also known as SSH keys. 

    Possible Remediating Actions:
    sudo waagent -deprovision -force
    """