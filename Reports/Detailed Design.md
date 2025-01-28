# Detailed Design


## Function of the Subsystem

The function of the Power Supply Subsystem is to detail the ways each component will be powered, and the steps needed to recreate the power system. Powering the system properly is important in running the entire project together, by ensuring the proper connections the project will operate correctly. To power the system the machine will function off of two different batteries, a 11.1V rechargeable Lipo battery [2] for control of RC motors and a 5V rechargeable lithium battery [1] to power the Raspberry Pi. The Raspberry Pi will supply it is connected components with necessary power, turning on the sensor used to scan the collected balls and the display to show the number of scanned balls. The 5V battery will also supply power to the vibration motor used on the main body directly, causing the battery to have multiple connections. 


## Specifications and Constraints

- The Power Subsystem shall supply the Raspberry Pi with at least 5 volts.
  - The raspberry Pi needs a stable 5 volts to work continuously.
    
- Th Power Subsystem shall provide a stable and non-conductive surface for the Raspberry Pi to operate on.
  - The Raspberry Pi could be damaged if not properly secured.

- The Power Subsystem's batteries shall be subjected to vibration tests while installed onto the Mower main body 
  - These tests are mandatory to ensure total compatibility with the vibration motor, the team will test the battery while the vibration motor acts at the same time. 

- The Power Subsystem shall use specific colors for wiring of batteries and components.
  - Doing this shall minimize overcomplication of wiring and allow wire direction to be easily traced.

- The Power Subsystem will have 5 V Lithium Polymer Rechargeable Battery shall power the Raspberry Pi.
  - The rechargeable battery will allow multiple uses of the battery as long as there is a charge. 

- The Power Subsystem will supply the correct amount of power to the RC motors by usage of a driver motor.
  - The Lithium Rechargeable Battery shall use an Open Frame Battery Charger to gain charge.

- Shall comply with 49 CFR 173.185 to prevent short-circuit damage
  - The standard goes into detail on the types of approved lithium batteries, as to not cause damage to the machine.
    
- Batteries shall operate safely within specified temperature ranges, with no risk of rupture, fire, or explosion due to temperature stress
  - The batteries must have the ability to be used at inconsistent rates, as to not damage the machine or the user. 
  
## Overview of Proposed Solution

The proposed solution of the Power Subsystem is focusing on powering the Raspberry Pi, RC wheels, Display systems, sensors, and vibration motors that are all connected to the Tennis ball Collector. The Raspberry Pi must be placed on the main body of the collector on a stable surface, so the vibrations do not mess with the connections coming from the Pi. The power supply for the Raspberry Pi will come from a 12 Volt battery that will be connected through a step down convertor to allow the neccessary 5 volts. The 12 volt battery will also send 12 volts to the motor drivers controlling the wheels of the design.
The LCD will allow
The Vibration motors
The Sensors 

## Interface with Other Subsystems

The Power Subsystem connects into all subsystems attached to tennis ball collector and starts by powering the connected Raspberry Pi to the 5V rechargeable battery. For the sensor subsystem, the power subsystem is expected to power it with the rechargeable battery as it acts as an input to allow data collections, this requires no extra voltage then what is being given to the Raspberry Pi. The collected data transfers to the Raspberry Pi that is also powered by the rechargeable battery. The display subsystem is powered mainly through the Raspberry Pi not needing any external power to operate. The vibration subsystem will use the power from the rechargeable battery directly similarly to the sensor subsystem. The Raspberry Pi, Sensor, Display, and Vibration motor are expected to continually be powered by the rechargeable battery when connected together. Power for the RC subsystem shall come from the Lipo 11.1 V battery that is attached to the tennis ball collector. The Lipo battery will supply the motor drivers used in the RC subsystem with up to 12A. This power supplied to the drivers then goes to the RC wheels so they can operate as needed. 


## Circuit Design

