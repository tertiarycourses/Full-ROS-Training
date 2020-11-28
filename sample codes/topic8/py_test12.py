#!/usr/bin/env python
import rospy
from my_robotics.srv import my_sum,my_sumResponse

def talker():
    rospy.init_node('my_sum_service_node')
    rospy.Service('my_sum_service',my_sum,sum_2_ints)
    rospy.spin()

def sum_2_ints(req):
    return my_sumResponse(req.a+req.b)
        
if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        rospy.shutdown()



