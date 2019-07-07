import agent_monitor.agent_ops as ops
import sys ,time



#import moddule and appending to csv a file
sys.stdout = open('user_diag.csv','a')
#diag = (print('ops.logedin()') #["EZBOmbd"]'
logged_in_users = ops.loggedin()


def diagnose():
    sys.stdout = open('user_diag.csv','a')
    #logged_in_users = ops.loggedin()
    logged_in_users = ops.loggedin()
    print(ops.loggedin())
    sys.stdout.close()
diagnose()
    #.close()
    #eturn

#while True:
#    diag()
#    time.sleep(10)

