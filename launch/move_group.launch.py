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

from typing import Dict
import os

from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument, OpaqueFunction
from launch.substitutions import LaunchConfiguration
from launch_ros.actions import Node
from moveit_configs_utils import MoveItConfigsBuilder
from launch_pal.arg_utils import read_launch_argument


def generate_launch_description():

    sim_time_arg = DeclareLaunchArgument(
        'use_sim_time', default_value='False', description='Use sim time'
    )

    use_sensor_manager_arg = DeclareLaunchArgument(name='use_sensor_manager',
                                                   default_value='False',
                                                   choices=['True', 'False'],
                                                   description='Use moveit_sensor_manager \
                                            for octomap')

    # Create the launch description and populate
    ld = LaunchDescription()
    ld.add_action(use_sensor_manager_arg)
    ld.add_action(sim_time_arg)

    # Execute move_group node
    ld.add_action(OpaqueFunction(function=launch_setup))

    return ld


def launch_setup(context, *args, **kwargs):

    use_sensor_manager = read_launch_argument("use_sensor_manager", context)

    robot_description_semantic = os.path.join(
        get_package_share_directory("talos_moveit_config"),
        "config/talos.srdf",
    )

    # Trajectory Execution Functionality
    moveit_simple_controllers_path = os.path.join(
        get_package_share_directory("talos_moveit_config"),
        "config/ros_controllers.yaml",
    )

    planning_scene_monitor_parameters = {
        "publish_planning_scene": True,
        "publish_geometry_updates": True,
        "publish_state_updates": True,
        "publish_transforms_updates": True,
    }

    use_sim_time = {
        'use_sim_time': LaunchConfiguration('use_sim_time')
    }

    moveit_config = (
        MoveItConfigsBuilder("talos")
        .robot_description_semantic(file_path=robot_description_semantic)
        .robot_description_kinematics(
            file_path=os.path.join("config", "kinematics_kdl.yaml")
        )
        .trajectory_execution(moveit_simple_controllers_path)
        .planning_pipelines(pipelines=["ompl"])
        .planning_scene_monitor(planning_scene_monitor_parameters)
        .pilz_cartesian_limits(
            file_path=os.path.join("config", "pilz_cartesian_limits.yaml")
        )
    )
    if use_sensor_manager:
        # moveit_sensors path
        moveit_sensors_path = "config/sensors_3d.yaml"
        moveit_config.sensors_3d(moveit_sensors_path)

    moveit_config.to_moveit_configs()

    # Start the actual move_group node/action server
    run_move_group_node = Node(
        package='moveit_ros_move_group',
        executable='move_group',
        output='screen',
        emulate_tty=True,
        parameters=[
            use_sim_time,
            moveit_config.to_dict(),
            {'publish_robot_description_semantic': True}
        ],
    )

    return [run_move_group_node]
