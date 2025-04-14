# Tennis Ball Collector Experimental Analysis 

## Purpose and Justification

#### BATTERY EXPERIMENT
Testing the battery’s life expectancy and safety is integral to making the Tennis Ball Collector 
remote-controlled. The batteries used are expected to run for the entire process of ball collection; 
If they fail, it can cause damage not only to the other components but also danger to the user themself. 

#### LCD AND LIDAR SENSOR EXPERIMENT 
The goal of this experiment is to test the accuracy of the sensors to detect a tennis ball and increment 
the counter on the LCD. The proper operation of these devices is crucial for the intended purpose 
of our device. Our device is expected to update the user with an accurate ball count so they know how many 
balls have been collected already. The extent of the data collected through the experiment is outlined in 
the detailed procedure section. 

#### CONTROLLER EXPERIMENT 
To test the functionality of the controller, a simple python script was used from 
https://github.com/FRC4564/Xbox. This allowed for each button to be tested individually and ensured that 
it would be useable with other Python files. Using the code made to work with the ROS2 package, the arrays of 
integers produced are recorded. These recordings were taken for 5 button presses of each button used in the 
ROS2 package. This will ensure that each button pressed is accounted for correctly by ROS to ensure that the 
system can be controlled correctly every time. 

## Detailed Procedure 

#### BATTERY EXPERIMENT 
- *Connect the first 12-Volt into the motor driver subsystem.*

- *Turn on the motor and start the timer.*

- *Let it run until the battery runs out of power or the motor stops moving.*

- *Test motor power by turning the motor switch on and off again intermittently.* 

- *This test allows us to see any issues that arise in long-term constant connection.* 

- *Connect the second 12-Volt battery into the 5-Volt stepdown input*

- *Connect the Raspberry Pi and vibration subsystem to 5-Volt stepdown output*

- *Start a timer again to calculate the length of time it stays on.*

- *Wait until the Raspberry Pi has powered off or until the vibration motors no longer turn on.*


#### LCD AND LIDAR SENSOR  EXPERIMENT 

- *First, the lidar sensors (2) are connected to the Raspberry Pi along with the LCD.* 

- *The code for sensing and counting the tennis balls as well as displaying the count on the LCD shall be loaded onto the Raspberry Pi, and both operate on the boot up of the Pi.*

- *Then, perform a series of trials on the sensor and display. There are 5 trials consisting of 10 attempts each, where a ball passes by both sensors and the accuracy of the sensors is tested.* 

- *Once past the sensor, the code loaded onto the Raspberry Pi shall increment the ball count to be viewed on the LCD.*


#### CONTROLLER EXPERIMENT 
- *Plug the controller into the Raspberry Pi*

- *Download the xbox.py and sample.py files from https://github.com/FRC4564/Xbox*

- *Run the command sudo python3 sample.py* 

- *Test different buttons on the controller and observe them on the terminal*

- *Once this test is complete as long build the ros2 package using the command colcon build* 

- *After the package is built, launch the package using the command ros2 launch tennisbot tennisbot.launch.py*

- *In a new terminal, type in the command ros2 topic echo/controls*

- *In the terminal, an array of integers can be seen and change from 0 to 1 when a button is pressed then back to 0 when let go*

- *Record the array for each button press 5 times* 

## Expected Results
#### BATTERY EXPERIMENT 
The expected result for the Motor battery is around 52 minutes due to the battery’s output and the consumption of the driver. The Raspberry Pi and DC motors are expected to run for at least an hour on their battery. This will stay on with no overheating or crashing of data, this can be assumed because of the rated 2.6 Ah of both batteries used. 

#### LCD AND LIDAR SENSOR EXPERIMENT 
The expected result of this experiment is an accurate count of tennis balls collected, as interpreted by the Lidar sensors, shown on the LCD. When each ball passes by the sensor, the count on the display will be incremented to the correct amount. 

#### CONTROLLER EXPERIMENT 
The experiment is expected to have 100% accuracy in detecting controller inputs due to having ensured that the code works and interacts nicely with ROS2. It is expected for the up arrow to change index 0, down arrow to change index 1, left arrow to change index 2, right arrow to change index 3, button A to change index 4, button B to change index 5, and button start to change index 6. 

## Actual Results

#### BATTERY EXPERIMENT 
![Screenshot (411)](https://github.com/user-attachments/assets/13956ba8-6a0c-4bfe-8f99-9f64f7b68b56)

#### LCD AND LIDAR SENSOR EXPERIMENT 
![Screenshot (412)](https://github.com/user-attachments/assets/403f0627-8332-40b8-a6a5-af0f3b84ad3f)

#### CONTROLLER EXPERIMENT 
![Screenshot (413)](https://github.com/user-attachments/assets/5b6a0667-5aaf-4fa2-a1cb-44ed17a86053)

## Interpretation and Conclusions

#### BATTERY EXPERIMENT 
The 12 Volt battery connected to the driver motor was overly discharged to test its capabilities and the safety of the battery. The battery ran for over an hour, and around an hour and 20 minutes in, the motor started rotating at a slower rate. After 2 hours of running the battery loses its ability to recharge due to a short circuit. These results show the importance of battery usage and maintain charge for the RC Tennis Ball Collector. 

#### LCD AND LIDAR SENSOR EXPERIMENT
After running through the five trials on the sensor, we were able to come out with 100% accuracy. This lets us know the sensors operate for their intended purpose successfully with no error. Not only was the detection of the sensors correct, but the results were also displayed correctly on the LCD. The only errors we noticed was a ghost count during the boot up of the Pi, which we ruled to possible movements on our part while this was going on. Aside from that, when the count was reset and the attempts took place, we were given accurate results. 

#### CONTROLLER EXPERIMENT 
Based on the results of this experiment, it can be concluded that the controller is accurately being represented by the ROS2 topic. Every button press tested for each trial was displayed correctly from the ROS2 topic, which means that the system is getting the input every time, ensuring that no errors can occur that would prevent the emergency stopping of the system. These results perfectly matched what was expected as there was 100% accuracy throughout the trials.

## CONCLUSION  
Two out of the three experiments were successful, and while the third was not entirely successful, it still provided valuable insights that will help improve the final design. Importantly, all three experiments met the project specifications. The LCD and LiDAR tests confirmed that the balls could be accurately counted and that the data could be displayed in a clear and meaningful way. The controller tests demonstrated that the device can be remotely operated, the ball counter reset, the vibration system toggled, and the device safely stopped in the event of an emergency. Battery testing showed that the device can operate for extended periods without issue. However, we discovered that running the device continuously for multiple hours may cause the battery to fail to recharge after being fully drained. As a result, we will advise users to power off the device when not in use and avoid running it for more than one hour at a time. Since the design constraints did not require extended continuous use, this limitation does not pose a problem for meeting project requirements.


### Statement of Contributions 
Maxwell Wynne: Worked on the Lidar/LCD experiment. Wrote a portion of Lidar/LCD analysis (Detailed Procedure, Expected Results, Results) 

Tate Finley: Worked on the Lidar/LCD experiment. Wrote a portion of Lidar/LCD analysis (Purpose, Logged results, Results) 

Carter Brady: Worked on the LiDAR/LCD and controller experiments design and execution. Did data analysis and wrote controller experiment report. Wrote the conclusion 

Gabriel Dubose: Worked on the Battery experiments and took the time of how each experiment lasted. Wrote a portion of the Battery Analysis. 

Ashli Watkins: Assisted Gabriel with the Battery experiments 

Cindy Escobar: Recorded information and converted our experiments to markdown for submission 


