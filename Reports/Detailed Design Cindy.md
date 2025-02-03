# Detailed Design

## Function of the Subsystem

The Vibration Subsystem prevents tennis ball jams by utilizing dual DC vibration motors that generate targeted oscillations to dislodge stuck tennis balls, ensuring uninterrupted operation of the Playmate Tennis Ball Collector [1]. It interfaces with the RC Control System, enabling remote activation and deactivation for enhanced adaptability and user convenience. Powered by a shared rechargeable Lithium Battery, the subsystem integrates seamlessly with other components, maintaining efficient power distribution and operational harmony. The design incorporates robust power integration, remote control capabilities, and environmental safeguards, ensuring longevity, reliability, and enhanced overall functionality of the collector.

## Specifications and Constraints

- The vibration subsystem shall use Vybronics DC Vibration Motors.
  - Rationale: Compact and lightweight with sufficient vibration force (1.3 G), aligning with system requirements.

- The vibration motors shall operate at 3.0 V DC with a current draw of approximately 60 mA per motor.
  - Rationale: Operating at the motor’s rated specifications ensures reliable performance and prevents premature wear or failure due to overvoltage 
or excessive current.

- The vibration motors shall be powered by the shared Lithium Battery from the Power Subsystem.
  - Rationale: Using the shared power source simplifies design by reducing the need for additional batteries, minimizing weight, and ensuring consistent power delivery across all subsystems for seamless integration.

- The motors shall be activated using a SunFounder 2-Channel 5V Relay Module, controlled remotely by the RC Subsystem.
  - Rationale:  The relay module enables reliable and efficient switching of the vibration motors when commanded by the controller, providing remote activation and deactivation.

- The subsystem shall comply with relevant safety standards, such as 49 CFR 173.185, to ensure safe handling and operation of lithium batteries.
  - Rationale: Minimizes risks to users and the system during operation.

- The vibration subsystem shall undergo tests alongside the power subsystem to ensure compatibility and stability.
  - Rationale: Verifies subsystem integration and prevents issues related to simultaneous operation.


## Overview of Proposed Solution

The proposed Vibration Subsystem comprises two Vybronics DC Vibration Motors (VZ4KC1B1051202) [2] strategically mounted on opposite sides of the tennis ball collector to mitigate jamming effectively. Power is supplied by the shared Lithium Polymer Battery from the Power Subsystem, ensuring streamlined integration and consistent energy delivery.

The motors are activated through a SunFounder 2-Channel 5V Relay Module [3], which the RC Subsystem controls. This relay module allows the vibration motors to be switched on or off remotely based on user commands from the controller. The relay ensures that the motors only activate when necessary, reducing power consumption and wear on the components.

This subsystem is designed to be efficient, cost-effective, and seamlessly compatible with other components. It complies with safety standards and delivers reliable performance without disrupting other functions, such as ball scanning or the operation of RC motors.


## Interface with Other Subsystems

The Vibration Subsystem interfaces closely with the Power Subsystem by utilizing the shared Lithium Battery as its primary power source. This connection ensures compatibility and minimizes the need for additional power components. The subsystem is carefully calibrated to avoid interference with the Sensor Subsystem, ensuring that vibrations do not disrupt the accuracy of ball scanning or detection.

The vibration motors are activated through the SunFounder Relay Module, which controls the RC Subsystem and the Raspberry Pi. When the controller sends a command, the relay switches on, allowing power to flow to the motors. This setup provides precise operation and quick responses to jamming scenarios while eliminating mechanical wear issues associated with lever-actuated switches.

The integration of the RC Subsystem enables centralized control of the vibration motors, simplifying the operational workflow while maintaining non-disruptive functionality. This cohesive design allows the Vibration Subsystem to perform its function effectively, addressing jamming issues while maintaining overall system stability, efficiency, and compatibility with other subsystems.

## Printed Circuit Board Layout
![PCB Mount](https://github.com/user-attachments/assets/dbda3a5c-661a-4333-b582-1860a208ab72)

![product specification](https://github.com/user-attachments/assets/2631ed9b-7ddf-4376-9867-24294a29ae83)



## Operational Flowchart

![image](https://github.com/user-attachments/assets/a773d65e-81e3-4c40-ac82-f4bbc640da97)



## BOM

![image](https://github.com/user-attachments/assets/0bf4446b-4700-42db-9c30-ab274c3db986)


## Analysis

The Vibration Subsystem design offers a potential solution to reduce tennis ball jams in the Playmate Tennis Ball Collector by utilizing dual Vybronics DC Vibration Motors. These motors are chosen based on their ability to generate sufficient vibration forces that could dislodge jammed balls without risking damage to the structure. While the system's theoretical basis—using vibration to disrupt static friction and release wedged objects—appears promising, further testing is necessary to determine its effectiveness under real-world conditions. The system is designed with flexibility in mind, featuring a remote-controlled activation mechanism that eliminates concerns over mechanical wear and ensures seamless integration with the RC and Raspberry Pi subsystems. The shared Lithium Battery contributes to overall system efficiency, reducing weight and maintaining cost-effectiveness, while the relay ensures motor activation occurs only when necessary.

Although initial calculations and system design suggest that the vibration motors should be appropriately sized for the tennis collector, confirmation of their adequacy in practice will be determined through future testing. Additionally, the design takes into account the conditions under which tennis balls typically become jammed—when multiple balls try to exit simultaneously or due to the speed of the tennis collector mechanism. Extensive testing and calibration will be conducted to assess the system’s performance, with adjustments made as needed to optimize the vibration's effect on ball jams and ensure compatibility with other subsystems. This iterative testing process will refine the subsystem, contributing to the overall functionality, stability, and efficiency of the Playmate Tennis Ball Collector.

## References

[1] “Ball Mower 2.0,” PLAYMATE Tennis, https://www.playmatetennis.com/ball-mower-2/  
[2] VZ4KC1B1051202 Vybronics Inc, https://www.digikey.com/en/products/detail/vybronics-inc/VZ4KC1B1051202/6009917    
[3] SunFounder 2-Channel 5V Relay Module, https://www.amazon.com/SunFounder-Channel-Optocoupler-Expansion-Raspberry/dp/B00E0NTPP4

