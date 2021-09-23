import os
import sys

import launch
import launch_ros.actions
from ament_index_python.packages import get_package_share_directory


def generate_launch_description():
    ld = launch.LaunchDescription([
        launch_ros.actions.Node(
            package='ros_opcua_impl_python_opcua',
            executable='ros_server.py',
            name='rosopcua',
            output='screen',
            parameters=[
                get_package_share_directory(
                    'ros_opcua_impl_python_opcua') + '/config/params.yaml'
            ]
        )
    ])
    return ld


if __name__ == '__main__':
    generate_launch_description()
