# Copyright (c) 2024 PAL Robotics S.L. All rights reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import os
from typing import Dict
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument, OpaqueFunction
from launch.substitutions import LaunchConfiguration
from launch_pal.arg_utils import read_launch_argument

from launch_ros.actions import Node
from moveit_configs_utils import MoveItConfigsBuilder


def launch_setup(context, *args, **kwargs):

    robot_description_semantic = os.path.join(
        get_package_share_directory("talos_moveit_config"),
        "config/talos.srdf",
    )
    # Trajectory Execution Functionality
    moveit_simple_controllers_path = os.path.join(
        get_package_share_directory("talos_moveit_config"),
        "config/ros_controllers.yaml",
    )

    use_sim_time = {
        'use_sim_time': LaunchConfiguration('use_sim_time')
    }

    # The robot description is read from the topic /robot_description if the parameter is empty
    moveit_config = (
        MoveItConfigsBuilder("talos")
        .robot_description_semantic(file_path=robot_description_semantic)
        .robot_description_kinematics(
            file_path=os.path.join("config", "kinematics_kdl.yaml")
        )
        .trajectory_execution(moveit_simple_controllers_path)
        .planning_pipelines(pipelines=["ompl"])
        .pilz_cartesian_limits(
            file_path=os.path.join("config", "pilz_cartesian_limits.yaml")
        ).to_moveit_configs()
    )

    # RViz
    rviz_base = os.path.join(get_package_share_directory(
        'talos_moveit_config'), 'config')
    rviz_full_config = os.path.join(rviz_base, 'moveit.rviz')
    rviz_node = Node(
        package='rviz2',
        executable='rviz2',
        output='log',
        arguments=['-d', rviz_full_config],
        emulate_tty=True,
        parameters=[
            use_sim_time,
            moveit_config.robot_description,
            moveit_config.robot_description_semantic,
            moveit_config.planning_pipelines,
            moveit_config.robot_description_kinematics,
        ],
    )

    return [rviz_node]


def generate_launch_description():

    sim_time_arg = DeclareLaunchArgument(
        'use_sim_time', default_value='False', description='Use sim time'
    )
    ld = LaunchDescription()

    ld.add_action(sim_time_arg)
    ld.add_action(OpaqueFunction(function=launch_setup))

    return ld
