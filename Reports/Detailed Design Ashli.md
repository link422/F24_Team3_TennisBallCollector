# Detailed Design

## Function of the Subsystem

The objective of the Motor Subsystem is to help navigate the Tennis Ball Collector [1] installed on the wheels using DC motors by increasing the mobility of already established wheels on the Tennis Ball Collector [1]. Several featured functions will be included in the composition of this subsection including:
  1. Connecting DC motors [2] to power supply and Raspberry Pi [3]
  2. Connecting Tennis Ball Collector's Dual Shaft Wheels to the Raspberry Pi
  3. Controlling movement and rotation of the collector without any manual help
  4. Recieving inputs of direction from RC controller system

## Specifications and Constraints
- The DC motors [2] shall be connected to the power supply and Raspberry Pi.
  - Rationale: The motors will need to be controlled by user interaction and power constraints for stability
- The collector's dual shaft wheels shall be connected by the Raspberry Pi
  - Rationale: The wheels will need to be controlled by user interaction to be directed by instructions
- The rotation of the motors shall control the movement of the collector without any manual help.
   - Rational : This will ensure that the movement maintains controllable while also ensuring the requirements to achieving a remote controlled tennis ball collector.   
- The DC motors shall recieve it's directions from the RC controller system.
  - Rationale : This will ensure motors operate via user input to limit unexpected behavior
- Shall continuely control the movement of the tennis ball collector.
  - Rationale : Control should be a constant factor within motor operation for reliable motions 


## Overview of Proposed Solution

The proposed solution for this Motor subsystem is to provide user controlled motors on the pre-existing wheels of the Tennis Ball Collector. Operations will be carried out from inputs and safety precautions of the RC Subsystem and Power Supply Subsystem established by the Sabertooth dual 12A motor driver [6] and the . The soluion will consist of 3-4 DC motor, GEARMOTOR 50 RPM 12V METAL [4], capable of operating an approximately 52 lb collector (inferred using the documented weight of a referenced website [5]). To ensure control of the collector without manual help we must consider how to effectively add motors that will be stable within the frame of the collector. There is large set of wheels in the back, potentially within the metal barrel that feeds the tennis balls into the collection basket. If the wheels are connected by an axel the motor shaft can be directly connected to it by direct coupling; all other wheel connections will be stablized by a 3D printed altered design of a motor casing [7] tailored to the dimensions of the collector's caster brackets and motors. 


## Interface with Other Subsystems

Provide detailed information about the inputs, outputs, and data transferred to other subsystems. Ensure specificity and thoroughness, clarifying the method of communication and the nature of the data transmitted.

Power system will supply an input of voltage for the motor drivers to activate and the RC controller subsystem 


## Buildable Schematic 


The schematic should be relevant to the design and provide ample details necessary for constructing the model. It must be comprehensive so that someone, with no prior knowledge of the design, can easily understand it. Each related component's value and measurement should be clearly mentioned.


## BOM

A complete list of all components needed for the design must be given with the cost of each component and the total cost of the subsystem. The BOM should be a markdown table. Make sure to to provide the manufacteror, part number, distributor, distributor part number, quantity, and price. Also provide a url where the product can be purchased from. If the componenet is refernced on your schematic make sure to include the component name.

Provide a comprehensive list of all necessary components along with their prices and the total cost of the subsystem. This information should be presented in a tabular format, complete with the manufacturer, part number, distributor, distributor part number, quantity, price, and purchasing website URL. If the component is included in your schematic diagram, ensure inclusion of the component name on the BOM (i.e R1, C45, U4).

## Analysis

Deliver a full and relevant analysis of the design demonstrating that it should meet the constraints and accomplish the intended function. This analysis should be comprehensive and well articulated for persuasiveness.

## References

All sources that have contributed to the detailed design and are not considered common knowledge should be duly cited, incorporating multiple references.
https://dhtennis.net/product/the-playmate-ball-mower-2-0/ (51 lb model)
