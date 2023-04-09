import rclpy
from rclpy.node import Node
import time
from nav_msgs.msg import Odometry
from geometry_msgs.msg import Twist


class BaseControl(Node):
    def __init__(self):
        super().__init__('base_control_node')
        # Publisher
        self.twist_pub = self.create_publisher(Twist, '/cmd_vel', 10)
        # Value
        self.twist_value = Twist()

    def translateDist(self, dist, speed = 0.2):
        self.twist_value.linear.x = dist/abs(dist)*speed
        target_time = abs(dist/speed)
        start_time = time.time()
        end_time = time.time()
        while end_time - start_time <= target_time:
            self.twist_pub.publish(self.twist_value)
            end_time = time.time()
            time.sleep(0.1)
        self.twist_value.linear.x = 0.0
        self.twist_pub.publish(self.twist_value)
        self.get_logger().info(f"Finish 'translateDist'.")

    def rotateAngle(self):
        print("ジャパン!")

def main():
    rclpy.init()
    bc = BaseControl()
    bc.translateDist(0.3)
    rclpy.shutdown()
