#! /usr/bin/env python3
import rclpy 
from rclpy.node import Node
from geometry_msgs.msg import Twist
from std_msgs.msg import Bool
import time

class MyNode(Node):
    def __init__(self):
        super().__init__("first_node")
        self.publisher_ = self.create_publisher(Twist,'/cmd_vel' ,10)
        self.publisher_c = self.create_publisher( Bool,'/finish_robot/touched',10)
        m = Bool()
        m.data = True
        self.publisher_c.publish(m)
        self.direction = -1.0
        self.get_logger().info("started")
    def move(self):
        message = Twist()
        message.linear.x = 0.0 
        message.linear.y = 0.0
        message.angular.z = 1.0
        message.angular.x = 0.0
        message.angular.y = 0.0
        self.direction *= -1
        self.publisher_.publish(message)



def main(args = None):
    rclpy.init(args=args)
    node = MyNode()
    while True:
        node.move()
        time.sleep(0.5)

    rclpy.shutdown()    

if __name__ == "__main__":
    main()