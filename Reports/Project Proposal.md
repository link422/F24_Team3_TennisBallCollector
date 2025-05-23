# Tennis Ball Collector

## Team 3

ECE 4961-001 

### Introduction 

Tennis is a time-honored game that can be dated back to the 11th century, played by all ages all around the world. When you think of tennis you think of the intense competition, the player’s personalities, and the feeling in the of your favorite team winning. What is not talked about however is the cleanup process, after an intense match there is a lot of preparation that goes into getting the next match ready. When consulting the customer, they explained that their current tennis ball collecting method was outdated and broken. The main objective of this Capstone Design is to make improvements to the current Tennis Ball Collector by adding remote control capability and an accurate ball counter to help make the cleanup process more effective.  


### Formulating the Problem 

Collecting Tennis Balls at the end of a long day at practice is a daunting task for players who have been running for hours on end. Having to go and pick up each ball one by one is not only a waste of the players' time, but energy as well. To aid in this task, companies have created push devices that collect balls into a cart. While these devices provided a solution to the bigger problem, they raised concerns for more. After taking in many tennis balls, these machines can jam, halting the process. Along with that, these devices can move for their given purpose but cannot be easily transported from court to court. With teams having indoor and outdoor courts at different locations this is crucial.


### Specifications and Constraints

Specifications

1. The improved version of the tennis ball collector shall not be autonomous but will have improved features such as a ball counter, remote control capability, and a vibration mechanism to prevent jamming.

2. Any modifications to the tennis ball collector shall not impact its pre-existing performance of collecting and managing 50-100 balls at a time on indoor and outdoor courts.

3. Any modifications to the tennis ball collector shall not pose damage or injury risk to individuals, operators or property. 

4. The improved version of the tennis ball collector shall be cost-efficient with costs no more than 33% more than the customer’s alternative option, Playmate’s ball mower valued at $595 [1].

Constraints

1. If the design uses lithium ion batteries for powering the circuitry within the tennis ball collector, the batteries and its casing shall comply with 49 CFR 173.185 to prevent short-circuits,damage caused by the shifting of components within a device, and accidental activation of equipment. 

2. If using alkaline or dry cell batteries in the design, the modifications shall comply with the U.S. Hazardous Materials Regulations for dry cell batteries.
   
3. If the sensors implemented in the tennis ball collector operate at a radio frequency greater than 9kHz, the device shall comply with FCC part 15 under the classification of an unintentional radiator.

### Survey of Solutions 

On the market, there is an autonomous robotic tennis ball collector, called Tennibot [2]. That collects up to 40 balls a minute on clay courts, on the entire court including the net, fence, and corners, and it weighs approximately 25 lbs. However due to it's high price of $3,000, customers could have trouble committing to such a purchase. Tennis is already an expensive sport that should not require additional spendings to pick up tennis balls. There are other manual tennis ball collectors, such as Playmates Ball Mower [1], that are similar to Tennessee Tech's use of a collector. Although the price of the manual collector is cheaper sitting at $595, the quality reported by the customer can be lacking. With these different designs in mind, the project wants to combat the problem of pricing with the autonomous competitors. As well as, adding more quality to the collector compared to the manual competitors.

 
### Unknown obstacles 

The process of customizing computer chips for design and having the hardware behave functionally as expected. 

Response of the sensors of the counter to ensure foreign objects aren't counted. 

Potential damage to hardware applied to vehicle from differing weather conditions including but not limited to heavy rainfall, snow, and thunderstorms. 

Response of Software and Hardware to electromagnetic interference brought by other devices or external sources. 

### Measure of Success 

The project shall build upon the already established tennis ball collector used by Tennessee Tech. The project shall enhance the ball collector by making it remote controlled, adding a counter to ensure complete collection of balls, add a vibrating function to eliminate blockage, and add hinges to help with the mobility on different terrain. With consecutive testing of these 4 designs, the project shall be deemed successful by: Fully controllable with a remote, Compact effectiveness and mobility, the customer shall test the mobility by having the project being used during practice. Eliminating blockage, the customer shall test the vibrating function with actual tennis balls to see its effectiveness. Finally for adding a counter having different sensors to detect the difference of the balls and foreign objects shall provide effective results.

