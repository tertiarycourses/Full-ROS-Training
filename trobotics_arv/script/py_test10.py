#!/usr/bin/env python
import rospy
from std_msgs.msg import Float32
from my_robotics.msg import iot_sensor

def callback(msg_data):
    temp_data = "Temperature = %s" % msg_data.temperature
    rospy.loginfo(temp_data)

def listener():
    rospy.init_node('my_tenth_node')
    rospy.Subscriber('temperature',iot_sensor,callback)
    rospy.spin()

if __name__ == '__main__':
    try:
        listener()
    except rospy.ROSInterruptException:
        rospy.shutdown()