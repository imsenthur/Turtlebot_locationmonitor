#!/usr/bin/env python

import rospy
import math
from locomotion_monitor_msgs.msg import LandmarkDistance
from nav_msgs.msg import Odometry

def distance(x1, y1, x2, y2):
	x = x1 - x2
	y = y1 - y2
	return math.sqrt(x**2 + y**2)

class LandmarkMonitor(object):

	def __init__(self, pub, landmarks):
		self._pub = pub
		self._landmarks = landmarks

	def callback(self, msg):
		x = msg.pose.pose.position.x
		y = msg.pose.pose.position.y
		closest_object = None
		closest_distance = None
		for o_name, o_x, o_y in self._landmarks:
			dist = distance(x, y, o_x, o_y)
			if closest_distance is None or dist < closest_distance:
				closest_object = o_name
				closest_distance = dist

		ld = LandmarkDistance()
		ld.landmark = closest_object
		ld.distance = closest_distance
		self._pub.publish(ld)
		#rospy.loginfo('Closest object: {}'.format(closest_object))	

def main():

	landmarks = [('cube', 0.31, -0.99), ('Dumpster', 0.11, -2.42), ('Cylinder', -1.14, -2.88), ('Barrier', -2.59, -0.83), ('Bookshelf', -0.09, 0.53)]
	pub = rospy.Publisher('closestobject', LandmarkDistance, queue_size =10)
	monitor = LandmarkMonitor(pub, landmarks)
	rospy.init_node('location_monitor')
	rospy.Subscriber("/odom", Odometry, monitor.callback)
	rospy.spin()

if __name__ == '__main__':
	main()