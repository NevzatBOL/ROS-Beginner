#!/usr/bin/env python
#-*-coding: utf-8 -*-

import rospy
from std_msgs.msg import String

def talker():
	pub = rospy.Publisher('chatter',String,queue_size=10) #yayıncımızı olusrutduk.
	rospy.init_node('talker',anonymous=True)
	rate = rospy.Rate(10) #10hz

	while( not rospy.is_shutdown()):
		hello_str="hello world %s" % rospy.get_time()
		rospy.loginfo(hello_str)
		pub.publish(hello_str) #mesaji yayinlar
		rate.sleep()


if __name__ == '__main__':
	try:
		talker()
	except rospy.ROSInterreptException:
		pass

