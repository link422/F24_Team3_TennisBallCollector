import lgpio
import time
import rclpy
from rclpy.node import Node
from std_msgs.msg import Int32MultiArray
from std_msgs.msg import Int32
# Define GPIO to LCD mapping
LCD_RS = 5
LCD_E  = 6
LCD_D4 = 25
LCD_D5 = 24
LCD_D6 = 23
LCD_D7 = 18


# Define some device constants
LCD_WIDTH = 16    # Maximum characters per line
LCD_CHR = True
LCD_CMD = False

LCD_LINE_1 = 0x80 # LCD RAM address for the 1st line
LCD_LINE_2 = 0xC0 # LCD RAM address for the 2nd line

# Timing constants
E_PULSE = 0.0005
E_DELAY = 0.0005

class LCDNode(Node):
    def __init__(self):
        super().__init__('lcd_node')
        self.h = lgpio.gpiochip_open(0)
        self.ballCount = 0
        self.debounce_state = False
        self.debounce_state_two = False
        self.timestamp = time.time()
        lgpio.gpio_claim_output(self.h, LCD_E) # E
        lgpio.gpio_claim_output(self.h, LCD_RS) # RS
        lgpio.gpio_claim_output(self.h, LCD_D4) # DB4
        lgpio.gpio_claim_output(self.h, LCD_D5) # DB5
        lgpio.gpio_claim_output(self.h, LCD_D6) # DB6
        lgpio.gpio_claim_output(self.h, LCD_D7) # DB7

        # Initialise display
        self.lcd_byte(0x33,LCD_CMD) # 110011 Initialise
        self.lcd_byte(0x32,LCD_CMD) # 110010 Initialise
        self.lcd_byte(0x06,LCD_CMD) # 000110 Cursor move direction
        self.lcd_byte(0x0C,LCD_CMD) # 001100 Display On,Cursor Off, Blink Off
        self.lcd_byte(0x28,LCD_CMD) # 101000 Data length, number of lines, font size
        self.lcd_byte(0x01,LCD_CMD) # 000001 Clear display
        time.sleep(E_DELAY)

        

        self.subscriptionOne = self.create_subscription(
            Int32MultiArray,
            '/controls',
            self.controller_callback,
            10)
        self.subscriptionOne  # Prevent unused variable warning

        self.subscriptionTwo = self.create_subscription(
            Int32,
            '/lidardata',
            self.lidar_callback,
            10)
        self.subscriptionTwo  # Prevent unused variable warning



    def controller_callback(self, msg):

        if msg.data[5]: #button B is pressed
            if not self.debounce_state:
                self.ballCount = 0
                self.debounce_state = True
        else:
            self.debounce_state = False

        # start button is emergency stop
        if msg.data[6]:
            lgpio.gpiochip_close(self.h)
            rclpy.shutdown()

    def lidar_callback(self, msg):
        if msg.data < 30:
            if not self.debounce_state_two:
                self.ballCount = self.ballCount + 1
                self.debounce_state_two = True
        else:
            self.debounce_state_two = False
        
        # Send some test
        if (time.time() - self.timestamp) > 3:
            bottomText = "counted " + str(self.ballCount)
            self.lcd_string("Tennis balls",LCD_LINE_1)
            self.lcd_string(bottomText,LCD_LINE_2)
            self.timestamp = time.time()



    def lcd_byte(self, bits, mode):
        # Send byte to data pins
        # bits = data
        # mode = True  for character
        #        False for command

        lgpio.gpio_write(self.h, LCD_RS, mode) # RS

        # High bits
        lgpio.gpio_write(self.h, LCD_D4, False)
        lgpio.gpio_write(self.h, LCD_D5, False)
        lgpio.gpio_write(self.h, LCD_D6, False)
        lgpio.gpio_write(self.h, LCD_D7, False)
        if bits&0x10==0x10:
            lgpio.gpio_write(self.h, LCD_D4, True)
        if bits&0x20==0x20:
            lgpio.gpio_write(self.h, LCD_D5, True)
        if bits&0x40==0x40:
            lgpio.gpio_write(self.h, LCD_D6, True)
        if bits&0x80==0x80:
            lgpio.gpio_write(self.h, LCD_D7, True)

        # Toggle 'Enable' pin
        self.lcd_toggle_enable()

        # Low bits
        lgpio.gpio_write(self.h, LCD_D4, False)
        lgpio.gpio_write(self.h, LCD_D5, False)
        lgpio.gpio_write(self.h, LCD_D6, False)
        lgpio.gpio_write(self.h, LCD_D7, False)
        if bits&0x01==0x01:
            lgpio.gpio_write(self.h, LCD_D4, True)
        if bits&0x02==0x02:
            lgpio.gpio_write(self.h, LCD_D5, True)
        if bits&0x04==0x04:
            lgpio.gpio_write(self.h, LCD_D6, True)
        if bits&0x08==0x08:
            lgpio.gpio_write(self.h, LCD_D7, True)

        # Toggle 'Enable' pin
        self.lcd_toggle_enable()

    def lcd_toggle_enable(self):
        # Toggle enable
        time.sleep(E_DELAY)
        lgpio.gpio_write(self.h, LCD_E, True)
        time.sleep(E_PULSE)
        lgpio.gpio_write(self.h, LCD_E, False)
        time.sleep(E_DELAY)

    def lcd_string(self, message,line):
        message = message.ljust(LCD_WIDTH," ")

        self.lcd_byte(line, LCD_CMD)

        for i in range(LCD_WIDTH):
            self.lcd_byte(ord(message[i]),LCD_CHR)

def main(args=None):
    rclpy.init(args=args)
    node = LCDNode()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == '__main__':
    main()
