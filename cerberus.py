#!/usr/bin/env python3
# =============================================================================
# Author  : Roberto Sosa
# Created : October 2021
# Version : 0.0.0
# Status  : Prototype
# =============================================================================
"""Coding Exercise: Staff Security Engineer"""
# =============================================================================

# Pre-Game Steps:
# pip install -r requirements.txt 
# pip3 install azure-cli
# az login
# az account list --query '[*].id'
# az role assignment list --subscription 63a7f75b-08dc-47f7-b481-b39c22b031f6 --role "Owner" --query '[*].principalName'

# Avoid this approach:
# import os
# az_account_list = "az account list --query '[*].id'"
# os.system(az_account_list)

# Test Case Example 1
# Account Management
# ID: NIST SP 800-53 Rev. 4 AC-2
# Description: It is recommended to designate up to 3 subscription owners 
# in order to reduce the potential for breach by a compromised owner.


# Possible Remediation Actions
# az role assignment create --role "Owner" --assignee <USER> --subscription <ID>

