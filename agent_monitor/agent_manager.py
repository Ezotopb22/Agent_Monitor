from agent_monitor import agent_ops as ops
from agent_monitor import settings
import json
import requests



# uname
# python version, jdk version
# free disk space \ memory
# cpu system \ user





class AgentManager:

    def __init__(self):
        pass


    def register(self):

        print('going to register agent')
        with open('License_key') as f:
            # print(f.readline())
            lk = f.readline()

        data = {'license_key': lk}
        err_msg = 'Agent was not identifide by the server'
        self.send_data_to_server(settings.REGISTER_URL, data, err_msg)

    def send_data_to_server(self ,url ,data, err_msg='bad request'):

        headers = {'content-type': 'application/json'}
        r = requests.post(url=url, data=json.dumps(data), headers=headers)

        # if response is 200 then continue else print error message and quit
        if r.status_code != 200:
            raise Exception(err_msg)

    def run_tasks(self):

        logged_in_users = ops.loggedin()

        data_to_server = self.prep_agent_data(list(logged_in_users), 'logged_in_users')

        self.send_data_to_server(settings.AGENT_UPDATES_URL, data_to_server)


        # call get python version
        # prepare data to server with python version and data_type which will be: python_version, it should look like
        # this: {'python_version': '3.7'}

        # now send data to server !! like in line 49



    def prep_agent_data(self ,data ,data_type):
        return {data_type: data}










