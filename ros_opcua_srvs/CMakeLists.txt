cmake_minimum_required(VERSION 3.5)
project(ros_opcua_srvs)
set(CMAKE_CXX_STANDARD 14)

find_package(message_generation REQUIRED)
find_package(ros_opcua_msgs REQUIRED)
find_package(std_msgs REQUIRED)
find_package(std_srvs REQUIRED)


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
  ${srv_files}
  DEPENDENCIES ros_opcua_msgs std_msgs std_srvs
)

ament_export_dependencies(
  message_runtime 
  ros_opcua_msgs 
  std_msgs 
  std_srvs
)
ament_package()

