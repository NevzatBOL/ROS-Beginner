#!/usr/bin/env python

import rospy
from sensor_msgs.msg import LaserScan

def scancallback(scan):
    #print scan
    print "scan: ", scan.ranges

if __name__ == '__main__':
    rospy.init_node('lidar_read',anonymous=True)
    rospy.Subscriber('/laser/scan',LaserScan,scancallback)
    rospy.spin()
