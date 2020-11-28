#!/usr/bin/env python
import rospy
from std_msgs.msg import Float32
from my_robotics.msg import iot_sensor
import random

def talker():
    rospy.init_node('temp_sensor_node')
    pub = rospy.Publisher('temperature',iot_sensor,queue_size=10)

    temp_data = iot_sensor()
    i = 1
    while True:
        temp_data.id = i
        temp_data.temperature = 28.0 + random.random()+2
        pub.publish(temp_data)
        rospy.sleep(1)

if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        rospy.shutdown()