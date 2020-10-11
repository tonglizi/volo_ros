#!/usr/bin/env python
# -*- coding: UTF-8 -*-
import rospy #导入rospy客户端
from std_msgs.msg import String #导入std_msg/string这个数据类型
 
def talker():
    pub = rospy.Publisher('chatter', String, queue_size=10) #话题的名称chatter
    rospy.init_node('talker', anonymous=True) #初始化节点，节点的名称为talker,名字要唯一
    rate = rospy.Rate(10) # 10hz,创建rage对象，与sleep()函数结合使用，控制话题消息发布的频率
    while not rospy.is_shutdown():
        hello_str = "hello world %s" % rospy.get_time()
        rospy.loginfo(hello_str)#函数在屏幕输出信息，这个信息存储在hello_str当中
        pub.publish(hello_str)
        rate.sleep()#用于控制发布的频率
 
if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass
