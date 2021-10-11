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

subprocess.run(az_auth_args, shell=True)

# Test Case Example 1
# Account Management
# ID: NIST SP 800-53 Rev. 4 AC-2
# Description: It is recommended to designate up to 3 subscription owners 
# in order to reduce the potential for breach by a compromised owner.
#
# Possible Remediation Actions
# az role assignment create --role "Owner" --assignee <USER> --subscription <ID>

subscriptions = json.loads(subprocess.check_output('az account list', shell=True))

print(json.dumps(subscriptions, indent=4, sort_keys=True))

print(type(subscriptions))
print(len(subscriptions))
print(subscriptions[0]['id'])

#sub_ids = []
#for i in range(len(subscriptions)):
#    sub_ids.append(subscriptions[i]['id'])

# Test
# print(sub_ids)

