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
- The DC motors shall be tested as applicable using procedures outline in IEEE Standard 112 [9]. 
  - Rationale : This IEEE standard defines methods for testing and evaluating motor efficiency, torque, power, and speed under controlled conditions. This will be helpful in ensuring the solution for the subsystem is satisfactory in execution.
  
Other motor subsystem specifications defined in the Conceptual Design were deemed irrational.
- The Dual Shaft Wheels shall not be connected by the Raspberry Pi
  - Rationale : Resulting effect would not outweigh the additional resources and calculations needed to ensure that it would not negatively impact the functionality of the collector.
- Shall operate continuously at rated power and rated voltage without exceeding temperature limits, as specified by IEC 60034-1
  -Rationale: The reference of this standard no longer applies as there is no means of measuring "temperature limits"; mention of the standard wasn also removed in the Ethical, Professional, and Standards Considerations of the Conceptual Design.
- Shall have a data rates based on the frequency: 2.4 GHz up to 250 kbps and 915 MHz, 40 kbps
  - This constraint on data rates does not apply to the motor subsystem.



## Overview of Proposed Solution

The proposed solution for this Motor subsystem is to provide user controlled motors on the pre-existing wheels of the tennis ball collector. 4 motors, 83 RPM Metal DC motor (GB37Y3530-12V-83R) [2], will be controlled by 2 motor drivers, Sabertooth dual 12A motor driver (Sabertooth 2x12) [4] (one for the collector's [1] front small wheels, and the other for the back larger wheels). Connectivity outside the motor subsystem will be through the motor drivers [4] that will satisfy specifications including connecting DC motors [2] to power supply and raspberry pi [3], connecting tennis ball collector's wheels to the Raspberry Pi, controlling movement and rotation of the collector [1] without any manual help, and recieving inputs of direction from RC subsystem.

The Sabertooth dual 12A motor driver [4] will be configured to operate using the schematic featured in the Buildable Schematic section and connection of motors using a casing model similar to the 775 Motor Casing [8]. These will be attached to the Mower Caster Bracket [6] for the front wheels and inside of connector drum for the back wheel motors. IEEE Standard 112 [9] testing will commence once all required motor components have been received and the necessary equipment has been prepared and verified for functionality.

## Interface with Other Subsystems


The Motor subsystem has few inputs and outputs as one of the technical applications of the design. Inputs include the Power Supply System subsystem's supply voltage using a compatible battery and the RC subsystem's input user instructions recieved from the raspberry pi microprocessor [3]. All are inputs to the motor drivers which in turn, output's control to the motors [2] for movement in the tennis ball collector [1]. 


## Buildable Schematic 

### Solution
I will use the Sabertooth 2x12 motor driver [4] as the motor controller of the DC motor supplying movement to the existing collector wheels. The schematic is shown below. 

![S2motorsubsystem-schematic-](https://github.com/user-attachments/assets/ba2a870e-6abd-4201-904d-1968bab00d49)





## Printed Circuit Board Layout

### Level Shifter : SparkFun Logic Level Converter - Bi-Directional 
![image](https://github.com/user-attachments/assets/40933d9c-2bdf-45d3-9f46-6e6a17af1974)

### Motor Driver : Sabertooth dual 12A motor driver for R/C
![Sabertooth-2X10-RC-diagram](https://github.com/user-attachments/assets/9cd1c8c9-8df3-47ef-ab18-a7affbf522ab)


### Motor Driver : Sabertooth dual 12A motor driver
![image](https://github.com/user-attachments/assets/5ac08e86-255c-49be-a490-a7906887921e)

### Motor :  83 RPM, 12V Metal DC motor Geared Motor 
![FIT0185_Dimension](https://github.com/user-attachments/assets/4f710ae7-9948-41e2-99e4-d2a06a53a3c0)

Installation shown in Analysis section

## BOM



| Component | Manufacterer | Product Number | Distributor | Distributor Part Number | Quantity | Price | Schematic Label | Purchase Link |
| ---------- | ---------- | --------- | --------- | --------- | --------- | --------- | --------- | --------- | 
| Sabertooth dual 12A motor driver | Dimension Engineering | SABERTOOTH 2X12 | DFRobot |  DRI0003 | 2 | 79.00 | D2x12 | [link](https://www.dfrobot.com/product-304.html) |
| 83 RPM Metal DC motor | DFRobot | FIT0185 | DFRobot | FIT0185 | 4 | 16.50 | M50/S1A-B/S2A-B | [link](https://www.dfrobot.com/product-633.html) |
| SparkFun Logic Level Converter - Bi-Directional | SparkFun Electronics | BOB-12009 | DigiKey |  1568-1209-ND | 1 | 3.50 | LS | [link](https://www.digikey.com/en/products/detail/sparkfun-electronics/BOB-12009/5673795?s=N4IgTCBcDaIIwFYBsAOAtHMAGAnGgcgCKDQBCALoC%2BQA) |
| 120pcs 20 cm Breadboard Jumper Wires Dupont Cable Assorted Kit| EDGELEC | ED-DP_L20_Mix_120pcs | Amazon | B07GD2BWPY | 1 | 6.98 | N/A | [link](https://www.amazon.com/EDGELEC-Breadboard-Optional-Assorted-Multicolored/dp/B07GD2BWPY?crid=3DGC320SX81Z2&dib=eyJ2IjoiMSJ9.APYjLeLR3cSKMa-3o77o4cYI1olfvBTpJBIBWrLqSaoqeqjKWlnOg1F7dI1ZHbmBbHXPnl9A-zfQjw7P80ggVPZr7fM9E61QH7DOhZ_nWHnJ6KQoWLD4hxEjd2VbMnSznD3cFZ049cNPHb-py6kYwTtqcH3GbSuH7vg1aoHE7ebusdWXj1c0YVqajUVuVcP0oktnHN8Mv2MMez3cyrXOVYzVh3j4K00H6j53cig7Ex4.4b2v71rjNo84MGdm-KeQ8BLrgu2huoe5dUA729xcNXA&dib_tag=se&keywords=jump%2Bwires%2Bmale%2Bto%2Bmale%2C%2Bmale%2Bto%2Bfemale%2C%2Bfemale%2Bto%2Bfemale&qid=1732744550&sprefix=jump%2Bwires%2Bmale%2Bto%2Bmale%2C%2Bmale%2Bto%2Bfemale%2C%2Bfemale%2Bto%2Bfemale%2Caps%2C147&sr=8-1&th=1) |
| Total Cost | N/A | N/A | N/A | N/A | N/A | $234.48 | N/A |

## Analysis

Operations will be carried out from inputs and safety precautions of the RC subsystem and Power Supply subsystem  the raspberry pi [3] and 2 Sabertooth dual 12A motor driver[4] (each handling up to 2 DC motors[2]). The soluion will consist of 4 DC motor, 83 RPM Metal DC motor (GB37Y3530-12V-83R) [2], capable of operating a weight load similar to the 52 lb Playmate Ball Mower 2.0 [7]. This design choice was established considering torque, weight distribution, and speed. The use of 4 motors will handle the load of 52 lb by attaching to it's drive wheels (2) in the back, and castor wheels in the front (4). One of our competitors, Tennibot travels at 1.4 mph; preferably we would like to get close to that speed.

Motor Specs:
Rated voltage = 12V
  Rationale : Within limitations of 11.1 V Lipo Battery supplied via Power Supply subsystem; though slightly reducing rated speed and torque.
Rated speed = 83 RPM
(Diameter * RPM)/ 60
  V(rear) = (1.12 m * 83 RPM)/ 60 = 1.55 m/s
  V(front) = (0.238 m * 83 RPM)/ 60 = 0.33 m/s
  Rationale : Speed will be dominated by the rear ($\approx$ 3.46 (1.55 * 2.237) can be infered to result in a speed greater or equal to 1.4 mph.
Rated torque = 45 kg.cm

52lb, 23.6 kg Load Distribution: $\approx$ 75% on rear wheels, $\approx$ 25% on front casters

Rear Wheels (14'' diameter, 1.12 m) Analysis:
Total Load: Weight = 23.6 kg * 0.75 = 17.7 kg 
    => Load per motor : 17.7/2 = 8.85 kg
Rear Torque: Radius = 0.178 m ; Torque = Weight per motor * radius
    => 8.85 kg * 0.178 m = 1.577 Nm; 16.1 kg.cm

Front Castor Wheels (3'' diameter, 0.238 m) Analysis: 
Total Load : 23.6 kg * 0.25 = 5.9kg 
    => Load per motor : 5.9/2 = 2.95 kg
Front Torque: Radius = 0.038 m ; Torque = (Weight per motor * radius)/ # of wheels 
    => (2.95 kg * 0.038 m) / 2 = 0.056 Nm; 0.57 kg.cm

Torque Rationale : Desired Rear (16.1 kg.cm) and Front (0.57 kg.cm) Motor Torque is in reasonable range of the rated torque of 45 kg.cm

To ensure control of the collector without manual help we must consider how to effectively add the motors. There is large set of wheels in the back, potentially within the metal barrel that feeds the tennis balls into the collection basket. If the wheels are connected by an axel the motor shaft can be directly connected to it by direct coupling. All other wheel connections, if needed, will be stablized by a 3D printed altered design of a motor casing [8] tailored to the dimensions of the collector's caster brackets and motors. 

The motors [2] will be connected through attaching a designed model similar to the 775 Motor Casing [8] to the Mower Caster Bracket [6] for the front wheels and the inside of connector drum of the tennis collector drum for the back wheels.

![Screenshot 2024-12-10 222114](https://github.com/user-attachments/assets/1528f36e-cd4a-49b6-ab87-81b47a65e6bc). 

![Screenshot 2024-12-10 224651](https://github.com/user-attachments/assets/26a69cd9-eb0b-473e-849b-aca4ff44eb49)



## References
[1] "BALL MOWER." PLAYMATE Tennis, 5 June 2023, www.playmatetennis.com/ball-mower/

[2] “12V Metal DC Geared Motor With Encoder (131:1, 83RPM, 45Kg.cm)” dfrobot.com, https://www.dfrobot.com/product-633.html

[3] Ltd, Raspberry P. "Buy a Raspberry Pi 4 Model B – Raspberry Pi." Raspberry Pi, https://www.raspberrypi.com/products/raspberry-pi-4-model-b/

[4] "Sabertooth 2X12 Regenerative Dual Motor Driver." Dimension Engineering, Power Electronics, Sensors, www.dimensionengineering.com/products/sabertooth2x12/

[5] "Bi-Directional Logic Level Converter Hookup Guide." Learn at SparkFun Electronics - SparkFun Learn, https://learn.sparkfun.com/tutorials/bi-directional-logic-level-converter-hookup-guide/all/

[6] "Ball Mower Caster Bracket Kit | Playmate Tennis Court Parts & Accessories | DH Distribution." DH Distribution, https://dhtennis.net/product/mower-caster-bracket-kit/

[7] "Playmate Ball Mower | Playmate Tennis Court Products | DH Distribution." DH Distribution, 9 Oct. 2024, https://dhtennis.net/product/the-playmate-ball-mower-2-0/

[8] "775 Motor Casing." Cults 3D, 25 June 2021, https://cults3d.com/en/3d-model/tool/775-motor-casing

[9] Institute of Electrical and Electronics Engineers. IEEE Standard Test Procedure for Polyphase Induction Motors and Generators. Iowa State University, 1997.

[10] "Ball Mower Replacement Casters | Playmate Tennis Court Parts & Accessories | DH Distribution." DH Distribution, 
https://dhtennis.net/product/replacement-caster-for-ball-mower/


