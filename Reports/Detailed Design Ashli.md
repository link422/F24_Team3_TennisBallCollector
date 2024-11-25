# Detailed Design

## Function of the Subsystem

The objective of the Motor Subsystem is to help navigate the Tennis Ball Collector [1] installed on the wheels using DC motors by increasing the mobility of already established wheels on the Tennis Ball Collector [1]. Several featured functions will be included in the composition of this subsection including:
  1. Connecting DC motors [2] to power supply and Raspberry Pi
  2. Connecting Dual Shaft Wheels [3] shall be connected by the Raspberry Pi
  3. Controlling movement and rotation of the collector without any manual help
  4. Recieving inputs of direction from RC controller system

## Specifications and Constraints
- The DC motors [2] shall be connected to the power supply and Raspberry Pi.
  - Rationale: The motors will need to be controlled by user interaction and power constraints for stability
- The Dual Shaft Wheels [3] shall be connected by the Raspberry Pi
  - Rationale: The wheels will need to be controlled by user interaction
- The rotation of the motors shall control the movement of the collector without any manual help.
   - Rational : This will ensure that the movement maintains controllable while also ensuring the requirements to achieving a remote controlled tennis ball collector.   
- The DC motors shall recieve it's directions from the RC controller system.
  - Rationale : This will ensure motors operate via user input to limit unexpected behavior
- Shall continuely control the movement of the tennis ball collector.
  - Rationale : Control should be a constant factor within motor operation for reliable motions 


## Overview of Proposed Solution

The proposed solution for this Motor subsystem  is to provide user controlled motors on the pre-existing wheels of the Tennis Ball Collector that is operated by the RC subsystem and power supply subsystem. The subsystem will consist of 3-4 DC motor capable of operating an approximately 52 lb collector strictly controlled by the inputs and safety precautions of the power supply and RC controller subsystems. To ensure control of the collector without manual help we must consider how to effectively add motors that will be stable within the frame of the collector. There is large set of wheels in the back, potentially within the metal barrel that feeds the tennis balls into the collection basket. If the wheels are connected by an axel the motor shaft can be directly connected to it by direct coupling; otherwise we can use a belt and pulley system to include the motor into the movement of the wheel. Towards the front of the collector there is very limited space between the sets of 2 wheels on each side, therefore a belt and pulley system would be more effective execution to connect the motor shaft to the wheels. A schematic on the potential method of connecting the power supply subsystem and raspberry pi [4] can be highlighted with the use of a dual H-bridge motor drive controller board, 

Describe the solution and how it will fulfill the specifications and constraints of this subsystem.


## Interface with Other Subsystems

Provide detailed information about the inputs, outputs, and data transferred to other subsystems. Ensure specificity and thoroughness, clarifying the method of communication and the nature of the data transmitted.


## 3D Model of Custom Mechanical Components

Should there be mechanical elements, display diverse views of the necessary 3D models within the document. Ensure the image's readability and appropriate scaling. Offer explanations as required.


## Buildable Schematic 

Integrate a buildable electrical schematic directly into the document. If the diagram is unreadable or improperly scaled, the supervisor will deny approval. Divide the diagram into sections if the text and components seem too small.

The schematic should be relevant to the design and provide ample details necessary for constructing the model. It must be comprehensive so that someone, with no prior knowledge of the design, can easily understand it. Each related component's value and measurement should be clearly mentioned.


## Printed Circuit Board Layout

Include a manufacturable printed circuit board layout.


## Operational Flowchart

For sections including a software component, produce a chart that demonstrates the decision-making process of the microcontroller. It should provide an overview of the device's function without exhaustive detail.


## BOM

A complete list of all components needed for the design must be given with the cost of each component and the total cost of the subsystem. The BOM should be a markdown table. Make sure to to provide the manufacteror, part number, distributor, distributor part number, quantity, and price. Also provide a url where the product can be purchased from. If the componenet is refernced on your schematic make sure to include the component name.

Provide a comprehensive list of all necessary components along with their prices and the total cost of the subsystem. This information should be presented in a tabular format, complete with the manufacturer, part number, distributor, distributor part number, quantity, price, and purchasing website URL. If the component is included in your schematic diagram, ensure inclusion of the component name on the BOM (i.e R1, C45, U4).

## Analysis

Deliver a full and relevant analysis of the design demonstrating that it should meet the constraints and accomplish the intended function. This analysis should be comprehensive and well articulated for persuasiveness.

## References

All sources that have contributed to the detailed design and are not considered common knowledge should be duly cited, incorporating multiple references.
