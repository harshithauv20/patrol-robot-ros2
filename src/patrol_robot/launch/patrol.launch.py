from launch import LaunchDescription
from launch_ros.actions import Node


def generate_launch_description():
    return LaunchDescription([
        Node(package='patrol_robot', executable='obstacle_monitor',
             parameters=[{'danger_distance': 0.5, 'use_sim_time': True}]),
        Node(package='patrol_robot', executable='patrol_node',
             output='screen', parameters=[{'use_sim_time': True}]),
    ])
