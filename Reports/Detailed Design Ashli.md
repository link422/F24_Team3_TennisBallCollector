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

The proposed solution for this Motor subsystem is to provide user controlled motors on the pre-existing wheels of the tennis ball collector. 2 motors, Makermotor High Torque Gearmotor 12V DC 6RPM Conveyor Gear Motor [2], will be controlled by a motor driver, Sabertooth dual 12A motor driver (Sabertooth 2x12) [4]; targeting control in the back larger wheels for simplicity as they drive most of the movement. Connectivity outside the motor subsystem will be through the motor driver [4] that will satisfy specifications including connecting DC motors [2] to power supply and raspberry pi [3], connecting tennis ball collector's wheels to the Raspberry Pi, controlling movement and rotation of the collector [1] without any manual help, and recieving inputs of direction from RC subsystem.

The Sabertooth dual 12A motor driver [4] will be configured to operate using the schematic featured in the Buildable Schematic section and connection of motors using pulley and belt system. IEEE Standard 112 [8] testing will commence once all required motor components have been received and the necessary equipment has been prepared and verified for functionality.

## Interface with Other Subsystems


The Motor subsystem has few inputs and outputs as one of the technical applications of the design. Inputs include the Power Supply System subsystem's supply voltage using a compatible battery and the RC subsystem's input user instructions recieved from the raspberry pi microprocessor [3]. All are inputs to the motor drivers which in turn, output's control to the motors [2] for movement in the tennis ball collector [1]. 


## Buildable Schematic 

### Solution

RC subsystem will recieve user input that will wirelessly connect to the raspberry pi microprocessor [3]. To ensure the signals are properly shifted to the required voltage levels, the level shifter [5] will be a median between the motor driver [4] and the raspberry pi. The motor driver will recieve input from the raspberry pi and using power from the power supply subsystem's battery the motor driver will power on its corresponding motors, providing non-manual movement to the collector [1]. 


