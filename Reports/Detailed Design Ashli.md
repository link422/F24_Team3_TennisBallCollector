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
- The DC motors shall be tested as applicable using procedures outline in IEEE Standard 112 [8]. 
  - Rationale : This IEEE standard defines methods for testing and evaluating motor efficiency, torque, power, and speed under controlled conditions. This will be helpful in ensuring the solution for the subsystem is satisfactory in execution.
  
Other motor subsystem specifications defined in the Conceptual Design were deemed irrational.
- The Dual Shaft Wheels shall not be connected by the Raspberry Pi
  - Rationale : Resulting effect would not outweigh the additional resources and calculations needed to ensure that it would not negatively impact the functionality of the collector.
- Shall operate continuously at rated power and rated voltage without exceeding temperature limits, as specified by IEC 60034-1
  - Rationale: The reference of this standard no longer applies as there is no means of measuring "temperature limits"; mention of the standard wasn also removed in the Ethical, Professional, and Standards Considerations of the Conceptual Design.
- Shall have a data rates based on the frequency: 2.4 GHz up to 250 kbps and 915 MHz, 40 kbps
  - This constraint on data rates does not apply to the motor subsystem.



## Overview of Proposed Solution

The proposed solution for this Motor subsystem is to provide user controlled motors on the pre-existing wheels of the tennis ball collector. 2 motors, 8BRINGSMART 12V 12rpm DC Worm Gear Motor 70kg.cm High Torque Self-Locking Reversed Mini Turbine Geared Motor for DIY Robot Rotating Table Door Lock Curtain Machine (B07F8Y36PD) [2], will be controlled by a motor driver, Sabertooth dual 12A motor driver (Sabertooth 2x12) [4]; targeting control in the back larger wheels for simplicity as they drive most of the movement. Connectivity outside the motor subsystem will be through the motor driver [4] that will satisfy specifications including connecting DC motors [2] to power supply and raspberry pi [3], connecting tennis ball collector's wheels to the Raspberry Pi, controlling movement and rotation of the collector [1] without any manual help, and recieving inputs of direction from RC subsystem.

The Sabertooth dual 12A motor driver [4] will be configured to operate using the schematic featured in the Buildable Schematic section and connection of motors using pulley and belt system. IEEE Standard 112 [8] testing will commence once all required motor components have been received and the necessary equipment has been prepared and verified for functionality.

## Interface with Other Subsystems


The Motor subsystem has few inputs and outputs as one of the technical applications of the design. Inputs include the Power Supply System subsystem's supply voltage using a compatible battery and the RC subsystem's input user instructions recieved from the raspberry pi microprocessor [3]. All are inputs to the motor drivers which in turn, output's control to the motors [2] for movement in the tennis ball collector [1]. 


## Buildable Schematic 

### Solution

RC subsystem will recieve user input that will wirelessly connect to the raspberry pi microprocessor [3]. To ensure the signals are properly shifted to the required voltage levels, the level shifter [5] will be a median between the motor driver [4] and the raspberry pi. The motor driver will recieve input from the raspberry pi and using power from the power supply subsystem's battery the motor driver will power on its corresponding motors, providing non-manual movement to the collector [1]. 


