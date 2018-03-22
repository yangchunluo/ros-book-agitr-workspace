#!/usr/bin/env python

import rospy
from geometry_msgs.msg import Twist
import random

if __name__ == "__main__":
    rospy.init_node("publish_velocity_py", anonymous=False)
    pub = rospy.Publisher("turtle1/cmd_vel", Twist, queue_size=1000)

    rate = rospy.Rate(2);
    while not rospy.is_shutdown():
        msg = Twist()
        msg.linear.x = random.random();
        msg.angular.z = 2 * random.random() - 1;

        pub.publish(msg);

        rospy.loginfo("Sending random vel command: linear={} angular={}".format(
            msg.linear.x, msg.angular.z));
        rate.sleep();