### Broader Implications/Ethics 
This project will act as a means of improving the current tennis team’s training efficiency, device accessibility, and facility maintenance. Globally, considering the demand for this product, it could contribute to resource depletion. Economically, this product could save TN Tech funding as we are modifying the existing model instead of purchasing a new one. From an environmental perspective, the process of designing our product could contribute to global waste and energy consumption. Socially, this product could create disparities between well-funded sports facilities and underprivileged communities. We are adament to developing a solution that is within health and safety regulations,  mindful of resource usage.  

### Resources 
To make a cost-effective, portable, remote controlled tennis ball collector efficient, it will take a solid understanding of remote controls and RF and knowledge of parts necessary for the robot. A processor that can handle multiple sensors such as infrared is needed for this robot. Lab equipment such as oscilloscopes and computers to interface with the processor will be needed. It is expected that it will take $1,000 dollars for prototyping to get the desired results. This number comes from the cost of all components mentioned above plus some extra because components may become damaged while working with them. This number comes from the cost of some components being added together with a small amount of overhead. Some of the more expensive components are the battery and charger which will range somewhere between $100-200 for a lithium-ion battery with high capacity, a raspberry-pi 5 is $80 dollars and we will also need a case and cables for it, and other various sensors together will cost around $200 dollars. This number will not be passed due to the individual components being used for prototyping being inexpensive for the most part. On top of prototyping costs, funding will be needed for CAD softwares and creating the finished build which will add at least $500 dollars based on softwares currently on the market so $1,500 will be enough to meet the customer’s needs.

