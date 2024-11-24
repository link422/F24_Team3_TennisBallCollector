# Detailed Design for Counting Display

## Function of the Counting Display Subsystem

The Counting Display Systems section shall implement a LCD Display that will display the amount of collected tennis balls.


## Specifications and Constraints

The LCD display shall use Serial Communication to communicate with the Counting Sensor and Raspberry Pi components.
The subsystem shall display an accurate account of collected balls throughout the entire collection process.
The LCD display shall be connected to a circuit that supplies the required voltage of approximately 3.3V to the LCD display.


## Overview of Proposed Solution

This subsystem shall display the amount of tennis balls collected as a numerical value. This subsystem also encompasses coding scripts that will interface with the LCD display. 


## Interface with Other Subsystems

Provide detailed information about the inputs, outputs, and data transferred to other subsystems. Ensure specificity and thoroughness, clarifying the method of communication and the nature of the data transmitted.


## 3D Model of Custom Mechanical Components

There are no mechanical components in this subsystem.


## Buildable Schematic 

Integrate a buildable electrical schematic directly into the document. If the diagram is unreadable or improperly scaled, the supervisor will deny approval. Divide the diagram into sections if the text and components seem too small.

The schematic should be relevant to the design and provide ample details necessary for constructing the model. It must be comprehensive so that someone, with no prior knowledge of the design, can easily understand it. Each related component's value and measurement should be clearly mentioned.


## Printed Circuit Board Layout

Entire PCB.


## Operational Flowchart

For sections including a software component, produce a chart that demonstrates the decision-making process of the microcontroller. It should provide an overview of the device's function without exhaustive detail.


## BOM

A complete list of all components needed for the design must be given with the cost of each component and the total cost of the subsystem. The BOM should be a markdown table. Make sure to to provide the manufacteror, part number, distributor, distributor part number, quantity, and price. Also provide a url where the product can be purchased from. If the componenet is refernced on your schematic make sure to include the component name.

Provide a comprehensive list of all necessary components along with their prices and the total cost of the subsystem. This information should be presented in a tabular format, complete with the manufacturer, part number, distributor, distributor part number, quantity, price, and purchasing website URL. If the component is included in your schematic diagram, ensure inclusion of the component name on the BOM (i.e R1, C45, U4).

## Analysis

Deliver a full and relevant analysis of the design demonstrating that it should meet the constraints and accomplish the intended function. This analysis should be comprehensive and well articulated for persuasiveness.

## References

[1] "EA DOGM132L-5," DigiKey Electronics, <https://www.digikey.com/en/products/detail/display-visions/EA-DOGM132L-5/4896710> (accessed Nov. 4, 2024). 

[2] "DOGM132 GRAPHIC,"  DigiKey Electronics, <https://www.lcd-module.de/eng/pdf/grafik/dogm132-5e.pdf> (accessed Nov. 19, 2024).

[3] "EA DOGM162W-A," DigiKey Electronics, <https://www.digikey.com/en/products/detail/display-visions/EA-DOGM162W-A/4896717?s=N4IgTCBcDaIKIEEAEARA8gcQLIEYBsYA6gLQIgC6AvkA> (accessed Nov. 24, 2024).

[4] "DOG series 3.3V," DigiKey Electronics, <https://www.lcd-module.de/eng/pdf/doma/dog-me.pdf> (accessed Nov. 24, 2024).

[5] "ST7036_EA_DOGM_Python_driver_plain.py" <https://www.lcd-module.com/fileadmin/html-seiten/deu/disk/development-service/Raspberry/ST7036_EA_DOGM_Python_driver_plain.py> (accessed Nov. 23, 2024).

[6] "Control a HD44780 LCD display via I2C with the Raspberry Pi" <https://tutorials-raspberrypi.com/control-a-raspberry-pi-hd44780-lcd-display-via-i2c/> (accessed Nov. 23, 2024).

[7] "Basic 16x2 Character LCD - Black on Green," Sparkfun, <https://www.sparkfun.com/products/255> (accessed Nov. 24, 2024).

[8] "HD44780U (LCD-II)," Sparkfun, <https://www.sparkfun.com/datasheets/LCD/HD44780.pdf> (accessed Nov. 24, 2024).

[9] "Arduino Display Interface" Amazon, <https://www.amazon.com/JANSANE-Arduino-Display-Interface-Raspberry/dp/B07D83DY17/ref=sr_1_18?adgrpid=1340305246769769&dib=eyJ2IjoiMSJ9.KForF0owAe67XDG8YMDcslAoBQE-22v5eSGkrAqNaagka8eYdQFb4Inb_TGtD3NxRcDPTJZMwSl3CCEAoDZkLUL7VGEIqbh7dUtcCLQ7RcQPL0_MUAk80VSzdCEG6yt1_8VDvR9V8bamJIndqjU6v2sHOYExJck5NwHhn5nhua3RWxtZPgSW2uHkna4ojTbBaIf_B9q1EfGQs1Y-IgaQ89n7GYYjCOpJBfbYZhWxWdI.VB7rdWt6ogCv0fKAzrzrQZ7aP5_I1_HFryDEM8fUEpU&dib_tag=se&hvadid=83769464201946&hvbmt=be&hvdev=c&hvlocphy=84181&hvnetw=o&hvqmt=e&hvtargid=kwd-83769441278522%3Aloc-190&hydadcr=24660_13770028&keywords=i2c+lcd+adapter&msclkid=302b2dd59fb41237af8b4a96e06373ae&qid=1732476931&sr=8-18> (accessed Nov. 24, 2024).
