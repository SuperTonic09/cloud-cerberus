#!/usr/bin/env python3
# =============================================================================
# Author  : Roberto Sosa
# Created : October 2021
# Version : 0.1.2
# Status  : Prototype
# =============================================================================
"""Coding Exercise: Staff Security Engineer (Role)"""
# =============================================================================

from cerberus import cloud_auth, sca_collection

try:
    cloud_auth.az_login()
except:
    raise ValueError('Failed to authenticate with provider(s)')


def main():
    print('\nCloud Cerberus checks starting...\n')
    
    sca_collection.test_case_1()
    sca_collection.test_case_2()
    sca_collection.test_case_3()


if __name__ == '__main__':
    main()
