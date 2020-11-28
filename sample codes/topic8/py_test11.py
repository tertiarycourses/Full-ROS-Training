#!/usr/bin/env python
import rospy
from my_robotics.srv import my_service,my_serviceResponse,my_serviceRequest

def talker():
    rospy.init_node('my_service_respond')
    rospy.Service('on_off_service',my_service,turn_on_off)
    rospy.spin()

def turn_on_off(req):

    if req.onezero == 1:
        return my_serviceResponse('ON')
    else:
        return my_serviceResponse('OFF')
        
if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        rospy.shutdown()



