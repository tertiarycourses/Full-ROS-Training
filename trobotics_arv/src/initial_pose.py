#!/usr/bin/env python
 
import rospy
from geometry_msgs.msg import PoseWithCovarianceStamped
from tf.transformations import quaternion_from_euler
 
rospy.init_node('init_pos')
pub = rospy.Publisher('/initialpose', PoseWithCovarianceStamped, queue_size = 10)
rospy.sleep(3)
checkpoint = PoseWithCovarianceStamped()
 
# Use $ rostopic echo /odom -n1 to obtain poses (both position and orientation)

checkpoint.pose.pose.position.x = 8.16914081573
checkpoint.pose.pose.position.y = 3.16029000282
checkpoint.pose.pose.position.z = 0.0
 
[x,y,z,w]=quaternion_from_euler(0.0,0.0,0.0)
checkpoint.pose.pose.orientation.x = 0.0
checkpoint.pose.pose.orientation.y = 0.0
checkpoint.pose.pose.orientation.z = 0.0769307017326
checkpoint.pose.pose.orientation.w = 0.997036457062
 
print checkpoint
pub.publish(checkpoint)
	
