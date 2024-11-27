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


## Interface with Other Subsystems


The Motor subsystem has few inputs and outputs as one of the technical applications of the design. Inputs include the Power Supply System subsystem's supply voltage using a compatible battery and the RC subsystem's input user instructions recieved from the raspberry pi microprocessor [3]. All are inputs to the motor driver [4] which in turn, output's control to the motors [2] for movement in the tennis ball collector [1]. 


## Buildable Schematic 

RC Subsystem will recieve user input that will wirelessny connect to the raspberry pi microprocessor [3]. Through wiring, the motor driver will recieve input from the raspberry pi and using power from the power supply subsystem's battery the motor driver [4] will power on its corresponding motors, providing non-manual movement to the collector [1].

![motorsubsystem-schematic-36](https://github.com/user-attachments/assets/9750c082-0021-476d-ac5b-0e0db246b397)

## BOM

A complete list of all components needed for the design must be given with the cost of each component and the total cost of the subsystem. The BOM should be a markdown table. Make sure to to provide the manufacteror, part number, distributor, distributor part number, quantity, and price. Also provide a url where the product can be purchased from. If the componenet is refernced on your schematic make sure to include the component name.

Provide a comprehensive list of all necessary components along with their prices and the total cost of the subsystem. This information should be presented in a tabular format, complete with the manufacturer, part number, distributor, distributor part number, quantity, price, and purchasing website URL. If the component is included in your schematic diagram, ensure inclusion of the component name on the BOM (i.e R1, C45, U4).

$5.99 for jumper wires
$1.78 

| Manufacteror | Product Number | Distributor | Distributor Part Number | Quantity | Price | Purchase Link |
| ---------- | --------- | --------- | --------- | --------- | --------- | --------- | 
| Dimension Engineering | 940-000117 | Logitech G |  940-000117 | 2 | 40 | [link](https://www.logitechg.com/en-us/products/gamepads/f710-wireless-gamepad.940-000117.html) |
| Raspberry Pi Holdings Ltd | 4292 | Raspberry Pi | 4292 | 1 | 45 | [link](https://www.adafruit.com/product/4292?src=raspberrypi) |
| Total Cost | N/A | N/A | N/A | N/A | 85 | N/A |

## Analysis

Operations will be carried out from inputs and safety precautions of the RC subsystem and Power Supply subsystem  the raspberry pi [3] and 2 Sabertooth dual 12A motor driver[4] (each handling up to 2 DC motors[2]). The soluion will consist of 3-4 DC motor, GEARMOTOR 50 RPM 12V METAL [2], capable of operating a weight load similar to the 52 lb Playmate Ball Mower 2.0 [5]. To ensure control of the collector without manual help we must consider how to effectively add the motors. There is large set of wheels in the back, potentially within the metal barrel that feeds the tennis balls into the collection basket. If the wheels are connected by an axel the motor shaft can be directly connected to it by direct coupling. All other wheel connections, if needed, will be stablized by a 3D printed altered design of a motor casing [6] tailored to the dimensions of the collector's caster brackets and motors. 



## References

All sources that have contributed to the detailed design and are not considered common knowledge should be duly cited, incorporating multiple references.
https://dhtennis.net/product/the-playmate-ball-mower-2-0/ (51 lb model)
