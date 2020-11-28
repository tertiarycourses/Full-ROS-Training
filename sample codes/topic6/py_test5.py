#!/usr/bin/env python
import rospy
from std_msgs.msg import Float32
import random

def talker():
    rospy.init_node('temp_sensor_node')
    pub = rospy.Publisher('temperature',Float32,queue_size=10)

    while True:
        temp_data = 28.0 + random.random()+2
        pub.publish(temp_data)
        rospy.sleep(1)

if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        rospy.shutdown()