from setuptools import find_packages, setup
import os
from glob import glob

package_name = 'tennisbot'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        (os.path.join('share', package_name, 'config'), glob('config/*')),
        (os.path.join('share', package_name), glob('launch/*.launch.py'))
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='clbrady43',
    maintainer_email='clbrady43@tntech.edu',
    description='TODO: Package description',
    license='Apache-2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [ 
            'controller_node = tennisbot.controller_node:main',
            'lcd_node = tennisbot.lcd_node:main',
            'lidar_node = tennisbot.lidar_node:main',
            'motor_node = tennisbot.motor_node:main',
        ],
    },
)
