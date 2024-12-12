# Detailed Design

## Function of the Subsystem

The Vibration Subsystem prevents tennis ball jams by utilizing dual DC vibration motors that generate targeted oscillations to dislodge stuck tennis balls, ensuring uninterrupted operation of the Playmate Tennis Ball Collector [1]. It interfaces with the RC Control System, enabling remote activation and deactivation for enhanced adaptability and user convenience. Powered by a shared rechargeable Lithium Battery, the subsystem integrates seamlessly with other components, maintaining efficient power distribution and operational harmony. Its design incorporates robust power integration, remote control capabilities, and environmental safeguards, ensuring longevity, reliability, and enhanced overall functionality of the collector.

## Specifications and Constraints

- The vibration subsystem shall use Vybronics DC Vibration Motors.
  - Rationale: Compact and lightweight with sufficient vibration force (1.3 G), aligning with system requirements.

- The vibration motors shall operate at 3.0 V DC with a current draw of approximately 60 mA per motor.
  - Rationale: Operating at the motor’s rated specifications ensures reliable performance and prevents premature wear or failure due to overvoltage 
or excessive current.

- The vibration motors shall be powered by the shared Lithium Battery from the Power Subsystem.
  - Rationale: Using the shared power source simplifies design by reducing the need for additional batteries, minimizing weight, and ensuring consistent power delivery across all subsystems for seamless integration.

- The motors shall be activated using lever-actuated switches and can be controlled remotely.
  - Rationale:  Lever-actuated switches offer mechanical durability, reliable activation, and easy integration with the collector system. Remote control functionality adds user convenience and operational flexibility, allowing the motors to start and stop without manual intervention.

- The subsystem shall comply with relevant safety standards, such as 49 CFR 173.185, to ensure safe handling and operation of lithium batteries.
  - Rationale: Minimizes risks to users and the system during operation.

- The vibration subsystem shall undergo tests alongside the power subsystem to ensure compatibility and stability.
  - Rationale: Verifies subsystem integration and prevents issues related to simultaneous operation.


## Overview of Proposed Solution

The proposed Vibration Subsystem comprises two Vybronics DC Vibration Motors (VZ4KC1B1051202) [2] strategically mounted on opposite sides of the tennis ball collector to mitigate jamming effectively. Power is supplied by the shared Lithium Polymer Battery from the Power Subsystem, ensuring streamlined integration and consistent energy delivery. The motors are engaged via durable lever-actuated switches (JANDECCN V-153-1C25) [3], which offer robust performance and intuitive operation within the collector’s mechanical framework. Additionally, the motors can be remotely controlled to start and stop, enhancing user convenience and operational flexibility. The long lever arms of the switches eliminate the need for additional protective overlays, simplifying the design while minimizing maintenance requirements.

This subsystem is designed to be efficient, cost-effective, and seamlessly compatible with other components. It complies with safety standards and delivers reliable performance without disrupting other functions, such as ball scanning or the operation of RC motors.

## Interface with Other Subsystems

The Vibration Subsystem interfaces closely with the Power Subsystem by utilizing the shared Lithium Battery as its primary power source. This connection ensures compatibility and minimizes the need for additional power components. The subsystem is carefully calibrated to avoid interference with the Sensor Subsystem, ensuring that vibrations do not disrupt the accuracy of ball scanning or detection. Additionally, the vibration motors can be manually activated via lever-actuated switches or remotely controlled through the RC and Control Subsystems, allowing precise operation and quick responses to jamming scenarios. This dual activation mechanism enhances user flexibility and ensures seamless coordination with the RC Subsystem's broader control functionalities.

The integration of the RC Subsystem enables centralized control of the vibration motors, simplifying the operational workflow while maintaining non-disruptive functionality. This cohesive design allows the Vibration Subsystem to perform its function effectively, addressing jamming issues, while maintaining overall system stability, efficiency, and compatibility with other subsystems.


## Printed Circuit Board Layout
![PCB Mount](https://github.com/user-attachments/assets/dbda3a5c-661a-4333-b582-1860a208ab72)

![product specification](https://github.com/user-attachments/assets/2631ed9b-7ddf-4376-9867-24294a29ae83)



## Operational Flowchart

![Screenshot 2024-12-11 034838](https://github.com/user-attachments/assets/3f87c6a7-b8f5-459e-955b-95057b11cb5e)

## BOM

![Screenshot 2024-11-30 091017](https://github.com/user-attachments/assets/a5299c18-9f1b-4f16-b977-1058372fee9b)


## Analysis

The Vibration Subsystem design presents a plausible and testable solution to mitigate tennis ball jams in the Playmate Tennis Ball Collector by employing dual Vybronics DC Vibration Motors. These motors generate sufficient vibration force to dislodge jammed balls without risking structural damage. While the effectiveness of vibration in resolving jamming is not guaranteed for all scenarios, it is a well-considered approach grounded in the understanding that oscillatory motion can disrupt static friction and free-wedged objects. The design incorporates flexible activation mechanisms—manual lever-actuated switches and RC control—to allow for precise, on-demand usage and adaptability in varying operational conditions.

The subsystem’s integration with the shared Lithium Battery from the Power Subsystem ensures simplicity, cost-efficiency, and reduced weight while maintaining reliable power delivery. The durable lever-actuated switches enhance mechanical compatibility and eliminate the need for overlays, streamlining the design. Extensive testing and calibration will be conducted to validate the vibration’s effectiveness in addressing jamming while ensuring seamless compatibility with the Sensor and RC Subsystems. This iterative process allows for refinement, ensuring the subsystem contributes to the machine's overall functionality, stability, and efficiency.

## References

[1] “Ball Mower 2.0,” PLAYMATE Tennis, https://www.playmatetennis.com/ball-mower-2/  
[2] VZ4KC1B1051202 Vybronics Inc, https://www.digikey.com/en/products/detail/vybronics-inc/VZ4KC1B1051202/6009917    
[3] JANDECCN V-153-1C25, Amazon, https://www.amazon.com/JANDECCN-Switch-Straight-Action-V-153-1C25/dp/B09SWCJ8FF 

