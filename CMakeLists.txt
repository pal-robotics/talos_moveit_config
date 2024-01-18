cmake_minimum_required(VERSION 3.8)
project(talos_moveit_config)

find_package(ament_cmake_auto REQUIRED)

ament_auto_find_build_dependencies()

# Install the moveit setup assistant to avoid some warnings when launching move_group
install(FILES
    .setup_assistant
    DESTINATION share/${PROJECT_NAME}
)

ament_auto_package(INSTALL_TO_SHARE)

