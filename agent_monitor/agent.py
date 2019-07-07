#In order to communicate with the server side we need to install a network protocol (HTTP) - pip

from agent_monitor.agent_manager import AgentManager

#  grab license key
# send it to server (install requests package)
# get response

import requests
import json
from agent_monitor import settings

if __name__ == '__main__':
    print('Starting agent')

    agent_manager = AgentManager()
    agent_manager.register()
    print('Agent is identifide by the srever')
    agent_manager.run_tasks()





#Every hour send the to server - How is loged to the machine



