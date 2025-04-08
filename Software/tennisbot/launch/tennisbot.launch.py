from launch import LaunchDescription
from launch_ros.actions import Node


def generate_launch_description():
    return LaunchDescription([
        Node(
            package='tennisbot',
            namespace='tennisbot',
            executable='controller_node',
            name='controller_node'
        ),
        Node(
            package='tennisbot',
            namespace='tennisbot',
            executable='lcd_node',
            name='lcd_node'
        ),
        Node(
            package='tennisbot',
            namespace='tennisbot',
            executable='lidar_node',
            name='lidar_node'
        ),
        Node(
            package='tennisbot',
            namespace='tennisbot',
            executable='motor_node',
            name='motor_node'
        )
    ])
