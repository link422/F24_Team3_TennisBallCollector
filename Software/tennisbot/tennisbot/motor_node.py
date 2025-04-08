import lgpio
import time
import rclpy
from rclpy.node import Node
from std_msgs.msg import Int32MultiArray

LEFT_MOTORS = 17
RIGHT_MOTORS  = 27
VIBE_MOTOR = 22

class MotorNode(Node):
    def __init__(self):
        super().__init__('motor_node')
        self.h = lgpio.gpiochip_open(0)
        self.vibe_level = False
        self.debounceActive = False
        lgpio.gpio_claim_output(self.h, LEFT_MOTORS)
        lgpio.gpio_claim_output(self.h, RIGHT_MOTORS)
        lgpio.gpio_claim_output(self.h, VIBE_MOTOR)
        lgpio.gpio_write(self.h, VIBE_MOTOR, self.vibe_level)
        self.subscription = self.create_subscription(
            Int32MultiArray,
            '/controls',
            self.listener_callback,
            10)
        self.subscription  # Prevent unused variable warning

    def listener_callback(self, msg):
        # D pad up mean go forward
        if msg.data[0] == 1:
            lgpio.gpio_write(self.h, RIGHT_MOTORS, True)
            lgpio.gpio_write(self.h, LEFT_MOTORS, True)
            time.sleep(.002)
            lgpio.gpio_write(self.h, RIGHT_MOTORS, False)
            lgpio.gpio_write(self.h, LEFT_MOTORS, False)
        # D pad down means go backword
        elif msg.data[1] == 1:
            lgpio.gpio_write(self.h, RIGHT_MOTORS, True)
            lgpio.gpio_write(self.h, LEFT_MOTORS, True)
            time.sleep(.001)
            lgpio.gpio_write(self.h, RIGHT_MOTORS, False)
            lgpio.gpio_write(self.h, LEFT_MOTORS, False)
        # D pad left means go left
        elif msg.data[2] == 1:
            lgpio.gpio_write(self.h, LEFT_MOTORS, True)
            time.sleep(.0015)
            lgpio.gpio_write(self.h, LEFT_MOTORS, False)
            lgpio.gpio_write(self.h, RIGHT_MOTORS, True)
            time.sleep(.002)
            lgpio.gpio_write(self.h, RIGHT_MOTORS, False)
        # D pad right means go right
        elif msg.data[3] == 1:
            lgpio.gpio_write(self.h, RIGHT_MOTORS, True)
            time.sleep(.0015)
            lgpio.gpio_write(self.h, RIGHT_MOTORS, False)
            lgpio.gpio_write(self.h, LEFT_MOTORS, True)
            time.sleep(.002)
            lgpio.gpio_write(self.h, LEFT_MOTORS, False)
        # A button means vibration toggle
        if msg.data[4]:
            if not self.debounceActive:
                self.vibe_level = not self.vibe_level
                lgpio.gpio_write(self.h, VIBE_MOTOR, self.vibe_level)
                self.debounceActive = True
        else:
            self.debounceActive = False
        # start button is emergency stop
        if msg.data[6]:
            lgpio.gpio_write(self.h, RIGHT_MOTORS, True)
            lgpio.gpio_write(self.h, LEFT_MOTORS, True)
            time.sleep(.0015)
            lgpio.gpio_write(self.h, RIGHT_MOTORS, False)
            lgpio.gpio_write(self.h, LEFT_MOTORS, False)
            rclpy.shutdown()





        




def main(args=None):
    rclpy.init(args=args)
    node = MotorNode()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == '__main__':
    main()
