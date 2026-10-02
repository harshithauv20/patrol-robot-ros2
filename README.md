# Autonomous Patrol Robot (ROS 2 Jazzy, Python)

A simulated TurtleBot3 Burger in Gazebo Harmonic, using SLAM Toolbox for mapping and Nav2 for navigation, with custom Python (rclpy) nodes.

**Status:** SLAM mapping working. Nav2 patrol in testing.

## Tech stack
ROS 2 Jazzy, Gazebo Harmonic, SLAM Toolbox, Nav2, RViz2, Python

## Nodes
- `obstacle_monitor`: subscribes to `/scan`, publishes `/obstacle_close` (Bool) when an obstacle is within a set distance
- `patrol_node`: sends waypoints to Nav2 using Nav2 Simple Commander (untested end to end)

## Lesson learned
On Jazzy, the Gazebo bridge subscribes to `/cmd_vel` as `TwistStamped`. A `Twist` publisher does not connect.
