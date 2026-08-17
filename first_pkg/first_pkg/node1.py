#! /usr/bin/env python3
import rclpy 
from rclpy.node import Node
from geometry_msgs.msg import Twist
import time

class MyNode(Node):
    def __init__(self):
        super().__init__("first_node")
        self.get_logger().info("Hello ")
        self.publisher_ = self.create_publisher(Twist,'/cmd_vel' ,10)
        self.direction = 1.0
        self.get_logger().info("started")
    def move(self):
        message = Twist()
        message.linear.x = self.direction * 3
        self.direction *= -1
        self.publisher_.publish(message)
        self.get_logger().info("moved")


def main(args = None):
    rclpy.init(args=args)
    node = MyNode()
    while True:
        node.move()
        time.sleep(5)

    rclpy.shutdown()    

if __name__ == "__main__":
    main()