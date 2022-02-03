#!/usr/bin/env python3
# =============================================================================
# Author  : Roberto Sosa
# Created : October 2021
# Version : 0.1.2
# Status  : Prototype
# =============================================================================


from cerberus import cloud_auth, sca_collection

try:
    cloud_auth.az_login()
except:
    raise ValueError('Failed to authenticate with provider(s)')


def main():
    print('\nStarting regulatory assessments ...\n')
    
    sca_collection.compliance_check_1()
    sca_collection.compliance_check_2()
    sca_collection.compliance_check_3()


if __name__ == '__main__':
    main()
