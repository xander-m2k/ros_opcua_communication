cmake_minimum_required(VERSION 3.5)
project(ros_opcua_msgs)
set(CMAKE_CXX_STANDARD 14)

find_package(ament_cmake REQUIRED)
find_package(std_msgs REQUIRED)
find_package(message_generation REQUIRED)

set(msg_files
  "msg/Address.msg"
  "msg/TypeValue.msg"
)

rosidl_generate_interfaces(
  ${msg_files}
  DEPENDENCIES std_msgs
)

ament_export_dependencies(
  message_runtime 
  std_msgs
)
ament_package()
