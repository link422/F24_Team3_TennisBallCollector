# Detailed Design

## Function of the Subsystem
The Sensor Subsystem’s role within the entire system is to track the amount of tennis balls entering the collection basket and send this amount to the LCD display all while the machine operates. 

## Specifications and Constraints
The Counting Sensor System section shall be expected to detect and keep track of the counted and collected balls while the entire system runs. 
- The Lidar range finder sensor [1] shall have a digital signal connected to the Raspberry Pi. 

    - Rationale: The Raspberry Pi [2] will house the software along with the power source for the Lidar Sensor 

- The Sensor shall take an accurate measurement of balls and display this data onto the LCD Display. 

    - Rationale: To allow the user to get an accurate count of how many balls have been collected 

- The Sensor shall be connected via GPIO pins on the Raspberry Pi. 

    - Rationale: This will provide immediate feedback between the sensor and the Pi 

- Shall enable seamless communication between transducers and the central microprocessor or other connected digital systems. 

    - Rationale: This will ensure accurate data processing in real time 

- Shall enable remote communication, configuration, and management of transducers over different network protocols. 

    - Rationale: allows maintenance to be done remotely without having to go to the physical device 

## Overview of Proposed Solution

Describe the solution and how it will fulfill the specifications and constraints of this subsystem.


## Interface with Other Subsystems

Provide detailed information about the inputs, outputs, and data transferred to other subsystems. Ensure specificity and thoroughness, clarifying the method of communication and the nature of the data transmitted.


## 3D Model of Custom Mechanical Components

Should there be mechanical elements, di' splay diverse views of the necessary 3D models within the document. Ensure the image's readability and appropriate scaling. Offer explanations as required.


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
