1. The ROS2 package here is used to control all aspects of the system. This includes interfacing with the LiDAR, motors, vibration motors, controller and LCD. A controller is used to move the system, turn on and off the vibration motors, reset the LCD, and do an emergency stop
2. ROS2-jazzy, colcon, xboxdrv, xbox.py from FRC4564, serieal, and lgpio
3. In order to install this software create or naviagate to a ROS2 workspace. When a ROS2 workspace is created a subfolder called src is created and inside of that is where you put this package.
4. Once the package is placed in the ROS2 workspace naviagte to the main folder of the workspace and type the command
```
colcon build
```
After the package is build it needs to be sourced with the following command while still in the ROS2 workspace
```
source install/setup.bash
```
Once it is sourced the package can be run by typing in 
```
ros2 launch tennisbot tennisbot.launch.py
```
