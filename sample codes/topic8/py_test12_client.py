#!/usr/bin/env python
import sys
import rospy
from my_robotics.srv import *

def py_test12_client(x, y):
    rospy.wait_for_service('my_sum_service')
    try:
        add_two_ints = rospy.ServiceProxy('my_sum_service', my_sum)
        resp1 = add_two_ints(x, y)
        return resp1.sum
    except rospy.ServiceException as e:
        print("Service call failed: %s"%e)

def usage():
    return "%s [x y]"%sys.argv[0]

if __name__ == "__main__":
    if len(sys.argv) == 3:
        x = int(sys.argv[1])
        y = int(sys.argv[2])
    else:
        print(usage())
        sys.exit(1)
    print "Requesting %s+%s"%(x, y) 
    print"%s + %s = %s"%(x, y, py_test12_client(x, y))