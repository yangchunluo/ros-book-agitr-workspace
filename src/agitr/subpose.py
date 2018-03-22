#!/usr/bin/env python

import rospy
from turtlesim.msg import Pose

def poseMessageReceived(data):
    rospy.loginfo("position=({:.2f}, {:.2f}), direction={:.2f}".format(data.x, data.y, data.theta))

if __name__ == "__main__":
    rospy.init_node("subscribe_to_pose_py", anonymous=False)
    rospy.Subscriber("turtle1/pose", Pose, poseMessageReceived)
    rospy.spin()
