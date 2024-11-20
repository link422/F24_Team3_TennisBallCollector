# Detailed Design

This document delineates the objectives of a comprehensive system design. Upon reviewing this design, the reader should have a clear understanding of:

- How the specific subsystem integrates within the broader solution
- The constraints and specifications relevant to the subsystem
- The rationale behind each crucial design decision
- The procedure for constructing the solution


## General Requirements for the Document

The document should include:

- Explanation of the subsystem’s integration within the overall solution
- Detailed specifications and constraints specific to the subsystem
- Synopsis of the suggested solution
- Interfaces among different subsystems
- 3D models of customized mechanical elements*
- A buildable diagram*
- A Printed Circuit Board (PCB) design layout*
- An operational flowchart*
- A comprehensive Bill of Materials (BOM)
- Analysis of crucial design decisions
- Execution plan considering skill sets and time requirements
*Note: These technical documentation elements are mandatory only when relevant to the particular subsystem.


## Function of the Subsystem

The RC subsystem's primary role within the overall system is to allow the user to control the DC motors wirelessly. Being able to wirelessly communicate with the Raspberry Pi CITE THIS will give the subsystem the ability to wirlessly control the DC motors which will allow for varying speeds, turns, and an emergency stop feature. Being able to reliably control the system from a distance is important for the system as the motors could be unpredictable if there is not a strong signal controlling it. Having an emergency stop will also increase the safety of the device should anything happen. The controller will use a 2.4 GHz USB nano reciever CITE THIS to ensure a strong connection as well as provide an intuitive controller that can have its buttons programmed to do the desired task.


## Specifications and Constraints

   - The RC subsystem shall operate on a 2.4 GHz frequency to ensure reliable communication between the controller and the Raspberry Pi.
     - Rationale: The 2.4 GHz frequency is commonly used for remote control systems because it has a good balance of range and reliability.

   - The RC subsystem shall maintain reliable communication within a range of up to 30 feet.
     - Rationale: This range lets the customer operate the device without having to move around to stay within range while picking up tennis balls.

   - The RC subsystem shall include an emergency stop to imediiately turn the system off.
     - Rationale: This will ensure device safety in case of unexpected behavior.

   - The RC subsystem shall be made cost effectively using only a F710 Wireless Gamepad that comes with a 2.4 GHz reciver.
     - Rationale: This will help ensure the device is within budget and can be easily purchased.
    
   - The RC subsystem shall comply with IEEE 802.15.4 standards for low-rate wireless personal area networks (LR-WPANs) CITE THIS.
     - Rationale: IEEE 802.15.4 lays the framework for lower network layers such as 2.4 GHz as its within the range 2400–2483.5 MHz.
     
## Overview of Proposed Solution

The proposed solution for the RC subsystem is to provide wireless control of the Tennis Ball Collector using a controller with a 2.4GHz receiver connected to a Raspberry Pi. This will allow the customer to control the system easily. The subsystem will provide variable speed control, directional movement, and an emergency stop function. The subsystem will interact with the DC motors for moving as well as the power subsystem, vibration subsystem, counting subsystem, and display subsystem for the emergency stop function. The subsystem will follow IEEE 802.15.4 standards in using a 2.4 GHz reciver which will ensure reliable and mid ranged wireless communication protocols are used. The choice of controller and reciver were made such that the subsystem is reliable as well as cost effective to ensure that the overall cost of the system stays as low as possible for ease of access to consumers.


## Interface with Other Subsystems

Provide detailed information about the inputs, outputs, and data transferred to other subsystems. Ensure specificity and thoroughness, clarifying the method of communication and the nature of the data transmitted.

TODO!!!


## Operational Flowchart

For sections including a software component, produce a chart that demonstrates the decision-making process of the microcontroller. It should provide an overview of the device's function without exhaustive detail.

TODO!!!


## BOM

A complete list of all components needed for the design must be given with the cost of each component and the total cost of the subsystem. The BOM should be a markdown table. Make sure to to provide the manufacteror, part number, distributor, distributor part number, quantity, and price. Also provide a url where the product can be purchased from. If the componenet is refernced on your schematic make sure to include the component name.

Provide a comprehensive list of all necessary components along with their prices and the total cost of the subsystem. This information should be presented in a tabular format, complete with the manufacturer, part number, distributor, distributor part number, quantity, price, and purchasing website URL. If the component is included in your schematic diagram, ensure inclusion of the component name on the BOM (i.e R1, C45, U4).

| Manufacteror | Product Number | Distributor | Distributor Part Number | Quantity | Price | Purchase Link |
| ---------- | --------- | --------- | --------- | --------- | --------- | --------- | 
| Logitech G | 940-000117 | Logitech G |  940-000117 | 1 | 40 | [link](https://www.logitechg.com/en-us/products/gamepads/f710-wireless-gamepad.940-000117.html) |
| Raspberry Pi Holdings Ltd | 4292 | Raspberry Pi | 4292 | 1 | 45 | [link](https://www.adafruit.com/product/4292?src=raspberrypi) |
| Total Cost | N/A | N/A | N/A | N/A | 85 | N/A |

## Analysis

Deliver a full and relevant analysis of the design demonstrating that it should meet the constraints and accomplish the intended function. This analysis should be comprehensive and well articulated for persuasiveness.

TODO!!!

## References

All sources that have contributed to the detailed design and are not considered common knowledge should be duly cited, incorporating multiple references.

do ctrl f CITE THIS
