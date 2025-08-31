ROS 2 SLAM Robot Simulation

A differential drive robot simulation with SLAM in Gazebo using ROS 2 Jazzy.
The robot supports teleoperation, mapping, and localization via slam_toolbox
.

Prerequisites

ROS 2 Jazzy

slam_toolbox

Gazebo Harmonic

gazebo_ros_pkgs (Gazebo-ROS bridge)

twist_mux (multiplex multiple velocity sources)

twist_stamper (adds timestamp to twist messages)

teleop_twist_keyboard (for manual control)

Build & Setup

Clone the repository into your ROS 2 workspace:

mkdir -p ~/ros2_ws/src
cd ~/ros2_ws/src
git clone git@github.com:SelvaDinesh2003/ros2-slam-simulation.git
cd ~/ros2_ws
colcon build --symlink-install
source install/setup.bash

Running the Simulation

Launch the robot in Gazebo:

ros2 launch robot simulation.launch.py


This will spawn the differential drive robot in Gazebo.

To control the robot via keyboard:

Open a new terminal and source your workspace:

source ~/ros2_ws/install/setup.bash


Run the teleop node:

ros2 run teleop_twist_keyboard teleop_twist_keyboard


Use your keyboard to drive the robot in Gazebo.

Running SLAM

Source your workspace in a new terminal:

source ~/ros2_ws/install/setup.bash

Online Mapping (recommended)
ros2 launch robot simulation.launch.py use_slam_option:=online_async_slam

Localization with Prebuilt Map
ros2 launch robot simulation.launch.py use_slam_option:=mapper_params_localization

Notes

Make sure to source your workspace in every new terminal before running any ROS 2 commands.

You can switch between mapping and localization using the use_slam_option launch argument.

For smoother operation, ensure gazebo_ros_pkgs and slam_toolbox are properly installed and compatible with ROS 2 Jazzy.
