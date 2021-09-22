set(CMAKE_CXX_STANDARD 14)
cmake_minimum_required(VERSION 3.5)
project(ros_opcua_impl_python_opcua)

# Find and load build settings from external packages
find_package(ros_opcua_msgs REQUIRED)
find_package(ros_opcua_srvs REQUIRED)
find_package(ament_cmake REQUIRED)
find_package(rosidl_default_generators REQUIRED)


################################################
## Declare ROS messages, services and actions ##
################################################


###########
## Build ##
###########


#############
## Install ##
#############


#############
## Testing ##
#############

if(BUILD_TESTING)
  find_package(ament_lint_auto REQUIRED)
  ament_lint_auto_find_test_dependencies()
endif()