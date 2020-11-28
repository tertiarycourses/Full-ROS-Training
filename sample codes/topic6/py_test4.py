#!/usr/bin/env python
import rospy
from std_msgs.msg import String

def callback(msg_data):
    rospy.loginfo(msg_data)

def listener():
    rospy.init_node('my_fourth_node')
    rospy.Subscriber('greetings',String,callback)
    rospy.spin()

if __name__ == '__main__':
    try:
        listener()
    except rospy.ROSInterruptException:
        rospy.shutdown()




