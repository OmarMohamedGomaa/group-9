#! /usr/bin/env python3
import rclpy 
from rclpy.node import Node

class actionClient(Node):
    def __init__(self):
        super().__init__("actionClient")
       # figure it out idk
        self.get_logger().info("started")


    def solve_maze(self,x):
        #implement algorithm
        pass

    # Search for the wall service 



def main(args = None):
    rclpy.init(args=args)
    #driver code idk
    node = actionClient()
    rclpy.shutdown()    

if __name__ == "__main__":
    main()