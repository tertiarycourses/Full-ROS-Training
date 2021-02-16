#!/usr/bin/env python
import rospy
from demo1.srv import *

def service():
    rospy.init_node('my_eleven_node')
    rospy.Service('on_off_service',my_service,turn_on_off)
    rospy.spin()

def turn_on_off(req):
    if req.onezero == 1:
        return my_serviceResponse('ON')
    else:
        return my_serviceResponse('OFF')
        
if __name__ == '__main__':
    service()



