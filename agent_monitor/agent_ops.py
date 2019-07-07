#importing System
import psutil
import time
import sys

#Every hour send the to server - who is logged to the machine.


def loggedin():
    """
    the function will return a list of logged in users, e.g: ["momo", "yoyo", "koko"] (unique)
    :return:

    """
    return psutil.users()
    #*** *SET' all data from psutill.users > database in order to geter info and be mpre efective?

    #while true loop the logedin() function
    # while True:
#    loggedin()
#    time.sleep(10)



