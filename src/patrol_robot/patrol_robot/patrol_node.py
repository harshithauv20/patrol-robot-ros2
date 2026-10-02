import math
import rclpy
from geometry_msgs.msg import PoseStamped
from nav2_simple_commander.robot_navigator import BasicNavigator, TaskResult


def make_pose(nav, x, y, yaw):
    pose = PoseStamped()
    pose.header.frame_id = 'map'
    pose.header.stamp = nav.get_clock().now().to_msg()
    pose.pose.position.x = x
    pose.pose.position.y = y
    pose.pose.orientation.z = math.sin(yaw / 2)
    pose.pose.orientation.w = math.cos(yaw / 2)
    return pose


def main():
    rclpy.init()
    nav = BasicNavigator()

    nav.setInitialPose(make_pose(nav, -2.0, -0.5, 0.0))
    nav.waitUntilNav2Active()

    # Edit these to points that are free space on YOUR map
    waypoints = [
        make_pose(nav, 0.0, -0.5, 0.0),
        make_pose(nav, 1.0, 0.5, 1.57),
        make_pose(nav, -1.0, 0.5, 3.14),
    ]

    while rclpy.ok():
        nav.followWaypoints(waypoints)
        while not nav.isTaskComplete():
            fb = nav.getFeedback()
            if fb:
                nav.get_logger().info(
                    f'Heading to waypoint {fb.current_waypoint + 1}/{len(waypoints)}')

        result = nav.getResult()
        if result == TaskResult.SUCCEEDED:
            nav.get_logger().info('Patrol loop complete, restarting')
        else:
            nav.get_logger().warn('Patrol failed or canceled')
            break

    nav.lifecycleShutdown()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
