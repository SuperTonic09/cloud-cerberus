# Performs Security Control Assessments.

import json
import subprocess

import cloud_rgs


try:
    # Get a global list of subscription IDs just once ——performance optimization.
    sid_list = cloud_rgs.Azure.get_subs()
except:
    raise ValueError('A valid subscription list is required to proceed.')


def test_case_1():
    """Account Management
    
    ID: NIST SP 800-53 Rev. 4 AC-2
    Description: It is recommended to designate up to 3 subscription owners 
    in order to reduce the potential for breach by a compromised owner.

    Possible Remediating Actions:
    az role assignment create --role "Owner" --assignee <USER> --subscription <ID>
    """

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

    for id in range(len(sid_list)):
        cloud_rgs.Azure.az_account_set(sid_list[id])
        
        az_vm_args = "az vm list --query '[*].id'"

        az_vm_query = subprocess.check_output(az_vm_args, shell=True)
        az_vm_list = json.loads(az_vm_query)

        if az_vm_list:
            for vm in az_vm_list:
                az_vm_args = 'az vm show --ids ' + vm + ' --query ' + \
                    'osProfile.linuxConfiguration.disablePasswordAuthentication'
                az_vm_check = subprocess.check_output(az_vm_args, shell=True)

                test_result = az_vm_check.decode().strip()

                print('\nSSH Keys enabled on compute:', vm)

                if test_result == 'true':
                    print('Security Control Assessment: “Satisfied”\n')
                else:
                    print('Security Control Assessment: “Other Than Satisfied”\n')
        
        else:
            print('\nNo compute resources found for subscription:', sid_list[id])

    return test_result