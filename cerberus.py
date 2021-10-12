#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# =============================================================================
# Author  : Roberto Sosa
# Created : October 2021
# Version : 0.0.0
# Status  : Prototype
# =============================================================================
"""Coding Exercise: Staff Security Engineer"""
# =============================================================================

import subprocess
import json

from client_credentials import *

az_auth_args = 'az login --service-principal' \
    + ' -u ' + az_client_id + ' -p ' + az_client_secret + ' -t ' + az_tenant_id

# subprocess.run(az_auth_args, shell=True)

print('\nCloud Cerberus checks starting...\n')

print("""
# -----------------------------------------------------------------------------
# Test Case Example 1
# Account Management
# ID: NIST SP 800-53 Rev. 4 AC-2
# Description: It is recommended to designate up to 3 subscription owners 
# in order to reduce the potential for breach by a compromised owner.
#
# Possible Remediating Actions:
# az role assignment create --role "Owner" --assignee <USER> --subscription <ID>
# -----------------------------------------------------------------------------
""")

az_account_list = subprocess.check_output('az account list', shell=True)
sub_list = json.loads(az_account_list)

print(json.dumps(sub_list, indent=4, sort_keys=True))

# Since each account can have multiple subscriptions, append to a final list: 
sub_ids = []
for i in range(len(sub_list)):
    sub_ids.append(sub_list[i]['id'])

for i in range(len(sub_ids)):
    az_role_args = 'az role assignment list --subscription ' + sub_ids[i] \
        + ' --role "Owner" --query \'[*].principalId\''
    
    az_role_check = subprocess.check_output(az_role_args, shell=True)
    sub_owner_list = json.loads(az_role_check)
    owner_count = len(sub_owner_list)
    
    print('\nSubscription ID:', sub_ids[i])
    print(json.dumps(sub_owner_list, indent=4, sort_keys=True), '\n')

    print('Total number of owners identified:', owner_count, '\n')

    if owner_count <= 3:
        print('Security Control Assessment: “Satisfied”\n')
    else:
        print('Security Control Assessment: “Other Than Satisfied”\n')