![Screenshot 2024-12-05 210703](https://github.com/user-attachments/assets/1b851988-9cc1-4bcf-b753-8e106f1760f4)

- Red lines represents power
- Black lines represent grounding
- The green lines represent general connection of RC Motors 


## BOM


| Manufacturer | Product Number | Distributor | Distributor Part Number | Quantity | Price | Purchase Link |
| ---------- | --------- | --------- | --------- | --------- | --------- | --------- | 
| KBT KEEP BETTER TECH | B0CX8VQWJ6  | Amazon |  B0CX8VQWJ6 | 1 | 11.99 | [link](https://www.amazon.com/KBT-4000mAh-Rechargeable-Lithium-ion-Connector/dp/B0CX8VQWJ6?th=1) |
| Emate | BO7L6BNTDV| Amazon | 0-50C-1400-3S1P-XT60+TRX | 1 | 13.60 | [link](https://www.amazon.com/Connector-Airplane-Helicopter-Quadcopter-Multi-Motor/dp/B07L6BNTDV) |
| Yueton | 5060768824800 | Amazon | HOME0098 | 1 | 5.50 | [link](https://www.amazon.com/Battery-Monitor-Voltage-Checker-Indicator/dp/B013U1CP08/ref=asc_df_B013U1CP08?mcid=057b15c4cb2232cf886245a8cf1b0621&tag=hyprod-20&linkCode=df0&hvadid=693308318554&hvpos=&hvnetw=g&hvrand=14971361529341986625&hvpone=&hvptwo=&hvqmt=&hvdev=c&hvdvcmdl=&hvlocint=&hvlocphy=1025954&hvtargid=pla-304998738630&psc=1) |
| Total Cost | N/A | N/A | N/A | N/A | 21.10 | N/A |
[link](https://www.amazon.com/Battery-Monitor-Voltage-Checker-Indicator/dp/B013U1CP08/ref=asc_df_B013U1CP08?mcid=057b15c4cb2232cf886245a8cf1b0621&tag=hyprod-20&linkCode=df0&hvadid=693308318554&hvpos=&hvnetw=g&hvrand=14971361529341986625&hvpone=&hvptwo=&hvqmt=&hvdev=c&hvdvcmdl=&hvlocint=&hvlocphy=1025954&hvtargid=pla-304998738630&psc=1)
## Analysis
The Power subsystem shall power all its specified components within the necessary constraints and have clear wiring. The subsystem will have two main points of needing power for the tennis ball collector system. 
The first being powering the RC motors and the second being powering the sensor, vibration motor, raspberry pi, and LCD display. 
The Lidar sensor as well as the LCD used will receive all necessary power from the Raspberry Pi. The vibration motor however will require a continuous 3A to operate. The amount of time every part is expected to be powered for around 10-15 minutes, and with a recharable 12 volt battery with a on and off switch this will work. The amount of power going into each subsystem shall follow along given constraints as to ensure safety will operating the machine. When correctly connected all components will operate at efficient levels to provide clear and effective results.


## References
- Amazon. (n.d.). KBT 4000mAh rechargeable lithium-ion battery with connector. Retrieved November 24, 2024, from https://www.amazon.com/KBT-4000mAh-Rechargeable-Lithium-ion-Connector/dp/B0CX8VQWJ6?th=1
- "Connector Airplane Helicopter Quadcopter Multi-Motor." Amazon, www.amazon.com/Connector-Airplane-Helicopter-Quadcopter-Multi-Motor/dp/B07L6BNTDV/. (Accessed 24 Nov. 2024.)
- "Product B0B1DLJ7ZP." Amazon, www.amazon.com/gp/product/B0B1DLJ7ZP/. (Accessed 24 Nov. 2024.)
- "Battery Monitor Voltage Checker Indicator." Amazon, www.amazon.com/Battery-Monitor-Voltage-Checker-Indicator/dp/B013U1CP08/. (Accessed 24 Nov. 2024.)
