#!/usr/bin/env python3
# =============================================================================
# Author  : Roberto Sosa
# Created : October 2021
# Version : 0.1.2
# Status  : Prototype
# =============================================================================
"""Coding Exercise: Staff Security Engineer (Role)"""
# =============================================================================

import json
import subprocess
import sys

import cloud_auth
import sca_collection

try:
    cloud_auth.az_login()
except:
    print('\nFailed to authenticate with provider(s)\n')
    sys.exit(1)

print('\nCloud Cerberus checks starting...\n')

sca_collection.test_case_1()
