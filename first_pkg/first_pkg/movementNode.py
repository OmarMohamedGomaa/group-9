#! /usr/bin/env python3
import rclpy 
from rclpy.node import Node
from geometry_msgs.msg import Twist
from nav_msgs.msg import Odometry
import time


class actionServer(Node):
    def __init__(self):
        super().__init__("actionServer")
        self.publisher_ = self.create_publisher(Twist,'/cmd_vel' ,10)
        self.subscrib_odom = self.create_subscription(Odometry,'/odom',self.current_pose,10)
        self.Pose = None
        self.current_yaw = 0.0
        self.get_logger().info("started")


    def moveX(self,x):
        #implement action not just a function
        pass

    def moveYaw(self,Yaw):
        rclpy.spin_once(self)
        start_angle = self.current_yaw

        

        twist = Twist()
        speed = 0.4
        twist.angular.z = speed if Yaw > 0 else -speed #set the rotation direction (positive = left, negative = right)

        
        while rclpy.ok(): #spin until the robot reaches the angle we want 
            rclpy.spin_once(self)

            # measure how much the robot has turned so far
            angle_turned = self.current_yaw - start_angle

            # handle passing the 180-degree boundary (-pi / +pi)
            if angle_turned > 3.14159:
                angle_turned -= 2 * 3.14159
            elif angle_turned < -3.14159:
                angle_turned += 2 * 3.14159

            # stop condition: reached or exceeded target angle
            if abs(angle_turned) >= abs(Yaw):
                break

            self.publisher_.publish(twist)

        #stop the rotation
        twist.angular.z = 0.0 
        self.publisher_.publish(twist)
        self.get_logger().info("Yaw rotation finished!")

    def current_pose(self,msg:Odometry):
        self.Pose = (msg.pose.pose.position.x , msg.pose.pose.position.y )
        self.current_yaw = (msg.pose.pose.orientation.z,msg.pose.pose.orientation.w)
        time.sleep(1)
        output = f"""
                     Pos:{self.Pose}
                     orientation:{self.current_yaw}
                     Linear :{(msg.twist.twist.linear.x,msg.twist.twist.linear.y)}
                     angular: {(msg.twist.twist.angular.z)}"""

def main(args = None):
    rclpy.init(args=args)
    node = actionServer()
    rclpy.spin(node)
    rclpy.shutdown()    

if __name__ == "__main__":
    main()