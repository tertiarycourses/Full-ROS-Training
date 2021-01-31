#!/usr/bin/env python
import rospy
from std_msgs.msg import String

def talker():
    rospy.init_node('my_third_node')
    pub = rospy.Publisher('greetings',String,queue_size=10)

    i = 0
    while True:
        msg_data = "Hello World %s" % i
        pub.publish(msg_data)
        rospy.sleep(1)
        i = i+1

if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        rospy.shutdown()

