#!/usr/bin/env python
import sys
import rospy
from demo1.srv import *

def on_off(req):
     rospy.wait_for_service('on_off_service')
     onoff = rospy.ServiceProxy('on_off_service', my_service)
     print(onoff(req))

if __name__ == "__main__":
     req = int(sys.argv[1])
     on_off(req)
