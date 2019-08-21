#!/usr/bin/env python

import numpy as np
import sys

# add ROS
import rospy
from std_msgs.msg import Int64
from std_msgs.msg import String
from people_msgs.msg import PositionMeasurementArray

project_name = 'black'

def callback_people(msg):
    global path, img_name, project_name
    # print msg.people[0].pos.x
    for i in range(len(msg.people)):
        if msg.people[i].pos.x < 2 and msg.people[i].pos.x > 0 and msg.people[i].pos.y < 2 and msg.people[i].pos.y > 0.5: #upper left side
            project_name = 'right_arrow'
        elif msg.people[i].pos.x < 2 and msg.people[i].pos.x > 0 and msg.people[i].pos.y > -2 and msg.people[i].pos.y < -0.5:  #upper right side
            project_name = 'left_arrow'
        elif msg.people[i].pos.x < 2 and msg.people[i].pos.x > 0 and msg.people[i].pos.y > -0.5 and msg.people[i].pos.y < 0.5:  #upper right side
            project_name = 'circle_image'
        else:
            project_name = 'black'

if __name__ == '__main__' :

    rospy.init_node('low_level_control')
    rospy.Subscriber('people_tracker_measurements', PositionMeasurementArray, callback_people)
    pub_project = rospy.Publisher('project', String, queue_size=5)
    rate = rospy.Rate(10)

    global project_name

    while not rospy.is_shutdown():
        pub_project.publish(project_name)
        rate.sleep()
