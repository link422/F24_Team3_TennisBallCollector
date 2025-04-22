import time
import serial
import rclpy
from rclpy.node import Node
from std_msgs.msg import Int32



class LidarNode(Node):
    def __init__(self):
        super().__init__('lidar_node')
        self.ser = serial.Serial("/dev/ttyUSB0", 115200)
        if self.ser.isOpen() == False:
            self.ser.open()

        self.publisher_ = self.create_publisher(Int32, '/lidardata', 10)
        self.timer = self.create_timer(0.1, self.timer_callback)  # 1/10 second interval

    def timer_callback(self):
        msg = Int32()
        msg.data = 300

        counter = self.ser.in_waiting # count the number of bytes of the serial port
        if counter > 8:
            bytes_serial = self.ser.read(9)
            self.ser.reset_input_buffer()

            if bytes_serial[0] == 0x59 and bytes_serial[1] == 0x59: 

                distance = bytes_serial[2] + bytes_serial[3]*256 # multiplied by 256, because the binary data is shifted by 8 to the left (equivalent to "<< 8").                                              # Dist_L, could simply be added resulting in 16-bit data of Dist_Total.
            
                
                msg.data = int(distance)
                self.ser.reset_input_buffer()
        
        self.publisher_.publish(msg)





def main(args=None):
    rclpy.init(args=args)
    node = LidarNode()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == '__main__':
    main()
