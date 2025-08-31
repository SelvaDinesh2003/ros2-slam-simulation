# ROS 2 SLAM Robot Simulation

A **differential drive robot** simulation with SLAM in Gazebo using **ROS 2 Jazzy**.  
The robot supports **teleoperation**, **mapping**, and **localization** via [slam_toolbox](https://github.com/SteveMacenski/slam_toolbox).

---

## Prerequisites

- **ROS 2 Jazzy**  
- **slam_toolbox**  
- **Gazebo Harmonic**  
- `gazebo_ros_pkgs` (Gazebo-ROS bridge)  
- `twist_mux` (multiplex multiple velocity sources)  
- `twist_stamper` (adds timestamp to twist messages)  
- `teleop_twist_keyboard` (for manual control)

---

## Build & Setup

Clone the repository into your ROS 2 workspace:

Run: `mkdir -p ~/ros2_ws/src`  
Then: `cd ~/ros2_ws/src`  
Clone the repo: `git clone git@github.com:SelvaDinesh2003/ros2-slam-simulation.git`  
Go to workspace: `cd ~/ros2_ws`  
Build: `colcon build --symlink-install`  
Source the workspace: `source install/setup.bash`

---

## Running the Simulation

Launch the robot in Gazebo: `ros2 launch robot simulation.launch.py`

---

## Teleoperation (Keyboard Control)

Open a **new terminal**, source your workspace: `source ~/ros2_ws/install/setup.bash`  
Run the teleop node: `ros2 run teleop_twist_keyboard teleop_twist_keyboard`

Use your keyboard to drive the robot in Gazebo.

---

## Running SLAM

Source your workspace in a new terminal: `source ~/ros2_ws/install/setup.bash`

### 1. Online Mapping (recommended)

Run: `ros2 launch robot simulation.launch.py use_slam_option:=online_async_slam`

### 2. Localization with Prebuilt Map

Run: `ros2 launch robot simulation.launch.py use_slam_option:=mapper_params_localization`

---

## Notes

- Always **source your workspace** in each new terminal before running ROS 2 commands.  
- Use the `use_slam_option` argument to switch between **mapping** and **localization**.  
- Ensure `gazebo_ros_pkgs` and `slam_toolbox` are installed and compatible with ROS 2 Jazzy.  
- All commands are inline using backticks so users can copy them easily.

