from glob import glob
from setuptools import setup

package_name = 'patrol_robot'

setup(
    name=package_name,
    version='0.0.1',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages', ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        ('share/' + package_name + '/launch', glob('launch/*.py')),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='you',
    maintainer_email='you@example.com',
    description='Patrol robot project',
    license='MIT',
    entry_points={
        'console_scripts': [
            'patrol_node = patrol_robot.patrol_node:main',
            'obstacle_monitor = patrol_robot.obstacle_monitor:main',
        ],
    },
)
