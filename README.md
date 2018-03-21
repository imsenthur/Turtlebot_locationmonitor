# Turtlebot_locationmonitor
A location monitor node for a turtlebot in gazebo simulator [ROS] which subscribes to the published odometer topic and calculates the closest landmark to the bot and publishes it under the topic 'closestobject'.

#Custom message:
Created a custom message called 'LandmarkDistance' which contains name of the nearby landmark and its distance from the turtlebot.
Instructions to create a custom message can be found in http://wiki.ros.org/ROS/Tutorials/CreatingMsgAndSrv 

#Note:
Always create a subfolder for all the custom/package specific messages you create, which helps in organising your workspace and causes lesser namespace errors.
