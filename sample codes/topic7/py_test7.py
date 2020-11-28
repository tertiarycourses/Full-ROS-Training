#!/usr/bin/env python
import rospy
from std_msgs.msg import String
from my_robotics.msg import my_msg

def talker():
    rospy.init_node('my_seventh_node')
    pub = rospy.Publisher('greetings',my_msg,queue_size=10)

    i = 0
    msg_data = my_msg()
    while True:
        msg_data.name = "Ally"
        msg_data.greetings = "Hello %s" %i
        pub.publish(msg_data)
        rospy.sleep(1)
        i = i+1

if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        rospy.shutdown()