![Capstone;)-5](https://github.com/user-attachments/assets/b29cfaad-eb5a-4e5e-9ac7-0063c703000e)





## Printed Circuit Board Layout

### Level Shifter : SparkFun Logic Level Converter - Bi-Directional 
![image](https://github.com/user-attachments/assets/40933d9c-2bdf-45d3-9f46-6e6a17af1974)

### Motor Driver : Sabertooth dual 12A motor driver
![image](https://github.com/user-attachments/assets/5ac08e86-255c-49be-a490-a7906887921e)

### Motor : Makermotor High Torque Gearmotor 12V DC 6RPM Conveyor Gear Motor

<img width="703" alt="Screenshot 2025-02-01 at 10 32 25 AM" src="https://github.com/user-attachments/assets/8b350bcd-bab9-4024-9ee3-be8640bdb52c" />


Installation shown in Analysis section

## BOM



| Component | Manufacterer | Product Number | Distributor | Distributor Part Number | Quantity | Price | Schematic Label | Purchase Link |
| ---------- | ---------- | --------- | --------- | --------- | --------- | --------- | --------- | --------- | 
| Sabertooth dual 12A motor driver | Dimension Engineering | SABERTOOTH 2X12 | DFRobot |  DRI0003 | 1 | 79.00 | D2x12 | [link](https://www.dfrobot.com/product-304.html) |
| Makermotor High Torque Gearmotor 12V DC 6RPM Conveyor Gear Motor | Makermotor | PN00113-6 | Amazon | B01890J6UW | 2 | 115.00 + 24.50 (shipping) | M50/Motors | [link](https://www.amazon.com/Makermotor-Torque-Gearmotor-Conveyor-Motor/dp/B01890J6UW?crid=FFFK3US0UTMP&dib=eyJ2IjoiMSJ9.Q9X_ekkq4Pnt-SCPsIByem9zFOtMHohVW9LYIAgq-i--aWRN1jk_abIqb4Z0boq-nsNk3rNYsqXsZ792wH6AWAaMB-wz0JlVvvuGxxpSega7GZVmJlvDplqDbd_xiO9Haa72QBXavtKZFi6OQfm95XJukHDaE2QREk5YxPkBCorwcusgbGS3y_7N7CFwzWn9BWLCFPsJrYp4-m3ApSK1TGJ9mvAobNW6pg26LOrmoXwe5dF_0LPlqXPcucPXX_uP_MqWffSH2xzQyxKJX1OILaxcRZbS0fx2mP1-uHanVobTh0CN2j6CCxy_owqOyziOq-Bbe3JkK2LrDxublglC4G4YZ4sCTTuZ8UxnP4o821LyqpK8j12JeWNsaLsOdLG4pXftp4oZauKAFSYyxpCR3tolMPhqgJDlbDvFH2FQ56MGBeusukfEsUyivF91fJOi.iwtwsuRRASnjylxk02lBdjk_u4gzNsFKogCkM_3qwa0&dib_tag=se&keywords=maker%5Cmotor&qid=1738426589&sprefix=makermotor%2Caps%2C216&sr=8-23) |
| SparkFun Logic Level Converter - Bi-Directional | SparkFun Electronics | BOB-12009 | DigiKey |  1568-1209-ND | 1 | 3.50 | LS | [link](https://www.digikey.com/en/products/detail/sparkfun-electronics/BOB-12009/5673795?s=N4IgTCBcDaIIwFYBsAOAtHMAGAnGgcgCKDQBCALoC%2BQA) |
| 120pcs 20 cm Breadboard Jumper Wires Dupont Cable Assorted Kit| EDGELEC | ED-DP_L20_Mix_120pcs | Amazon | B07GD2BWPY | 1 | 6.98 | N/A | [link](https://www.amazon.com/EDGELEC-Breadboard-Optional-Assorted-Multicolored/dp/B07GD2BWPY?crid=3DGC320SX81Z2&dib=eyJ2IjoiMSJ9.APYjLeLR3cSKMa-3o77o4cYI1olfvBTpJBIBWrLqSaoqeqjKWlnOg1F7dI1ZHbmBbHXPnl9A-zfQjw7P80ggVPZr7fM9E61QH7DOhZ_nWHnJ6KQoWLD4hxEjd2VbMnSznD3cFZ049cNPHb-py6kYwTtqcH3GbSuH7vg1aoHE7ebusdWXj1c0YVqajUVuVcP0oktnHN8Mv2MMez3cyrXOVYzVh3j4K00H6j53cig7Ex4.4b2v71rjNo84MGdm-KeQ8BLrgu2huoe5dUA729xcNXA&dib_tag=se&keywords=jump%2Bwires%2Bmale%2Bto%2Bmale%2C%2Bmale%2Bto%2Bfemale%2C%2Bfemale%2Bto%2Bfemale&qid=1732744550&sprefix=jump%2Bwires%2Bmale%2Bto%2Bmale%2C%2Bmale%2Bto%2Bfemale%2C%2Bfemale%2Bto%2Bfemale%2Caps%2C147&sr=8-1&th=1) |
| AZSSMUK 08A 40# Roller Chain - 5 Feet 40Mn Carbon Steel Material with 1 Connecting Link for Go Kart, Mini Bike Chain Replacement | AZSSMUK | MAXLER | Amazon | B079L72M2V | 2 | 13.99 | Sprocket and Chain Drive | [link](https://www.amazon.com/Aobbmok-Roller-Chain-Connecting-Replacements/dp/B079L72M2V?crid=PIUBEA96E714&dib=eyJ2IjoiMSJ9.cctI3hRBcZxu_ycCiZFonsfAW1wb-uNxiFLm6bleJgVY8nD3DBPD7WY16KsbHtYB4wNSXRSan6MjmNUI1cq_rz7XP0Cg2W5OIGsOPTVbgzKxisG0CfpnPhej4uQxF7FWp85FWs0lb_PsCZtFJqUnxsm5OOpT4ZMK0hwLgLtA-xXoM5-xeTwWVNcoNa-EE58yGgHurztlMKHzqd1CKNTDWTo5oypTSR_DXagpK0MowaY.4MD-SatGKf8DkQihdCIhgjb0sip0wH5ZKGYJwF4mm28&dib_tag=se&keywords=roller%2Bchain%2B40&qid=1738461187&sprefix=roller%2Bchain%2B40%2Caps%2C180&sr=8-6&th=1) |
| uxcell 2pcs ANSI #40 / DIN(ISO)08A Roller Chain Idler Sprocket 15mm Bore, 1/2" Pitch, Hardened 15 Tooth Tensioner Sprocket, Insert Single Bearing (B Type) | uxcell | N/A | Amazon | B0CNSGX2RB | 1 | 27.09 | "Motors" (Motor-Sprocket Connection) | [link](https://www.amazon.com/uxcell-Sprocket-Hardened-Tensioner-Bearing/dp/B0CNSGX2RB?crid=26EP8PRTDG0FX&dib=eyJ2IjoiMSJ9.4c9I2pQ9tfO2Lx866RMSfdz5z2mSuC-57w3ttb1NQJc_gftIVww5ei_NFen8GUNK7IqGBktRlzv4RAQLhgpwD_BhKTr02bwZ0vOss12z6SLSxssfILlClr_NYwUASfboJJQQ9A9UjV76xlnAF7g3k40hlkzEQfnAe8nydV9bZRYab-jfyQrRuPwBtNHv9zu8uCVn_FaRFPyeDlW_NEflkOrLwo9B7QlaGGVAwGFtH30.zf7oUCfGfPOOeMfC5WzioXQ-isqOu5F2YZeZO3axWGo&dib_tag=se&keywords=%2340+roller+chain+sprocket+15mm+bore&qid=1738465023&sprefix=15mm+%2340+sp%2Caps%2C113&sr=8-3) |
| Jeremywell #40 Roller Chain Sprocket B Type 1" Bore Hardened 12 Tooth | Jeremywell | 40BS12H | Amazon | B08DDKLYMF | 2 | 18.45 | Bevel/Sprocket Hub | [link](https://www.amazon.com/Jeremywell-40BS12H-1-Tooth-Sprocket-Roller/dp/B08DDKLYMF?crid=3QXM1Q3Q259YY&dib=eyJ2IjoiMSJ9.eHq2qMWk_gU-Q967Zd8a4dwBOf81104aE_hJYjO19nVlbWbAyKQ2JhRfD4On6Q5A53D2RPeeQzwq6WTjKMb6ZyjPVFBzLiDF30BvHpBhNnQmUPTnslf6PutXO-K8toVb1maPpv7eSILN6kGG5RtihufMgbNn8ATkbKZI8vFtcjl3ldNYhrf72c4vu-rBffsur6KYLXLVoNCod7btfuJu4kYWYeAigeYV7_B_1Z66Vz9IBavoXvFOnCQ0CQxnlsdzJSz-Vo_Du1M4r9-nHMQcGfuq4umWL_19mGEwZHwdKHtxT1iqG1V9XwrUy_1ocLaYCtvtO6MRYZMRHrPex6O7ihuTTX1EydUTgT2vpaAFi-Y.KAHWSK25yG6iv_iKQTwQQRrhKl4P0uctOMVWdxHDrAg&dib_tag=se&keywords=%2340%2BRoller%2BChain%2BSprocket%2BB%2BType%2B1%27%27%2B12%2Btooth&qid=1738461979&s=industrial&sprefix=%2B40%2Broller%2Bchain%2Bsprocket%2Bb%2Btype%2B1%27%27%2B12%2Btooth%2Cindustrial%2C175&sr=1-4&th=1) |
| 2 Pcs 1.5M 20 Teeth 8/10/12/14/15/16mm Shaft Hole Tapered Bevel Gear 1: 1# 45 Steel 1.5 Module 90 Degree Steering Gear with M5 Fixing Hole (12mm) | PGFUN | TYXC-0011_1.5_20_12 | Amazon | B09VGPWQSQ | 1 | 13.99 | Bevel | [link](https://www.amazon.com/PGFUN-Teeth-Shaft-Tapered-Bevel/dp/B09VGPWQSQ?crid=1UCJMBJGVPPM3&dib=eyJ2IjoiMSJ9.dFIRvfj8nzZrceaqvGTgcawWpd03jtaeqbcw-NzG3sPJZQALyZWqZOPUCKwM5CDXO0w2N64mMGc8zDS9qjmYr1vuGtMJaUgS4IP3cLRsX9f4NbuncOyO6rNCmOLH7e_tRBAw5vnX74ObLVL7hMpwEw27bxMgPw5cmCtRgiaGPk4dhz2ZRp3r6cGEYWKpbxh3BMam1Itd4OB6a7mL0H7cLQIc7_nJXoEomoLizPzRGT4.jJQF5s_2g1LHmYxEmKVJp-g1MJkYeL58PHAKA8u0swU&dib_tag=se&keywords=bevel%2Bgear%2B1%2Bin&qid=1738468301&sprefix=bevel%2Bgear%2B1%2Bin%2Caps%2C126&sr=8-1&th=1) |
| Total Cost | N/A | N/A | N/A | N/A | N/A | $449.94 | N/A |

## Analysis

Operations will be carried out from inputs and safety precautions of the RC subsystem and Power Supply subsystem  the raspberry pi [3] and 2 Sabertooth dual 12A motor driver[4] (each handling up to 2 DC motors[2]). The soluion will consist of 2 DC gearmotors,  Makermotor High Torque Gearmotor 12V DC 6RPM Conveyor Gear Motor [2], capable of operating a weight load similar to the 44 lb Playmate Ball Mower 2.0 [7]. This design choice was established considering torque, weight distribution, and speed. The use of 4 motors will handle the load of 44 lb by attaching to it's drive wheels (2) in the back. One of our competitors, Tennibot travels at 1.4 mph (0.6258 m/s); preferably we would like to get close to that speed, this will be done with a speed increasing sprocket and chain system.


### Desired Motor Specifications: 

Assumptions of environment: Starts with no added weight (0 collected tennis balls) on smooth, acrylic/clay court -> $\mu$ $\approx$ 0.01

#### Initial (static torque) 

Desired Horsepower/Watts for tennis collector (RPM * Torque / 5252)

Rear Wheel Diameter, D = 14in ,, 0.3556 m) 

s = speed (m), C = circumference, W = load per wheel (2), r = wheel radius (m) = D/2

RPM = 60 * s / C = 0.6258 * 60 / ( $\pi * 0.3556) = 33.61 RPM

Torque = W * r = ((44 * 4.448) / 2) * 0.1778 $\approx$ 17.4 Nm = 12.83 lb-ft

Power = (33.61 * 12.83)/ 5252 $\approx$ 0.082 Hp $\approx$ 61.2 W

current = P/V = 61.2/12 = 5.1 A (peak current)
   
#### Continuous (dynamic torque)
Rear Wheel Diameter d = 14in ,, 0.3556 m -> radius r = 0.1778 m 

s = desired speed (m) = 0.6258 m/s

C = circumference = ($\pi * 0.3556)

Acceleration a = 0.2 m/$s^2$

Moderate acceleration for slow-moving device, m = load per wheel = 44/2 lb = 22 lb $\approx$ 10 kg

RPM = 60 * s / C = 33.61 RPM

Frictional Force = $\mu$ * m * g = 0.981 N

Acceleration Force = m * a = 2 N

Total Force per Wheel = 2.981

Torque per Wheel $\tau$ = Total Force * r $\approx$ 0.53 N, for safety margin total T * 1.5 = 1.59 N

Power($\tau$ * $\omega$) P = (1.59 * 33.61)/9.549 $\approx$ 5.6 W 

Considering an added weight of tennis balls (100): 
same procedure leads us to => 2.07 Nm total torque required (1.04 Nm on each motor); desired current to be P/V = 7.15/12 $\approx$ 0.6 A

### Motor Rationale: Makermotor High Torque Gearmotor 12V DC 6RPM Conveyor Gear Motor
21 N-m (15.5 ft-lb) torque at 6 RPM; Shaft dimensions are 15mm diameter by 50mm (2.0 inches) of length.  The shaft is a D-shaft (shaft with a flat).

### Specifications for Alignment 

At start up, we will need all the torque given by the motor, but as we continue it would be favorable if speed increases. To ensure this and keep the design as simple as possible, we will use a sprocket and chain drive. Location of this focus, depends on the metal barrel that feeds tennis balls into the collection basket; if it has enough space to easily confide within it without disturbing the function of other subsystems and ball collecting. If at any point it is inferred that that is impossible, we make the motor subsystem external; this will only add scrap metal or 3d printed barring as needed to hold the components. 

#### Sprocket and Chain Drive

Due to the limited space in the direction adjacent to the wheel, we need to have a bevel gear set [10] to shift the output by 90 degrees, allowing for hidden  sprocket and chain drive connecing to the motor. 

For the SC drive, the turned wheel output will be linked to a sprocket, which by chain will connect to the motor. For execution, we will need a wheel sprocket [13] and a motor sprocket [12]. For simplicity, we will make the motor sprocket 12 teeth, and the wheel socket 12 teeth with a #40 roller chain [11].

![design](https://github.com/user-attachments/assets/255b2d81-3017-44d0-bff8-5ad7d472c6ab)


## References
[1] "BALL MOWER." PLAYMATE Tennis, 5 June 2023, www.playmatetennis.com/ball-mower/

[2] “Makermotor High Torque Gearmotor 12V DC 6RPM Conveyor Gear Motor.” amazon.com, 8 September 2011, [https://www.amazon.com/Makermotor-Torque-Gearmotor-Conveyor-Motor/](https://www.amazon.com/Makermotor-Torque-Gearmotor-Conveyor-Motor/dp/B01890J6UW?crid=2UYAOB5PJGPJC&dib=eyJ2IjoiMSJ9.QyJ7dWqdbUJFV4Z3vxTzYv5q6VTMUr1toHcuorTLZkSz6JPO9eRZbK2_9vNilJTBjt7pQBmsIrahrwTTa5m0Wtu5NAPRFtodIjqK8NQAuAjcR7p7cgQWpwaIv7e8MBsJooJWIP-H9AiRClwPD_s17C1pwnnYdkKIqkn-_Eq9gVUsBHNzDOz6LHY82lrc38RKnzWV15vCOqKh-KryHls_GdKr9flt6JddVYAHpYlNlkh9BRHedd-CXgjuW2-H_CT6TLZpJ2ATEC0Pf91IjbfHP-AbZ65niq1bFqFLZxbFHp_Zhbw8FwAuzK_Yb0-PAVkhEpwRsYgEJCe3HPdzXOmkzRLkzaEfVA_dA6bbf02Lg2z0ZSumK7V0gPKW6gtqDV8edKZxp5SG34x3dS-09Dqj3CZU2aX1IBgBp0gEfiNqq4LuCFjoVVNu6IeNcdsIDPXF.eykrnPWY5i8EMRbGOvpRQrPUOaJ2t1Sd8IfFHJ5cFSM&dib_tag=se&keywords=12v+high+torque+dc+motor+low+speed&qid=1738352199&refinements=p_36%3A9400-&rnid=1243644011&sprefix=12v+high+torque+dc+motor+low+speed%2Caps%2C177&sr=8-2)

[3] Ltd, Raspberry P. "Buy a Raspberry Pi 4 Model B – Raspberry Pi." Raspberry Pi, https://www.raspberrypi.com/products/raspberry-pi-4-model-b/

[4] "Sabertooth 2X12 Regenerative Dual Motor Driver." Dimension Engineering, Power Electronics, Sensors, www.dimensionengineering.com/products/sabertooth2x12/

[5] "Bi-Directional Logic Level Converter Hookup Guide." Learn at SparkFun Electronics - SparkFun Learn, https://learn.sparkfun.com/tutorials/bi-directional-logic-level-converter-hookup-guide/all/

[6] "Ball Mower Caster Bracket Kit | Playmate Tennis Court Parts & Accessories | DH Distribution." DH Distribution, https://dhtennis.net/product/mower-caster-bracket-kit/

[7] "Playmate Ball Mower | Playmate Tennis Court Products | DH Distribution." DH Distribution, 9 Oct. 2024, https://dhtennis.net/product/the-playmate-ball-mower-2-0/

[8] Institute of Electrical and Electronics Engineers. IEEE Standard Test Procedure for Polyphase Induction Motors and Generators. Iowa State University, 1997.

[9] "Ball Mower Replacement Casters | Playmate Tennis Court Parts & Accessories | DH Distribution." DH Distribution, 
https://dhtennis.net/product/replacement-caster-for-ball-mower/


[10] "2 Pcs 1.5M 20 Teeth 8/10/12/14/15/16mm Shaft Hole Tapered Bevel Gear 1: 1# 45 Steel 1.5 Module 90 Degree Steering Gear with M5 Fixing Hole (12mm)." Amazon, https://www.amazon.com/PGFUN-Teeth-Shaft-Tapered-Bevel/dp/B09VGPWQSQ?crid=1UCJMBJGVPPM3&dib=eyJ2IjoiMSJ9.dFIRvfj8nzZrceaqvGTgcawWpd03jtaeqbcw-NzG3sPJZQALyZWqZOPUCKwM5CDXO0w2N64mMGc8zDS9qjmYr1vuGtMJaUgS4IP3cLRsX9f4NbuncOyO6rNCmOLH7e_tRBAw5vnX74ObLVL7hMpwEw27bxMgPw5cmCtRgiaGPk4dhz2ZRp3r6cGEYWKpbxh3BMam1Itd4OB6a7mL0H7cLQIc7_nJXoEomoLizPzRGT4.jJQF5s_2g1LHmYxEmKVJp-g1MJkYeL58PHAKA8u0swU&dib_tag=se&keywords=bevel%2Bgear%2B1%2Bin&qid=1738468301&sprefix=bevel%2Bgear%2B1%2Bin%2Caps%2C126&sr=8-1&th=1

[11]"AZSSMUK 08A 40# Roller Chain - 5 Feet 40Mn Carbon Steel Material with 1 Connecting Link for Go Kart, Mini Bike Chain Replacement." Amazon, https://www.amazon.com/Aobbmok-Roller-Chain-Connecting-Replacements/dp/B079L72M2V?crid=PIUBEA96E714&dib=eyJ2IjoiMSJ9.cctI3hRBcZxu_ycCiZFonsfAW1wb-uNxiFLm6bleJgVY8nD3DBPD7WY16KsbHtYB4wNSXRSan6MjmNUI1cq_rz7XP0Cg2W5OIGsOPTVbgzKxisG0CfpnPhej4uQxF7FWp85FWs0lb_PsCZtFJqUnxsm5OOpT4ZMK0hwLgLtA-xXoM5-xeTwWVNcoNa-EE58yGgHurztlMKHzqd1CKNTDWTo5oypTSR_DXagpK0MowaY.4MD-SatGKf8DkQihdCIhgjb0sip0wH5ZKGYJwF4mm28&dib_tag=se&keywords=roller%2Bchain%2B40&qid=1738461187&sprefix=roller%2Bchain%2B40%2Caps%2C180&sr=8-6&th=1

[12] "uxcell 2pcs ANSI #40 / DIN(ISO)08A Roller Chain Idler Sprocket 15mm Bore." Amazon, https://www.amazon.com/uxcell-Sprocket-Hardened-Tensioner-Bearing/dp/B0CNSGX2RB?crid=26EP8PRTDG0FX&dib=eyJ2IjoiMSJ9.4c9I2pQ9tfO2Lx866RMSfdz5z2mSuC-57w3ttb1NQJc_gftIVww5ei_NFen8GUNK7IqGBktRlzv4RAQLhgpwD_BhKTr02bwZ0vOss12z6SLSxssfILlClr_NYwUASfboJJQQ9A9UjV76xlnAF7g3k40hlkzEQfnAe8nydV9bZRYab-jfyQrRuPwBtNHv9zu8uCVn_FaRFPyeDlW_NEflkOrLwo9B7QlaGGVAwGFtH30.zf7oUCfGfPOOeMfC5WzioXQ-isqOu5F2YZeZO3axWGo&dib_tag=se&keywords=%2340+roller+chain+sprocket+15mm+bore&qid=1738465023&sprefix=15mm+%2340+sp%2Caps%2C113&sr=8-3

[13] "Jeremywell #40 Roller Chain Sprocket B Type 1" Bore Hardened 12 Tooth." Amazon, https://www.amazon.com/Jeremywell-40BS12H-1-Tooth-Sprocket-Roller/dp/B08DDKLYMF?crid=3QXM1Q3Q259YY&dib=eyJ2IjoiMSJ9.eHq2qMWk_gU-Q967Zd8a4dwBOf81104aE_hJYjO19nVlbWbAyKQ2JhRfD4On6Q5A53D2RPeeQzwq6WTjKMb6ZyjPVFBzLiDF30BvHpBhNnQmUPTnslf6PutXO-K8toVb1maPpv7eSILN6kGG5RtihufMgbNn8ATkbKZI8vFtcjl3ldNYhrf72c4vu-rBffsur6KYLXLVoNCod7btfuJu4kYWYeAigeYV7_B_1Z66Vz9IBavoXvFOnCQ0CQxnlsdzJSz-Vo_Du1M4r9-nHMQcGfuq4umWL_19mGEwZHwdKHtxT1iqG1V9XwrUy_1ocLaYCtvtO6MRYZMRHrPex6O7ihuTTX1EydUTgT2vpaAFi-Y.KAHWSK25yG6iv_iKQTwQQRrhKl4P0uctOMVWdxHDrAg&dib_tag=se&keywords=%2340%2BRoller%2BChain%2BSprocket%2BB%2BType%2B1%27%27%2B12%2Btooth&qid=1738461979&s=industrial&sprefix=%2B40%2Broller%2Bchain%2Bsprocket%2Bb%2Btype%2B1%27%27%2B12%2Btooth%2Cindustrial%2C175&sr=1-4&th=1
