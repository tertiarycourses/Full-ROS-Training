#!/usr/bin/env python
import rospy
from std_msgs.msg import Float32

def callback(msg_data):
    rospy.loginfo(msg_data)

def listener():
    rospy.init_node('iot_sensor')
    rospy.Subscriber('temperature',Float32,callback)
    rospy.spin()

if __name__ == '__main__':
    try:
        listener()
    except rospy.ROSInterruptException:
        rospy.shutdown()