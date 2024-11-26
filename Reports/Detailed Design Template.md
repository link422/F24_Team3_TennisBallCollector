# Detailed Design


## Function of the Subsystem

The function of the Power Supply Subsystem is to detail the ways each component will be powered and the steps needed to recreate the power system. Powering the system properly is important in running the entire project together, by ensuring the proper connections the project will operate correctly. To power the system the machine will function off of two different batteries, a 11.1V rechargable Lipo battery [2] for control of RC motors and a 3.7V rechargable lithium battery [1] to power the Raspberry Pi. The Raspberry Pi will supply it's connected components with neccassary power, turning on the the sensor used to scan the collected balls and the display to show the number of scanned balls. The 3.7V battery will also supply power to the vibration motor used on the main body directly, causing the battery to have multiple connections. The power subsystem is made to efficiently and safely power the many components in the system as to not cause damage to the user or the machine.


## Specifications and Constraints

- The Power Subsystem shall supply the Raspberry Pi with at least 5 volts.
  - The raspberry Pi needs a stable 5 volts to work continuely.
    
- Th Power Subsystem shall provide a stable and non-conductive surface for the Raspberry Pi to operate on.
  - The Raspberry Pi could be damaged if not properly secured.

- The Power Subsystem's batteries shall be subjected to vibration tests while installed onto the Mower main body 
  - These tests are mandatory to ensure total compability with the vibration motor, the team will test the battery while the vibration motor acts at the same time. 

- The Power Subsystem shall use specific colors for wiring of batteries and components.
  - Doing this shall minimize overcomplication of wiring and allow wire direction to be easily traced.

- The Power Subsystem will have 3.7 V Lithium Polymer Rechargeable Battery shall power the Raspberry Pi.
  - The rechargable battery will allow multiple uses of the battery as long as there is a charge. 

- The Power Subsystem will supply the correct amount of power to the RC motors by usage of a driver motor.
  - The Lithium Rechargeable Battery shall use an Open Frame Battery Charger to gain charge.

- Shall comply with 49 CFR 173.185 to prevent short-circuit damage
  - The standard goes into detail on the types of approved lithium batteries, as to not cuz damage to the machine.
    
- Batteries shall operate safely within specified temperature ranges, with no risk of rupture, fire, or explosion due to temperature stress
  - The batteries must have the ability to be used at inconsistant rates, as to not damage the machine or the user.  
  
## Overview of Proposed Solution

The proposed solution of the Power Subsystem is focusing on powering the Raspberry Pi, Rc wheels, Display systems, sensors, and vibration motors that are all connected to the Tennisball Collector. The Raspberry Pi must be placed on the main body of the collector on a stable surface so the vibrations do not mess with the connections coming from the Pi. The wired connections for the Pi will be sorted in a way that makes issues easy to detect. The battery connected into the Pi will have a secure casing as well to not allow loose wires to affect the machines desired output. The second 11.1V Lipo Battery will have a testers set in place such as a battery tester [4]to ensure there is no overflow of power going into the motors. All testing will be done before it is installed onto the machine for ease of testing, after connections are made correctly it will then be installed on the machine with the same connections as before.


## Interface with Other Subsystems

The Power Subsystem connects into all subsystems attached to tennisball collector and starts by powering the connected Raspberry Pi to the Lithium rechargeable battery. For the sensor subsystem, the power subsystem is expected to power it with the rechargable battery as it acts as an input to allow data collections. The collected data transfers to the Raspberry Pi that is also powered by the rechargable battery. The display subsystem is powered mainly through the Raspberry Pi not needing any external power to operate. The vibration subsystem will use the power from the rechargable battery directly similarly to the sensor subsystem. The Raspberry Pi, Sensor, Display, and Vibration motor are expected to continually be powered by the recharable battery while the system runs. Power for the RC subsystem shall come from an alternative 11.1 V battery [1] that is attached to the tennisball collector. The power will go to motor driver first to disperse the voltage ingto something readable for the Raspberry Pi


## Circuit Design

![image](https://github.com/user-attachments/assets/6a254889-1bd9-4de9-bb13-1f803c1aee14)

## BOM


| Manufacturer | Product Number | Distributor | Distributor Part Number | Quantity | Price | Purchase Link |
| ---------- | --------- | --------- | --------- | --------- | --------- | --------- | 
| Jauch Quartz | LP906090JH+PCM+2 WIRES 70MM  | DigiKey |  1908-LP906090JH+PCM+2WIRES70MM-ND | 1 | 23.64 | [link](https://www.digikey.com/en/products/detail/jauch-quartz/LP906090JH-PCM-2-WIRES-70MM/9560999) |
| Emate | BO7L6BNTDV| Amazon | 0-50C-1400-3S1P-XT60+TRX | 1 | 13.60 | [link](https://www.adafruit.com/product/4292?src=raspberrypi) |
| Yueton | 5060768824800 | Amazon | HOME0098 | 1 | 5.50 | [link](https://www.amazon.com/Battery-Monitor-Voltage-Checker-Indicator/dp/B013U1CP08/ref=asc_df_B013U1CP08?mcid=057b15c4cb2232cf886245a8cf1b0621&tag=hyprod-20&linkCode=df0&hvadid=693308318554&hvpos=&hvnetw=g&hvrand=14971361529341986625&hvpone=&hvptwo=&hvqmt=&hvdev=c&hvdvcmdl=&hvlocint=&hvlocphy=1025954&hvtargid=pla-304998738630&psc=1) |
| Total Cost | N/A | N/A | N/A | N/A | 42.74 | N/A |

## Analysis
The Power subsytem shall power all its specified components within the neccessary constraints and have clear wiring. The subsystem will have two main points of power for the tennisball collector system. The first being a 11.1V Lipo Battery for powering the RC motors and the second being a 3.7V rechargable lithium battery to be used for the sensor, vibration motor, raspberry pi, and LCD display. The amount of power going into the each subsystem shall follow along given constraints as to ensure safety will operating the machine. When correctly connected all components will operate at efcient levels to provide clear and effective results.


## References
- "LP906090JH PCM 2 Wires 70mm." *Digi-Key Electronics*, Jauch Quartz, www.digikey.com/en/products/detail/jauch-quartz/LP906090JH-PCM-2-WIRES-70MM/9560999. (Accessed 24 Nov. 2024.)
- "Connector Airplane Helicopter Quadcopter Multi-Motor." Amazon, www.amazon.com/Connector-Airplane-Helicopter-Quadcopter-Multi-Motor/dp/B07L6BNTDV/. (Accessed 24 Nov. 2024.)
- "Product B0B1DLJ7ZP." Amazon, www.amazon.com/gp/product/B0B1DLJ7ZP/. (Accessed 24 Nov. 2024.)
- "Battery Monitor Voltage Checker Indicator." Amazon, www.amazon.com/Battery-Monitor-Voltage-Checker-Indicator/dp/B013U1CP08/. (Accessed 24 Nov. 2024.)

