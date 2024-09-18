^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Changelog for package talos_moveit_config
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

2.0.0 (2024-09-18)
------------------
* Merge branch 'ros2-migration' into 'humble-devel'
  ROS 2 Migration
  See merge request control/talos_moveit_config!8
* Remove moveit_fake_controller_manager dependency
* add moveit-ros-perception depend
* re-structure of the move_group launch files
* fix ros_controllers yaml file
* fix config files
* clean libraries moveit_rviz
* launch files
* licence and contributing
* config files
* migration of CMakeLists.txt and package.xml to ros2
* Contributors: Adrià Roig, Sai Kishor Kothakota, ileniaperrella

0.3.5 (2022-03-02)
------------------
* Merge branch 'add_flexibility' into 'dubnium-devel'
  Update related to hip flexibility in simulation
  See merge request control/talos_moveit_config!6
* Add robot_description argument to move_group launch file, and remap the /robot_description topic to this value
* Add flexibility joints as passive in the srdf
* Contributors: Pierre Fernbach, saikishor

0.3.4 (2021-11-17)
------------------
* Merge branch 'uedin_markers' into 'dubnium-devel'
  Disable collisions from the VICON markers to the adjacent links
  See merge request control/talos_moveit_config!5
* Disable collisions from the VICON markers to the adjacent links
* Disable collision pair between d435 and head_2_link
* Contributors: Adria Roig, Pierre Fernbach

0.3.3 (2020-07-02)
------------------
* Merge branch 'fix-right-leg-collision' into 'dubnium-devel'
  Fix collision between arm_right_7 and leg_right_3
  See merge request control/talos_moveit_config!4
* Fix collision between arm_right_7 and leg_right_3
* Contributors: Victor Lopez, victor

0.3.2 (2020-01-17)
------------------
* Merge branch 'moveit_fix' into 'dubnium-devel'
  fix moveit cartesian goals issue on robot
  See merge request control/talos_moveit_config!3
* fix moveit cartesian goals issue on robot
* Contributors: Sai Kishor Kothakota

0.3.1 (2019-11-28)
------------------
* Launch with moveit.rviz config by default
* Merge branch 'add_move_group_both_legs' into 'dubnium-devel'
  regenerated talos moveit config
  See merge request control/talos_moveit_config!2
* regenerated talos moveit config
* Contributors: Jordan Palacios, Luca Marchionni

0.2.6 (2018-04-13)
------------------
* Merge branch 'update-config' into 'dubnium-devel'
  regenerate talos srdf
  See merge request control/talos_moveit_config!1
* regenerate talos srdf
* Contributors: Hilario Tome, Victor Lopez

0.2.5 (2018-02-05)
------------------
* added uploading of collision blacklist
* Contributors: Hilario Tomé

0.2.4 (2017-08-18)
------------------
* added talos simple moveit controller manager
* Contributors: Hilario Tomé

0.2.3 (2016-11-11)
------------------
* Fix circular depenendency
* Merge branch 'dubnium-devel' of gitlab:control/talos_moveit_config into dubnium-devel
* Config tested on robot
* Contributors: Luca, Victor Lopez

0.2.2 (2016-11-09)
------------------
* 0.2.1
* Updated changelog
* Update moveit_config for Talos
* Created single torso group
* Added controller manageer controllers for torso and grippers
* Added more groups and controller manager configuration
* Contributors: Hilario Tome, Luca

* Update moveit_config for Talos
* Created single torso group
* Added controller manageer controllers for torso and grippers
* Added more groups and controller manager configuration
* Contributors: Hilario Tome, Luca

0.2.1 (2016-10-31)
------------------
* Iniitial commit
* Contributors: Hilario Tome
