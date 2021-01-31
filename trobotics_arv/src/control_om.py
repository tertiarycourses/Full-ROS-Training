#!/usr/bin/env python
# works for OM simulation ONLY!
# does not work for OM_with_TB3

import rospy					#import the python library for ROS
from std_msgs.msg import Float64		#import Float64 message from the std_msgs package
import math

def talker():
	rospy.init_node('OM_publisher')	#Initiate a Node called 'OM_publisher'
	grip = rospy.Publisher('/open_manipulator/gripper_position/command', Float64, queue_size=10)
	pub1 = rospy.Publisher('/open_manipulator/joint1_position/command', Float64, queue_size=10)
	pub2 = rospy.Publisher('/open_manipulator/joint2_position/command', Float64, queue_size=10)
	pub3 = rospy.Publisher('/open_manipulator/joint3_position/command', Float64, queue_size=10)
	pub4 = rospy.Publisher('/open_manipulator/joint4_position/command', Float64, queue_size=10)
	rate = rospy.Rate(10)

	while not rospy.is_shutdown():
		grippos = 0.01
		#Allowed grip values from -0.01 (fully closed) to 0.01 (fully open)
		#For joint positions, refer to orientation reference for OM
		position1 = -0.5
		position2 = 0
		position3 = 0.5
		position4 = -0.5
		rospy.loginfo(grippos)
		rospy.loginfo(position1)
		rospy.loginfo(position2)		
		rospy.loginfo(position3)		
		rospy.loginfo(position4)
		grip.publish(grippos)
		pub1.publish(position1)
		pub2.publish(position2)
		pub3.publish(position3)
		pub4.publish(position4)

if __name__== '__main__':
	try:
		talker()
	except rospy.ROSInterruptException:
		pass
