#! /usr/bin/env python3
import rclpy 
from rclpy.node import Node
from geometry_msgs.msg import Twist


class actionServer(Node):
    def __init__(self):
        super().__init__("actionServer")
        self.publisher_ = self.create_publisher(Twist,'/cmd_vel' ,10)
        #subscribe to odom
        self.get_logger().info("started")


    def moveX(self,x):
        #implement action not just a function
        pass

    def moveYaw(self,Yaw):
        #implement action not just a function
        pass



def main(args = None):
    rclpy.init(args=args)
    #driver code idk
    node = actionServer()
    rclpy.shutdown()    

if __name__ == "__main__":
    main()