![Capstone1-5](https://github.com/user-attachments/assets/30f928da-f8ba-418e-b377-814de5fbdece)






## Printed Circuit Board Layout

### Level Shifter : SparkFun Logic Level Converter - Bi-Directional 
![image](https://github.com/user-attachments/assets/40933d9c-2bdf-45d3-9f46-6e6a17af1974)

### Motor Driver : Sabertooth dual 12A motor driver
![image](https://github.com/user-attachments/assets/5ac08e86-255c-49be-a490-a7906887921e)

### Motor :  BRINGSMART 12V 12rpm DC Worm Gear Motor 
![image](https://github.com/user-attachments/assets/7a826df7-fbd1-4694-b574-afbe7d909ffe)


Installation shown in Analysis section

## BOM



| Component | Manufacterer | Product Number | Distributor | Distributor Part Number | Quantity | Price | Schematic Label | Purchase Link |
| ---------- | ---------- | --------- | --------- | --------- | --------- | --------- | --------- | --------- | 
| Sabertooth dual 12A motor driver | Dimension Engineering | SABERTOOTH 2X12 | DFRobot |  DRI0003 | 1 | 79.00 | D2x12 | [link](https://www.dfrobot.com/product-304.html) |
| BRINGSMART 12V 12rpm DC Worm Gear Motor | Hugwig Company | A58SW31ZY | Amazon | B07F8Y36PD | 2 | 26.22 | M50 | [link](https://www.amazon.com/BRINGSMART-70kg-cm-Self-locking-Reversed-Rotating/dp/B07F8Y36PD?dib=eyJ2IjoiMSJ9.lRc1JXl09pYwCJYedlOy6vOR1eXRAe_QP4rlXNh62gKUX5VoMbQpF0jbiUQE5naXb0iEwiCXEegvldtuZ5cWV0Olz9cXPuhkjCPJlxFVhfpuzsZD2fePkaBsWzDykprzVzV2GKjkRYgc5K2yF3SsqRBp86F8KqkkyxoB1PdLqHYY-C4tH7DQy08ylL-GlJkLKc91FgDQpZjrcADe0Ez2ax7uYcwEhz7nubUgzjc-isrJYjnwCCpeLVoPmjF5ucqvi0RINV35Sp99jmJGaUDvSMOpV0pJpedBnO0lv3-55V8JxE7Pmc8IRq1fWWbmFHPIIN9mlE10XA8eqtrDaYS-F_qXoQ1KyMU2Y5kHgCzhdRhjmiOj3DGrcKXks6xk2iXGmGqwgbUZmYBEvUBra3_EpfQC2XeXJiRz3tVcJV5g0imSdGvIC7LIAEM5dnO6jTIq.HsAywLdAWmite_N27a7INBedNzcalUtHO4v64B7J7i4&dib_tag=se&keywords=12v%2Bdc%2Bmotor%2Bhigh%2Btorque&qid=1738259387&sr=8-5&utm_source=chatgpt.com&th=1) |
| SparkFun Logic Level Converter - Bi-Directional | SparkFun Electronics | BOB-12009 | DigiKey |  1568-1209-ND | 1 | 3.50 | LS | [link](https://www.digikey.com/en/products/detail/sparkfun-electronics/BOB-12009/5673795?s=N4IgTCBcDaIIwFYBsAOAtHMAGAnGgcgCKDQBCALoC%2BQA) |
| 120pcs 20 cm Breadboard Jumper Wires Dupont Cable Assorted Kit| EDGELEC | ED-DP_L20_Mix_120pcs | Amazon | B07GD2BWPY | 1 | 6.98 | N/A | [link](https://www.amazon.com/EDGELEC-Breadboard-Optional-Assorted-Multicolored/dp/B07GD2BWPY?crid=3DGC320SX81Z2&dib=eyJ2IjoiMSJ9.APYjLeLR3cSKMa-3o77o4cYI1olfvBTpJBIBWrLqSaoqeqjKWlnOg1F7dI1ZHbmBbHXPnl9A-zfQjw7P80ggVPZr7fM9E61QH7DOhZ_nWHnJ6KQoWLD4hxEjd2VbMnSznD3cFZ049cNPHb-py6kYwTtqcH3GbSuH7vg1aoHE7ebusdWXj1c0YVqajUVuVcP0oktnHN8Mv2MMez3cyrXOVYzVh3j4K00H6j53cig7Ex4.4b2v71rjNo84MGdm-KeQ8BLrgu2huoe5dUA729xcNXA&dib_tag=se&keywords=jump%2Bwires%2Bmale%2Bto%2Bmale%2C%2Bmale%2Bto%2Bfemale%2C%2Bfemale%2Bto%2Bfemale&qid=1732744550&sprefix=jump%2Bwires%2Bmale%2Bto%2Bmale%2C%2Bmale%2Bto%2Bfemale%2C%2Bfemale%2Bto%2Bfemale%2Caps%2C147&sr=8-1&th=1) |
| Motor Pulley | --- | --- | Automation Direct | 2 |  | | N/A | [link](https://www.automationdirect.com/adc/shopping/catalog/power_transmission_(mechanical)/timing_belts,_timing_pulleys_-a-_tapered_bushings) |
| Gearbox | --- | --- | Automation Direct | 2 |  | | N/A | [link](https://www.automationdirect.com/adc/shopping/catalog/power_transmission_(mechanical)/timing_belts,_timing_pulleys_-a-_tapered_bushings) |
| Pulley Belt | --- | --- | Automation Direct | 1 |  | | N/A | [link](https://www.automationdirect.com/adc/shopping/catalog/power_transmission_(mechanical)/timing_belts,_timing_pulleys_-a-_tapered_bushings) |
| Total Cost | N/A | N/A | N/A | N/A | N/A | $234.48 | N/A |

## Analysis
------------figure out what spur to use and continue proofreading
Operations will be carried out from inputs and safety precautions of the RC subsystem and Power Supply subsystem  the raspberry pi [3] and 2 Sabertooth dual 12A motor driver[4] (each handling up to 2 DC motors[2]). The soluion will consist of 2 DC gearmotors, BRINGSMART 12V 12rpm DC Worm Gear Motor [2], capable of operating a weight load similar to the 44 lb Playmate Ball Mower 2.0 [7]. This design choice was established considering torque, weight distribution, and speed. The use of 4 motors will handle the load of 44 lb by attaching to it's drive wheels (2) in the back. One of our competitors, Tennibot travels at 1.4 mph (0.626 m/s); preferably we would like to get close to that speed.

Motor Specs:
Rated Torque = 70 kg.cm = 6.97 Nm
Rated voltage = 12V
  Rationale : Within limitations of 12V Battery supplied via Power Supply subsystem; high torque to ensure it can handle load without stalling
Rated speed = 9 RPM
No Load Current = 350mA
Rated Current = 1.6 A
Reducer ratio = 1:670

Analysis: 
(Diameter * RPM)/ 60
  Motor RPM = 9 RPM/670 = 0.01343 RPM
  V(rear) = (1.12 m * 0.01343 RPM)/ 60 = 0.000251 m/s
  We will need another stage of gear to increase it--we can also use this as a means to connection motors to the wheels.
  Rationale : Speed will be dominated by the rear ($\approx$ 0.501 (0.224 m/s * 2.237)), but it still does not meet the desired speed. 

Considering a spur gear.
  Rationale:
    - increases speed by having the wheel gear smaller than the motor gear
    - cost-effective, simple, and efficient for direct power transmission

Rated torque = 70 kg.cm =  N * 4 motors = 17.652 Nm 


Rear Wheels (14'' diameter, 1.12 m) Analysis:
Tennis Ball collector weight: 44lb, 20.87 kg 
Total Load per motor: 20.87 * 9.81/4 = 51.2 N
Rear Torque: Radius = 0.1778 m ; Torque = Weight per motor * radius
    =>  51.2 N * 0.1778 m = 9.1 Nm;

Torque Rationale : Desired Rear (9.1 Nm) Motor Torque is in reasonable range of the rated torque of 45 kg.cm (17.652 Nm)

To ensure control of the collector without manual help we must consider how to effectively add the motors. There is large set of wheels in the back, potentially within the metal barrel that feeds the tennis balls into the collection basket. If the wheels are connected by an axel the motor-wheel connection


will be using a pulley and belt system that consist of 2 motor pulleys (6mm bore size) and 1 wheel pulley (unknown bore size) on each 14 inch drive wheel. The materials to use for this system will be selected from AutomationDirect [10] (they all have fairly quick shipping). This is to be confirmed after more measurments are taken from the tennis ball collector. In the diagram below, I show how the framing inside the drum (khaki circle) will be, with the pulley and belt system highlighted in white and mechanical connections noted in purple. 


![Rest of Motor Subsystem + Other Subsystems](https://github.com/user-attachments/assets/5605b516-1fd3-41b4-aa7a-a15c189de39e)




## References
[1] "BALL MOWER." PLAYMATE Tennis, 5 June 2023, www.playmatetennis.com/ball-mower/

[2] “BRINGSMART 12V 12rpm DC Worm Gear Motor 70kg.cm High Torque Self-Locking Reversed Mini Turbine Geared Motor for DIY Robot Rotating Table Door Lock Curtain Machine (12V 12rpm)” amazon.com, https://www.amazon.com/BRINGSMART-70kg-cm-Self-locking-Reversed-Rotating/dp/B07F8Y36PD?dib=eyJ2IjoiMSJ9.lRc1JXl09pYwCJYedlOy6vOR1eXRAe_QP4rlXNh62gKUX5VoMbQpF0jbiUQE5naXb0iEwiCXEegvldtuZ5cWV0Olz9cXPuhkjCPJlxFVhfpuzsZD2fePkaBsWzDykprzVzV2GKjkRYgc5K2yF3SsqRBp86F8KqkkyxoB1PdLqHYY-C4tH7DQy08ylL-GlJkLKc91FgDQpZjrcADe0Ez2ax7uYcwEhz7nubUgzjc-isrJYjnwCCpeLVoPmjF5ucqvi0RINV35Sp99jmJGaUDvSMOpV0pJpedBnO0lv3-55V8JxE7Pmc8IRq1fWWbmFHPIIN9mlE10XA8eqtrDaYS-F_qXoQ1KyMU2Y5kHgCzhdRhjmiOj3DGrcKXks6xk2iXGmGqwgbUZmYBEvUBra3_EpfQC2XeXJiRz3tVcJV5g0imSdGvIC7LIAEM5dnO6jTIq.HsAywLdAWmite_N27a7INBedNzcalUtHO4v64B7J7i4&dib_tag=se&keywords=12v%2Bdc%2Bmotor%2Bhigh%2Btorque&qid=1738259387&sr=8-5&utm_source=chatgpt.com&th=1

[3] Ltd, Raspberry P. "Buy a Raspberry Pi 4 Model B – Raspberry Pi." Raspberry Pi, https://www.raspberrypi.com/products/raspberry-pi-4-model-b/

[4] "Sabertooth 2X12 Regenerative Dual Motor Driver." Dimension Engineering, Power Electronics, Sensors, www.dimensionengineering.com/products/sabertooth2x12/

[5] "Bi-Directional Logic Level Converter Hookup Guide." Learn at SparkFun Electronics - SparkFun Learn, https://learn.sparkfun.com/tutorials/bi-directional-logic-level-converter-hookup-guide/all/

[6] "Ball Mower Caster Bracket Kit | Playmate Tennis Court Parts & Accessories | DH Distribution." DH Distribution, https://dhtennis.net/product/mower-caster-bracket-kit/

[7] "Playmate Ball Mower | Playmate Tennis Court Products | DH Distribution." DH Distribution, 9 Oct. 2024, https://dhtennis.net/product/the-playmate-ball-mower-2-0/

[8] Institute of Electrical and Electronics Engineers. IEEE Standard Test Procedure for Polyphase Induction Motors and Generators. Iowa State University, 1997.

[9] "Ball Mower Replacement Casters | Playmate Tennis Court Parts & Accessories | DH Distribution." DH Distribution, 
https://dhtennis.net/product/replacement-caster-for-ball-mower/

[10] Timing Belts, Timing Pulleys and Tapered Bushings | Power Transmission (Mechanical) | Products | AutomationDirect, https://www.automationdirect.com/adc/shopping/catalog/power_transmission_(mechanical)/timing_belts,_timing_pulleys_-a-_tapered_bushings

