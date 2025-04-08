import xbox
import rclpy
from rclpy.node import Node
from std_msgs.msg import Int32MultiArray

class ControllerNode(Node):
    def __init__(self):
        super().__init__('controller_node')
        self.joy = xbox.Joystick()
        self.publisher_ = self.create_publisher(Int32MultiArray, '/controls', 10)
        self.timer = self.create_timer(0.25, self.timer_callback)  # 1/4 second interval

    def timer_callback(self):
        msg = Int32MultiArray()
        msg.data = [0, 0, 0, 0, 0, 0, 0]  # Example array data
        if self.joy.dpadUp():
            msg.data[0] = 1
        if self.joy.dpadDown():
            msg.data[1] = 1
        if self.joy.dpadLeft():
            msg.data[2] = 1
        if self.joy.dpadRight():
            msg.data[3] = 1
        if self.joy.A():
            msg.data[4] = 1
        if self.joy.B():
            msg.data[5] = 1
        if self.joy.Start():
            msg.data[6] = 1
        self.publisher_.publish(msg)

def main(args=None):
    rclpy.init(args=args)
    node = ControllerNode()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == '__main__':
    main()
