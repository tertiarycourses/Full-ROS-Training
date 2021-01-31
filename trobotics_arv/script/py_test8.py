#!/usr/bin/env python
import rospy
from std_msgs.msg import Float32
from my_robotics.msg import my_msg

def callback(msg_data):
    greeting_msg = msg_data.name + "," + msg_data.greetings
    rospy.loginfo(greeting_msg)

def listener():
    rospy.init_node('my_eighth_node')
    rospy.Subscriber('greetings',my_msg,callback)
    rospy.spin()

if __name__ == '__main__':
    try:
        listener()
    except rospy.ROSInterruptException:
        rospy.shutdown()