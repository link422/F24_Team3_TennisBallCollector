# Detailed Design


## Function of the Subsystem

The function of the Power Supply Subsystem is to detail the ways each component will be powered, and the steps needed to recreate the power system. Powering the system properly is important in running the entire project together, by ensuring the proper connections the project will operate correctly. To power the system the machine will function off of a single battery, a 12V rechargeable Li-ion battery [1] to control the RC motors and the Raspberry Pi. The Raspberry Pi will supply it is connected components with necessary power, turning on the sensor used to scan the collected balls and the display to show the number of scanned balls. The 12V battery will also supply power to the vibration motor used on the main body directly, causing the battery to have multiple connections. 


## Specifications and Constraints

- The Power Subsystem shall supply the Raspberry Pi with at least 5-volts.
  - The raspberry Pi needs a stable 5-volts to work continuously.
    
- Th Power Subsystem shall provide a stable and non-conductive surface for the Raspberry Pi to operate on.
  - The Raspberry Pi could be damaged if not properly secured.

- The Power Subsystem's batteries shall be subjected to vibration tests while installed onto the Mower main body 
  - These tests are mandatory to ensure total compatibility with the vibration motor, the team will test the battery while the vibration motor acts at the same time. 

- The Power Subsystem shall use specific colors for wiring of batteries and components.
  - Doing this shall minimize overcomplication of wiring and allow wire direction to be easily traced.

- The Power Subsystem shall have a 12 V Li-ion rechargeable Battery power the Raspberry Pi.
  - The rechargeable battery will allow multiple uses of the battery as long as there is a charge. 

- The Power Subsystem will supply the correct amount of power to the RC motors by usage of a driver motor.
  - The Lithium rechargeable Battery shall use an Open Frame Battery Charger to gain charge.

- Shall comply with 49 CFR 173.185 to prevent short-circuit damage
  - The standard goes into detail on the types of approved lithium batteries, as to not cause damage to the machine.
    
- Batteries shall operate safely within specified temperature ranges, with no risk of rupture, fire, or explosion due to temperature stress
  - The batteries must have the ability to be used at inconsistent rates, as to not damage the machine or the user. 
  
## Overview of Proposed Solution

The proposed solution of the Power Subsystem is focusing on powering the Raspberry Pi, RC wheels, Display systems, sensors, and vibration motors that are all connected to the Tennis ball Collector. The Raspberry Pi must be placed on the main body of the collector on a stable surface, so the vibrations do not mess with the connections coming from the Pi. The power supply for the Raspberry Pi will come from a 12-volt battery that will be connected through a buck convertor [2] to allow the necessary 5-volts. The 12-volt battery will also send 12-volts to the motor drivers controlling the wheels of the design. The LCD only needs 1mA to power on, which is provided from connecting into the Raspberry Pi. The Vibration motors are standard DC vibration motors needing 450 mA, this is supplied from the 12-volts after being stepped down to 5-volts. The Sensors are primarily contacted to the raspberry Pi as well and need only 20mA supplied to it.

## Interface with Other Subsystems

The Power Subsystem connects into all subsystems attached to tennis ball collector and starts by powering the connected Raspberry Pi to the rechargeable battery. To ensure the 12-volt battery doesn't overcharge the lower-voltage components, such as the Pi and DC vibration motors, the step-down converter will bring it down to 5-volts. For the sensor subsystem, the power subsystem is expected to power it with the rechargeable battery as it acts as an input to allow data collections, this requires no extra-voltage then what is being given to the Raspberry Pi. The LCD in the display subsystem is powered mainly through the Raspberry Pi not needing any external power to operate. The powering for the vibration subsystem's motors will be connected after the stepdown converter, allowing it to get the 5-volts necessary to operate. The Sensor, Display, and Vibration subsystems are expected to stay powered on as long as the battery is connected into the system. Power for the Motor subsystem will be directly connected to the Motor drivers to allow efficient output on the gears. The motor drivers shall be supplied with 12 amps of current. The RC subsystem does not require any external battery connections due to the controller being wireless.




## Circuit Design


![image](https://github.com/user-attachments/assets/5fa23260-60b9-4396-bf57-2e666d11d092)

- Red lines represents power
- Black lines represent grounding
- The green lines represent general connection of RC Motors 


## BOM


| Manufacturer | Product Number | Distributor | Distributor Part Number | Quantity | Price | Purchase Link |
| ---------- | --------- | --------- | --------- | --------- | --------- | --------- | 
| KBT KEEP BETTER TECH | B0C243MXMQ  | Amazon |  B0C243MXMQ | 1 | 16.99 | [link](https://www.amazon.com/KBT-1200mAh-rechargeable-Replacement-Compatible/dp/B0C243MXMQ/ref=asc_df_B0C243MXMQ?mcid=dea48368babc3c8f81704b14a90b61e6&hvocijid=18117759364931301635-B0C243MXMQ-&hvexpln=73&tag=hyprod-20&linkCode=df0&hvadid=721245378154&hvpos=&hvnetw=g&hvrand=18117759364931301635&hvpone=&hvptwo=&hvqmt=&hvdev=c&hvdvcmdl=&hvlocint=&hvlocphy=9013670&hvtargid=pla-2281435179258&th=1) |
| JZK | B071ZRXKJY| Amazon | B071ZRXKJY | 1 | 6.38 | [link](https://www.amazon.com/Connector-Airplane-Helicopter-Quadcopter-Multi-Motor/dp/B07L6BNTDV) |
| Total Cost | N/A | N/A | N/A | N/A | 23.37 | N/A |

## Analysis
The Power subsystem shall power all its specified components within the necessary constraints and have clear wiring. The subsystem will have two different-voltages, 12-volts and 5-volts, which will be used to operate the tennis ball collector system. The direction of the 12-volts coming directly from the battery will go to the motor drivers of the RC subsystem supplying them with effective power. The second direction of the 12-volts will go through a step-down convertor to output 5-volts. The 5-volts will then branch to both the DC vibration motors and the Raspberry Pi. The rechargeable battery outputs 1200mAh so it expected to power the system for up to 1.2 hours when fully charged. The amount of power going into each subsystem shall follow along given constraints as to ensure safety will operating the machine. 


## References
(1) "KBT 12V 1200mah rechargeable Li-Ion Battery, Bare Leads Wire Replacement Battery Pack with 12V Charger Compatible for 12V Devices RC Car, Boat, Robot, DIY, LED Light Kit : Health & Household." Amazon, www.amazon.com/KBT-1200mAh-rechargeable-Replacement-Compatible/dp/B0C243MXMQ. (Accessed 30 Jan. 2025.) 
(2) "JZK 24V / 12V to 5V 5A Power Buck Module DC-DC step-down Power Supply Converter with LED." Amazon, www.amazon.com/gp/product/B0B1DLJ7ZP/. (Accessed 30 Jan. 2025.)
