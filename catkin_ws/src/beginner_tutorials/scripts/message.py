#!/usr/bin/env python
import rospy
from beginner_tutorials.msg import Num

def talker():
    rospy.init_node('message_talker',anonymous=True)
    pub = rospy.Publisher('talker',Num)
    r = rospy.Rate(10)
    msg = Num()
    msg.num = 4
    
    while not rospy.is_shutdown():
        rospy.loginfo(msg)
        pub.publish(msg)
        r.sleep()

if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException: pass
