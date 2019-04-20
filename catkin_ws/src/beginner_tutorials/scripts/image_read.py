#!/usr/bin/env python

import cv2
import rospy
from sensor_msgs.msg import Image
from cv_bridge import CvBridge

def callback(image_msg):
    bridge = CvBridge()
    image_cv = bridge.imgmsg_to_cv2(image_msg)
    
    print image_cv.shape
    
    cv2.imshow("frame",image_cv)
    cv2.waitKey(1)
    

if __name__ == '__main__':
    rospy.init_node('cv_camera',anonymous=True)
    rospy.Subscriber('/rrbot/camera1/image_raw',Image,callback)
    rospy.spin()
