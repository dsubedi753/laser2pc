#! /usr/bin/env python

import rospy
from sensor_msgs.msg import PointCloud2
from laser_assembler.srv import AssembleScans2

rospy.init_node ("laser2PointCloud")
rospy.wait_for_service ("assemble_scans2")
assemble_scans = rospy.ServiceProxy ('assemble_scans2', AssembleScans2)

pub = rospy.Publisher ("/laser_pointcloud", PointCloud2, queue_size=1)

r = rospy.Rate(1)

while not rospy.is_shutdown():
    try:
        resp = assemble_scans(rospy.Time(0,0), rospy.get_rostime())
        pub.publish (resp.cloud)
        
    except rospy.ServiceException, e:
        print "Service call for PC conversion failed: %s"%e
        
    r.sleep()