| Part name  | Est. Price | Link |
| ------------- | ------------- | ------------- |
| RC transmitter  | 50-100  | N/A  |
| RC reciver  | 50-100  | N/A  |
| Arduino UNO R4   | 30  | [Click](https://store.arduino.cc/products/uno-r4-wifi )  | 
| Battery  | 30-50  | [Click](https://www.digikey.com/en/products/detail/adafruit-industries-llc/5035/14625568?s=N4IgjCBcoMw1oDGUBmBDANgZwKYBoQB7KAbRAHYYxyAGEAXQIAcAXKEAZRYCcBLAOwDmIAL4EALGABMCEMkjps%2BIqRAwAbAFYqmhszaROPAcJFiQMyGQy8WAC14BXALYACXoX4MRQA )  | 
| Charger   | 30-70  | [Click](https://www.digikey.com/en/products/filter/battery-chargers/85?s=N4IgjCBcoCxgTFUBjKAzAhgGwM4FMAaEAeygG0QBmANgFZKxaQBdIgBwBcoQBlDgJwCWAOwDmIAL4SiiSBSyCOAC0EBXALYACQcWGbkSjP1F5%2BLCUA )  | 
| LCD display   | 10  | [Click](https://www.digikey.com/en/products/detail/display-visions/EA-DOGM132L-5/4896710 )  | 
| Vibration motor   | 5-10  | [Click](https://www.digikey.com/en/products/detail/vybronics-inc/VZ4KC1B1051202/6009917 )  | 
| Wheels   | 50  | [Click](https://www.studica.com/studica-robotics-brand/125mm-all-terrain-wheel-set )  | 
| Servos   | 100  | [Click](https://www.digikey.com/en/products/detail/adafruit-industries-llc/1142/5154658 )  | 
| Sensors | 77 | [Click](https://stack-light.com/products/diffuse-photo-sensors?variant=44817176461531&currency=USD&gad_source=1&gclid=Cj0KCQjwjY64BhCaARIsAIfc7YZnyGzIxWyyUjUTWbqxsLxM_eVRJhUGIMK7RvBAOAtBdTkI59_Xu8YaAmwzEALw_wcB) |

### Personnel 

Carter Brady- Has worked with autonomous vehicle simulations including ROS. Has strong software background. 

Gabriel Dubose- Experience in working microcomputer processing, digital systems, Arduino coding  

Cindy Escobar- Experienced with object-oriented programming, a little RANCS autonomous vehicle programming, microcomputing, and digital systems. 

Tate Finley- Experienced with C/C++, Schematic design, and interest in recursive neural networks.  

Ashli Watkins- Previous work in object-oriented programming, computer networking, and circuit design/wiring 

Maxwell Wynne- Has experience with languages C/C++, python, and assembly. Also has experience with microcomputing and algorithms. 

 

### Timeline 

Initial meeting with stakeholder 09/12, declaring the first set of draft specifications 

Project Proposal Draft expected to be completed by September 16th 

Finalizing details with advisors and customers for proposal 

Project Proposal Final expected to be completed by September 30th 

Researching components that can be used for the design. 

Conceptual Design expected to be completed by October 28th 

Verifying theories of implementation of software and design with advisor and customer. 

Detailed Design expected to be completed by November 30th 

Final Presentation expected to be completed by November 30th 

The project will be done with the project by May 25th, 2025 

```mermaid
gantt
    title Timeline
    dateFormat  YYYY-MM-DD
    section Section
    Stakeholder meeting      :   2024-09-12, 1d
    Project proposal draft   :    2024-09-09, 7d
    Finalizing details with advisor and customer :  2024-09-12, 1d
    Project proposal final   :   2024-09-24, 7d
    Product research         :   2024-09-12, 30d
    Conceptual design        :   2024-10-01, 27d
    Detailed design          :   2024-10-28, 32d
    Final presentation       :   2024-10-28, 32d
``` 

### Contributions 

Carter Brady – Worked on resources, personnel, and timeline 

Maxwell Wynne – Worked on formulating the problem, personnel, and timeline 

Gabriel Dubose - Worked on Introduction, personnel, and timeline 

Tate Finley – Worked on sections ‘summarizing the problem,’ and ‘looking down the path to success’ including subsections. 

Ashli Watkins- Specification and Contributions, Timeline 

Cindy Escobar- Survey of Solutions, Personnel, Timeline 


 ### References

 [1] “Ball Mower 2.0,” PLAYMATE Tennis, https://www.playmatetennis.com/ball-mower-2/ (accessed Oct. 7,             2024). 

[2] “Tennibot ,” Tennibot, https://www.tennibot.com/buy/ (accessed Oct. 7, 2024). 

[3] “Arduino® Uno R4 WIFI,” Arduino Official Store, https://store.arduino.cc/products/uno-r4-wifi (accessed Oct. 7, 2024). 

[4] “5035,” DigiKey Electronics, https://www.digikey.com/en/products/detail/adafruit-industries-llc/5035/14625568?s=N4IgjCBcoMw1oDGUBmBDANgZwKYBoQB7KAbRAHYYxyAGEAXQIAcAXKEAZRYCcBLAOwDmIAL4EALGABMCEMkjps%2BIqRAwAbAFYqmhszaROPAcJFiQMyGQy8WAC14BXALYACXoX4MRQA (accessed Oct. 7, 2024).

[5] DigiKey - electronic components distributor, https://www.digikey.com/ (accessed Oct. 7, 2024). 

[6] “DigiKey Home,” DigiKey, https://www.digikey.com/ (accessed Oct. 7, 2024). 

[7] “EA DOGM132L-5,” DigiKey Electronics, https://www.digikey.com/en/products/detail/display-visions/EA-DOGM132L-5/4896710 (accessed Oct. 7, 2024). 

[8] “VZ4KC1B1051202,” DigiKey Electronics, https://www.digikey.com/en/products/detail/vybronics-inc/VZ4KC1B1051202/6009917 (accessed Oct. 7, 2024). 

[9] “125mm all-terrain robotics wheel set,” Studica, https://www.studica.com/studica-robotics-brand/125mm-all-terrain-wheel-set (accessed Oct. 7, 2024). 

[10] “Servos 1142,” DigiKey Electronics, https://www.digikey.com/en/products/detail/adafruit-industries-llc/1142/5154658 (accessed Oct. 7, 2024).

[11] “Photo sensors - diffuse,” Stack, https://stack-light.com/products/diffuse-photo-sensors?variant=44817176461531&currency=USD&gad_source=1&gclid=Cj0KCQjwjY64BhCaARIsAIfc7YZnyGzIxWyyUjUTWbqxsLxM_eVRJhUGIMK7RvBAOAtBdTkI59_Xu8YaAmwzEALw_wcB (accessed Oct. 7, 2024). 
