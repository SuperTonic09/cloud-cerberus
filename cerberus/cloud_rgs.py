# Helper functions to enumerate resource group identifiers; 
# Consider that most CLI cases don't honor --all.

import json
import subprocess


class Azure:

    def get_subs():
        az_accounts = subprocess.check_output('az account list', shell=True)
        subscriptions = json.loads(az_accounts)

        # Since each account can have multiple subscriptions, parse a final id list.
        sid_list = []
        for id in range(len(subscriptions)):
            sid_list.append(subscriptions[id]['id'])
        return sid_list

    def az_account_set(sid):
        subprocess.run('az account set --subscription ' + sid, shell=True)
