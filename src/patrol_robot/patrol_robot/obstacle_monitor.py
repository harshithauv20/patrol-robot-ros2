
cat > ~/ros2_ws/src/patrol_robot/patrol_robot/obstacle_monitor.py << 'EOF'
import rclpy
from rclpy.node import Node
from rclpy.qos import qos_profile_sensor_data
from sensor_msgs.msg import LaserScan
from std_msgs.msg import Bool


class ObstacleMonitor(Node):
    def __init__(self):
        super().__init__('obstacle_monitor')
        self.declare_parameter('danger_distance', 0.4)
        self.sub = self.create_subscription(
            LaserScan, 'scan', self.on_scan, qos_profile_sensor_data)
        self.pub = self.create_publisher(Bool, 'obstacle_close', 10)

    def on_scan(self, msg: LaserScan):
        limit = self.get_parameter('danger_distance').value
        valid = [r for r in msg.ranges if msg.range_min < r < msg.range_max]
        close = bool(valid) and min(valid) < limit
        self.pub.publish(Bool(data=close))
        if close:
            self.get_logger().warn(f'Obstacle at {min(valid):.2f} m')


def main():
    rclpy.init()
    rclpy.spin(ObstacleMonitor())
    rclpy.shutdown()


if __name__ == '__main__':
    main()
