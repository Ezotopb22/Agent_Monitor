import agent_monitor.agent_ops as ops
import sys ,time

# this will be unittest file

#import moddule and appending to csv a file
#sys.stdout = open('user_diag.csv','a')
#diag = (print('ops.logedin()') #["EZBOmbd"]'






def test_logged_in_users():

    logged_in = 'EZomob'
    logged_in_users = ops.loggedin()

    assert logged_in in logged_in_users

#while True:
#    diagnose()
#    time.sleep(500)

