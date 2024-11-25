# Detailed Design


## Function of the Subsystem

The function of the Power Supply Subsystem is to detail the ways each component will be powered and the steps needed to recreate the power system. and for the hardware such as the DC motors, vibrating motors, display, and sensors. Powering the system properly is important in running the entire project together, by ensuring the proper connections the project will operate correctly. The 3.7 V Lithium Polymer Rechargeable Battery [12] will act as the main power system to power the Raspberry Pi. From the Raspberry Pi the connections run to the the different motors, sensors and display.


## Specifications and Constraints

The powering of the Raspberry Pi: 
- The Power subsystem shall utilize a 3.7 V Lithium battery to charge the Rasberry Pi
  - Bigger Battery will power Motors
    
- The Power Subsystem's batteries shall be subjected to vibration tests while installed onto the Mower main body 
  - These tests are mandatory to ensure total compability with the vibration motor, the team will test the battery while the vibration motor acts at the same time. 

- The Power Subsystem shall use specific colors for wiring of batteries and components.
  - Doing this shall minimize overcomplication of wiring and allow wire direction to be easily traced.

- The 3.7 V Lithium Polymer Rechargeable Battery [12] shall power the Raspberry Pi
  - The rechargable battery will allow multiple uses of the battery as long as there is a charge. 

The powering of the Rc Motors
- A 12 V battery will supply power to the RC motors by going through a driver motor.
  - The Lithium Rechargeable Battery shall use an Open Frame Battery Charger [3] to gain charge.

- Shall comply with 49 CFR 173.185 to prevent short-circuit damage
  - It is important to ensure the connections are effectively being used and not causing damage
    
- Batteries shall operate safely within specified temperature ranges, with no risk of rupture, fire, or explosion due to temperature stress
  - Batteries must have the ability to be used at inconsistant rates, as to not damage the machine or the user.  
  
## Overview of Proposed Solution

The proposed solution of the Power Subsystem is focusing on powering the Raspberry Pi, Rc wheels, Display systems, sensors, and vibration motors that are all connected to the Tennisball Collector. With the multiple components steming from the raspberry pi and batteries, ensuring accurate connections while powering important since incorrect powering can cause damage to the machine. 

## Interface with Other Subsystems

The Power Subsystem connects into all subsystems attached to tennisball collector and starts by powering the connected Raspberry Pi to the Lithium rechargeable battery. For the sensor subsystem, the power subsystem is expected to power it with the rechargable battery as it acts as an input to allow data collections. The collected data transfers to the Raspberry Pi that is also powered by the rechargable battery. The display subsystem is powered mainly through the Raspberry pi not needing any external power to operate. The vibration subsystem will use the power from the rechargable battery directly similarly to the sensor subsystem. The Raspberry Pi, Sensor, Display, and Vibration motor are expected to continually be powered by the recharable battery while the system runs. Power for the RC subsystem shall come from an alternative 12 V battery that is attached to the tennisball collector.


## Buildable Schematic 

Integrate a buildable electrical schematic directly into the document. If the diagram is unreadable or improperly scaled, the supervisor will deny approval. Divide the diagram into sections if the text and components seem too small.

The schematic should be relevant to the design and provide ample details necessary for constructing the model. It must be comprehensive so that someone, with no prior knowledge of the design, can easily understand it. Each related component's value and measurement should be clearly mentioned.



## BOM


| Manufacturer | Product Number | Distributor | Distributor Part Number | Quantity | Price | Purchase Link |
| ---------- | --------- | --------- | --------- | --------- | --------- | --------- | 
| Jauch Quartz | LP906090JH+PCM+2 WIRES 70MM  | DigiKey |  1908-LP906090JH+PCM+2WIRES70MM-ND | 1 | 23.64 | [link](https://www.digikey.com/en/products/detail/jauch-quartz/LP906090JH-PCM-2-WIRES-70MM/9560999) |
| Lipo Battery | 4292 | Raspberry Pi | 4292 | 1 | 45 | [link](https://www.adafruit.com/product/4292?src=raspberrypi) |
| Voltage reader | x | x | x | x | x | [link](https://www.adafruit.com/product/4292?src=raspberrypi) |
| Total Cost | N/A | N/A | N/A | N/A | 85 | N/A |

## Analysis
The Power subsytem shall power all its specified components within the neccessary constraints and have clear wiring. The subsystem will have two main points of power for the tennisball collector system. The first being a 11.1V Lipo Battery for powering the RC motors and the second being a 3.7V rechargable lithium battery to be used for the sensor, vibration motor, raspberry pi, and LCD display. The amount of power going into the each subsystem shall follow along given constraints as to ensure safety will operating the machine. 


## References

All sources that have contributed to the detailed design and are not considered common knowledge should be duly cited, incorporating multiple references.
