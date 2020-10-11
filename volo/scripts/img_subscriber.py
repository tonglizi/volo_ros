#!/usr/bin/env python
# -*- coding: UTF-8 -*-
import rospy
from sensor_msgs.msg import Image
import cv2
from cv_bridge import CvBridge, CvBridgeError

bridge = CvBridge()
count = 0

def callback(data):
    # define picture to_down' coefficient of ratio
    print ('图像时间戳:' + str(data.header.stamp.to_sec()))
    scaling_factor = 0.5
    global count, bridge
    count = count + 1
    if count == 1:
        count = 0
        cv_img = bridge.imgmsg_to_cv2(data, "bgr8")
        cv2.imshow("frame", cv_img)
        cv2.waitKey(3)
    else:
        pass

def subscriber():
    rospy.init_node('kinect_python', anonymous=True)
    rospy.Subscriber("/kinect2/hd/image_color", Image, callback)
    rospy.spin()

if __name__ == '__main__':
    subscriber()
