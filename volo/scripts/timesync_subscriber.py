#!/usr/bin/env python
# -*- coding: UTF-8 -*-
import time

import rospy
from sensor_msgs.msg import Image

# API: https://docs.ros.org/api/message_filters/html/python/#message_filters.Subscriber
import message_filters

#tool:https://github.com/eric-wieser/ros_numpy/blob/master/README.md
#install: https://answers.ros.org/question/270439/ros_numpy-package/
import ros_numpy

import numpy as np
from sensor_msgs.msg import PointCloud2
from multiprocessing import Queue, Process

q=Queue(20)#TODO 考虑用双buffer，减少锁的开销

def callback(img_msg,pts_msg): # producer
    assert isinstance(img_msg,Image)
    assert isinstance(pts_msg,PointCloud2)
    print ('图像时间戳:' + str(img_msg.header.stamp.to_sec()))
    print ('点云时间戳:' + str(pts_msg.header.stamp.to_sec()))

    pc = ros_numpy.numpify(pts_msg)
    # points=np.zeros((pc.shape[0],3))
    # points[:,0]=pc['x']
    # points[:,1]=pc['y']
    # points[:,2]=pc['z']

    img=ros_numpy.numpify(img_msg)

    data_unit=[img,pc]
    global q
    q.put(data_unit)

def consumer(q,name): # consumer
    while True:
        print 'Consumer see queue length:'+str(q.qsize())
        q.get()
        #mock volo processing: 10fps
        fps=3.0
        time.sleep(1/fps)
        print 'vlolo processing...'

def subscriber():
    rospy.init_node('timesync_producer', anonymous=True)
    img_sub=message_filters.Subscriber('/kinect2/hd/image_color',Image)
    pts_sub=message_filters.Subscriber('/velodyne_points',PointCloud2)
    #调用ROS的message_filters进行数据时间同步
    ts=message_filters.ApproximateTimeSynchronizer([img_sub,pts_sub],10,0.005)
    ts.registerCallback(callback)
    rospy.spin()

if __name__ == '__main__':
    c=Process(target=consumer,args=(q,'volo'))
    c.start()
    subscriber()
