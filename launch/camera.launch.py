import os

from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='realsense2_camera',
            executable='realsense2_camera_node',
            output='screen',
            namespace='camera',
            parameters=[{
                'align_depth': True,
                'enable_pointcloud': False,
                'enable_sync': True,
                'color_width': 640,
                'color_height': 480,
                'depth_width': 640,
                'depth_height': 480,
                'infra_width': 640,
                'infra_height': 480,
                'color_fps': 30,
                'depth_fps': 30,
                'infra_fps': 30
            }],
            remappings=[('/camera/color/image_raw', '/camera/image_color')]
        )
    ])
