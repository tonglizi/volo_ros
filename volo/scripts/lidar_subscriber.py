#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# ros点云数据格式sensor_msgs/PointCloud2转换成python可处理格式
import rospy
#tool:https://github.com/eric-wieser/ros_numpy/blob/master/README.md
#install: https://answers.ros.org/question/270439/ros_numpy-package/
import ros_numpy
import numpy as np
from sensor_msgs.msg import PointCloud2
#from sensor_msgs import point_cloud2

def callback(data):
    assert isinstance(data, PointCloud2)
    pc = ros_numpy.numpify(data)
    points=np.zeros((pc.shape[0],3))
    points[:,0]=pc['x']
    points[:,1]=pc['y']
    points[:,2]=pc['z']

    print ('点云时间戳:'+str(data.header.stamp.to_sec()))
    #
    # gen=point_cloud2.read_points(data)
    # print type(gen)
    # for p in gen:
    #     print p

def subscriber():
    rospy.init_node('velodyne_python', anonymous=True)
    rospy.Subscriber("/velodyne_points", PointCloud2, callback)
    rospy.spin()

if __name__ == '__main__':
    subscriber()
