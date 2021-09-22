
cmake_minimum_required(VERSION 3.5)
project(ros_opcua_impl_python_opcua)
set(CMAKE_CXX_STANDARD 14)
# Find and load build settings from external packages
find_package(ament_cmake REQUIRED)
find_package(rosidl_default_generators REQUIRED)
find_package(builtin_interfaces REQUIRED)



################################################
## Declare ROS messages, services and actions ##
################################################
set(msg_files
  "msg/Address.msg"
  "msg/TypeValue.msg"
)

set(srv_files
  "srv/CallMethod.srv"
  "srv/Connect.srv"
  "srv/Disconnect.srv"
  "srv/ListNode.srv"
  "srv/Read.srv"
  "srv/Subscribe.srv"
  "srv/Unsubscribe.srv"
  "srv/Write.srv"
)

rosidl_generate_interfaces(${PROJECT_NAME}
  ${msg_files}
  ${srv_files}
  DEPENDENCIES builtin_interfaces
)

ament_export_dependencies(rosidl_default_runtime)
ament_package()


#############
## Testing ##
#############

if(BUILD_TESTING)
  find_package(ament_lint_auto REQUIRED)
  ament_lint_auto_find_test_dependencies()
endif()