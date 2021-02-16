#!/usr/bin/env python
import rospy
from demo1.srv import *

def service():
    rospy.init_node('my_tweleve_node')
    rospy.Service('sum_2_ints_service',my_sum,sum_2_ints)
    rospy.spin()

def sum_2_ints(req):
    return my_sumResponse(req.a+req.b)
        
if __name__ == '__main__':
    service()

