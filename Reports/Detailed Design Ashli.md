# Detailed Design

## Function of the Subsystem

The objective of the Motor subsystem is to help navigate the tennis ball collector [1] installed on the wheels using DC motors [2] by increasing the mobility of already established wheels on the tennis ball collector [1]. Several featured functions will be included in the composition of this subsection including:
  1. Connecting DC motors [2] to power supply and raspberry pi [3]
  2. Connecting tennis ball collector's [1] dual shaft wheels to the Raspberry Pi
  3. Controlling movement and rotation of the collector [1] without any manual help
  4. Recieving inputs of direction from RC subsystem

## Specifications and Constraints
- The DC motors [2] shall be connected to the power supply and raspberry pi [3].
  - Rationale: The motors will need to be controlled by user interaction and power constraints for stability
- The collector's [1] wheel's shall be connected by the raspberry pi [3]
  - Rationale: The wheels will need to be controlled by user interaction to be directed by instructions
- The rotation of the motors [2] shall control the movement of the collector without any manual help.
   - Rationale : This will ensure that the movement maintains controllable while also ensuring the requirements to achieving a remote controlled tennis ball collector.   
- The DC motors [2] shall recieve it's directions from the RC controller system.
  - Rationale : This will ensure motors operate via user input to limit unexpected behavior
- Shall continuely control the movement of the tennis ball collector [1].
  - Rationale : Control should be a constant factor within motor operation for reliable motions

  
Other motor subsystem specifications defined in the Conceptual Design were deemed irrational.
- The Dual Shaft Wheels shall not be connected by the Raspberry Pi
  - Rationale : Resulting effect would not outweigh the additional resources and calculations needed to ensure that it would not negatively impact the functionality of the collector.
- Shall operate continuously at rated power and rated voltage without exceeding temperature limits, as specified by IEC 60034-1
  -Rationale: The reference of this standard no longer applies as there is no means of measuring "temperature limits"; mention of the standard wasn also removed in the Ethical, Professional, and Standards Considerations of the Conceptual Design.
- Shall have a data rates based on the frequency: 2.4 GHz up to 250 kbps and 915 MHz, 40 kbps
  - This constraint on data rates does not apply to the motor subsystem.



## Overview of Proposed Solution

The proposed solution for this Motor subsystem is to provide user controlled motors on the pre-existing wheels of the tennis ball collector. 3-4 motors, GEARMOTOR 50 RPM 12V METAL [2], will be controlled by 2 motor drivers, Sabertooth dual 12A motor driver (Sabertooth 2x12) [4] (one for the collector's [1] front small wheels, and the other for the back larger wheels). Connectivity outside the motor subsystem will be through the motor drivers [4] that will satisfy specifications including connecting DC motors [2] to power supply and raspberry pi [3], connecting tennis ball collector's wheels to the Raspberry Pi, controlling movement and rotation of the collector [1] without any manual help, and recieving inputs of direction from RC subsystem.
There are two possible solution only differing by motor driver version. The first is a more desirable use of a simplistic R/C driver, Sabertooth dual 12A motor driver for R/C [4]. The other is a more generic version of the same motor driver type, the Sabertooth dual 12A motor driver [5]

## Interface with Other Subsystems


The Motor subsystem has few inputs and outputs as one of the technical applications of the design. Inputs include the Power Supply System subsystem's supply voltage using a compatible battery and the RC subsystem's input user instructions recieved from the raspberry pi microprocessor [3]. All are inputs to the motor drivers which in turn, output's control to the motors [2] for movement in the tennis ball collector [1]. 


## Buildable Schematic 

### Solution 1
RC subsystem will recieve user input that will wirelessly connect to the raspberry pi microprocessor [3]. To ensure the signals are properly shifted to the required voltage levels, the level shifter [5] will be a median between the desired motor driver [4] and the raspberry pi. The motor driver will recieve input from the raspberry pi and using power from the power supply subsystem's battery the motor driver will power on its corresponding motors, providing non-manual movement to the collector [1]. For the Sabertooth Driver, S1 is the forwards/backwards channel of control and S2 is the left/right channel. The unnamed cord is the flip channel and it has optional usage that will depend on the coding of the raspberry pi.

![motorsubsystem-schematic-36](https://github.com/user-attachments/assets/4be2daa4-ec76-4ef0-b437-3f1ab952ba29)

### Solution 2 
If I am unable to purchase the more cost efficient option of motor driver, I will use the more general Sabertooth 2x12 motor driver [6]. Though not mentioned on the schematic, this will also include the LS component shown in the first solution.
![S2motorsubsystem-schematic-](https://github.com/user-attachments/assets/4e5bcad6-35ae-4cb9-a393-64119f4c6344)


## Printed Circuit Board Layout

### Level Shifter : SparkFun Logic Level Converter - Bi-Directional 
![image](https://github.com/user-attachments/assets/40933d9c-2bdf-45d3-9f46-6e6a17af1974)

### Motor Driver : Sabertooth dual 12A motor driver for R/C
![Sabertooth-2X10-RC-diagram](https://github.com/user-attachments/assets/9cd1c8c9-8df3-47ef-ab18-a7affbf522ab)


### Motor Driver : Sabertooth dual 12A motor driver
![image](https://github.com/user-attachments/assets/5ac08e86-255c-49be-a490-a7906887921e)

### Motor : GearMotor 50 RPM 12V METAL
![image](https://github.com/user-attachments/assets/64201d8d-ab02-4b5a-8bfb-3c196a20a89c)

## BOM

$5.99 for jumper wires

| Manufacterer | Product Number | Distributor | Distributor Part Number | Quantity | Price | Schematic Label | Purchase Link |
| ---------- | --------- | --------- | --------- | --------- | --------- | --------- | --------- | 
| Dimension Engineering | SABERTOOTH 2X12 R/C | RobotShop |  RB-Dim-43 | 2 | 64.95 |  | [link](https://www.robotshop.com/products/sabertooth-dual-12a-regenerative-motor-driver) |
| Dimension Engineering | SABERTOOTH 2X12 | DFRobot |  DRI0003 | 2 | 64.95 |  | [link](https://www.dfrobot.com/product-304.html) |
| DFRobot | FIT0492-A | DigiKey |  FIT0492-A | 4 | 11.90 | | [link](https://www.dfrobot.com/product-304.html) |
| Total Cost | N/A | N/A | N/A | N/A | 85 | N/A |

## Analysis

Operations will be carried out from inputs and safety precautions of the RC subsystem and Power Supply subsystem  the raspberry pi [3] and 2 Sabertooth dual 12A motor driver[4] (each handling up to 2 DC motors[2]). The soluion will consist of 3-4 DC motor, GEARMOTOR 50 RPM 12V METAL [2], capable of operating a weight load similar to the 52 lb Playmate Ball Mower 2.0 [7]. To ensure control of the collector without manual help we must consider how to effectively add the motors. There is large set of wheels in the back, potentially within the metal barrel that feeds the tennis balls into the collection basket. If the wheels are connected by an axel the motor shaft can be directly connected to it by direct coupling. All other wheel connections, if needed, will be stablized by a 3D printed altered design of a motor casing [8] tailored to the dimensions of the collector's caster brackets and motors. 



## References

All sources that have contributed to the detailed design and are not considered common knowledge should be duly cited, incorporating multiple references.
https://dhtennis.net/product/the-playmate-ball-mower-2-0/ (51 lb model)
