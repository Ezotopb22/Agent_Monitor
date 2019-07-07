#In order to communicate with the server side we need to install a network protocol (HTTP) - pip


#  grab license key
# send it to server (install requests package)
# get response

import requests
import json
from agent_monitor import settings

if __name__ == '__main__':
    print('Start agent')


    with open('License_key') as f:
        #print(f.readline())
        lk = f.readline()

    data={'license_key':lk}
    headers = {'content-type': 'application/json'}
    r = requests.post(url=settings.REGISTER_URL, data=json.dumps(data), headers=headers)

    # if response is 200 then continue else print error message and quit
    if r.status_code == 200:
        print('Agent is identifide by the srever')
    else:
        raise Exeption('Agent was not identifide by the server')

#Every hour send the to server - How is loged to the machine



