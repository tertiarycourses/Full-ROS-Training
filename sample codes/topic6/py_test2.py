#!/usr/bin/env python
import rospy
from std_msgs.msg import String

def talker():
    rospy.init_node('my_second_node')
    while True:
        rospy.loginfo("Hello World")
        rospy.sleep(1)

if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass

