# Authenticates with multiple cloud providers.

import subprocess

from secret.client_credentials import *

def az_login():
    # Microsoft Azure
    az_auth_args = 'az login --service-principal' \
    + ' -u ' + az_client_id + ' -p ' + az_client_secret + ' -t ' + az_tenant_id
    
    subprocess.run(az_auth_args, shell=True, check=True)

def aws_login():
    # Amazon Web Services 
    print('No yet implemented')
    pass

def gcp_login():
    # Google Cloud Platform
    print('No yet implemented')
    pass