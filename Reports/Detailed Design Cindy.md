# Detailed Design

## Function of the Subsystem

The function of the Vibration Subsystem is to prevent tennis ball jamming by utilizing dual DC vibration motors to induce targeted vibrations. These vibrations help dislodge jammed tennis balls from the collection system, ensuring uninterrupted operation of the Playmate Tennis Ball Collector [1]. This subsystem is powered by a shared rechargeable Lithium Battery and integrates seamlessly with other components for efficient functionality. Proper integration of power and environmental protection ensures the longevity and reliability of the vibration subsystem.

## Specifications and Constraints

- The vibration subsystem shall use Vybronics DC Vibration Motors (VZ4KC1B1051202)[2].
  - Rationale: Compact and lightweight with sufficient vibration force (1.3 G), aligning with system requirements.

- The vibration motors shall operate at 3.0 V DC with a current draw of approximately 60 mA per motor.
  - Rationale: Operating at the motor’s rated specifications ensures reliable performance and prevents premature wear or failure due to overvoltage 
or excessive current.

- The vibration motors shall be powered by the shared 3.7 V Lithium Battery from the Power Subsystem.
  - Rationale: Using the shared power source simplifies design by reducing the need for additional batteries, minimizes weight, and ensures consistent power delivery across all subsystems for seamless integration.

- The motors shall be activated using lever-actuated switches (JANDECCN V-153-1C25) [3].
  - Rationale:  Lever-actuated switches offer mechanical durability, reliable activation, and easy integration with the collector system. Their long lever arms are suitable for engaging the motors during mechanical operation without requiring additional protection overlays.

- The subsystem shall comply with relevant safety standards, such as 49 CFR 173.185, to ensure safe handling and operation of lithium batteries.
  - Rationale: Minimizes risks to users and the system during operation.

- The vibration subsystem shall undergo vibration tests alongside the power subsystem to ensure compatibility and stability.
  - Rationale: Verifies subsystem integration and prevents issues related to simultaneous operation.


## Overview of Proposed Solution

The proposed Vibration Subsystem consists of two Vybronics DC Vibration Motors mounted on opposite sides of the tennis ball collector to address jamming. Power is supplied through the shared Lithium Polymer Battery from the Power Subsystem. The motors are activated via lever-actuated switches (JANDECCN V-153-1C25), which offer enhanced durability and ease of operation within the collector’s mechanical structure. The long lever arms of the switches eliminate the need for additional overlays, simplifying design and reducing maintenance requirements.

This solution is efficient, cost-effective, and integrates seamlessly with other subsystems. It adheres to safety standards and ensures consistent performance without interfering with other operations, such as ball scanning or RC motor functions.

## Interface with Other Subsystems

The Vibration Subsystem interfaces closely with the Power Subsystem by utilizing the shared 3.7V Lithium Battery as its primary power source. This connection ensures compatibility and minimizes the need for additional power components. The subsystem is carefully calibrated to avoid interference with the Sensor Subsystem, ensuring that vibrations do not disrupt the accuracy of ball scanning or detection. Additionally, the manual activation of the vibration motors via lever-actuated switches is designed to operate independently from the RC and Control Subsystems, ensuring non-disruptive functionality. This seamless integration with other subsystems allows the Vibration Subsystem to perform its function effectively while maintaining overall system stability and efficiency.


## Printed Circuit Board Layout
![PCB Mount](https://github.com/user-attachments/assets/dbda3a5c-661a-4333-b582-1860a208ab72)

![product specification](https://github.com/user-attachments/assets/2631ed9b-7ddf-4376-9867-24294a29ae83)



## Operational Flowchart

![Professional_Vibration_Subsystem_Flowchart](https://github.com/user-attachments/assets/262fefb3-5d19-4b54-9843-88b6941b6d99)


## BOM

![Screenshot 2024-11-30 091017](https://github.com/user-attachments/assets/a5299c18-9f1b-4f16-b977-1058372fee9b)


## Analysis

The Vibration Subsystem design provides an efficient and reliable solution for preventing tennis ball jams in the Playmate Tennis Ball Collector by utilizing dual Vybronics DC Vibration Motors, delivering sufficient vibration force without causing structural damage. Powered by the shared Lithium Battery from the Power Subsystem, the design simplifies integration, minimizes cost and weight, and replaces press-button switches with durable lever-actuated switches for increased reliability and mechanical compatibility. These switches eliminate the need for additional overlays and provide straightforward activation through mechanical engagement. Careful testing and calibration will verify the subsystem’s effectiveness, ensuring compatibility with the Sensor and RC Subsystems and preventing interference with ball detection processes. This well-balanced design achieves seamless integration, cost-efficiency, and robust performance, contributing to the overall functionality and stability of the machine.

## References

[1] “Ball Mower 2.0,” PLAYMATE Tennis, https://www.playmatetennis.com/ball-mower-2/  
[2] VZ4KC1B1051202 Vybronics Inc, https://www.digikey.com/en/products/detail/vybronics-inc/VZ4KC1B1051202/6009917    
[3] JANDECCN V-153-1C25, Amazon, https://www.amazon.com/JANDECCN-Switch-Straight-Action-V-153-1C25/dp/B09SWCJ8FF 

