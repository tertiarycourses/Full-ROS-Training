#!/usr/bin/env python
# works for actual OM_with_TB3 ONLY!
# does not work for actual OM

# unable to execute this python file! changing joint positions gives errors BUT NOT gripper positions
# error message: rospy.service.ServiceException: transport error completing service call: 
# unable to receive data from sender, check sender's logs for details
# when this python code is executed, rosservice call commands via terminal will produce the following error:
# ERROR: Unable to communicate with service [/arm/moveit/set_joint_position], 
# address [rosrpc://192.168.0.XXX:54163]

# ensure moveit is run first

import rospy
from open_manipulator_msgs.msg import JointPosition
from open_manipulator_msgs.srv import SetJointPosition
import math

def talker():
	rospy.init_node('OM_tb3_publisher')	#Initiate a Node called 'OM_tb3_publisher'
	set_joint_position = rospy.ServiceProxy('/arm/moveit/set_joint_position', SetJointPosition)
        set_gripper_position = rospy.ServiceProxy('/om_with_tb3/gripper', SetJointPosition)
	
	while not rospy.is_shutdown():
		joint_position = JointPosition()
		joint_position.joint_name = ['joint1','joint2','joint3','joint4']
		joint_position.position =  [-0.5, 0, 0.5, -0.5]		# in radians
		resp1 = set_joint_position('planning_group',joint_position, 3)
		gripper_position = JointPosition()
		gripper_position.joint_name = ['gripper']
		gripper_position.position =  [0.01]	# -0.01 for fully close and 0.01 for fully open
		respg2 = set_gripper_position('planning_group',gripper_position, 3)

	rospy.spin()

if __name__== '__main__':
	try:
		talker()
	except rospy.ROSInterruptException:
		pass
