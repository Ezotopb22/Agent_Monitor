#importing System
import psutil
import time
import sys

#Every hour send the to server - who is logged to the machine.


def loggedin():
    """
    this function will return logged in users
    :return: unique users
    """
    logged_in_users = psutil.users()
    users_online = set() # collection of elemnts withour repetition
    for user in logged_in_users:
        users_online.add(user[0])

    return users_online


def get_uname_data():
    pass

def get_get_python_version():
    return sys.version






