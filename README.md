# ROS 2 SLAM Robot Simulation 🤖

A differential drive robot simulation with SLAM in Gazebo using **ROS 2 Jazzy**. 
The robot can be teleoperated and supports both **mapping** and **localization** using `slam_toolbox`.

---

---

## ⚡ Requirements

Make sure the following are installed:

- [ROS 2 Jazzy](https://docs.ros.org/en/jazzy/Installation.html)  
- [slam_toolbox](https://github.com/SteveMacenski/slam_toolbox)  
- [Gazebo Harmonic](https://gazebosim.org/docs/harmonic)  
- `gazebo_ros_pkgs` (for Gazebo-ROS bridge)  
- `twist_mux` (multiplex multiple velocity sources)  
- `twist_stamper` (adds timestamp to twist messages)  

---

## 🚀 Build & Setup

Clone the repo into your ROS 2 workspace:
```bash
mkdir -p ~/ros2_ws/src
cd ~/ros2_ws/src
git clone https://github.com/<your-username>/ros2-slam-simulation.git
cd ~/ros2_ws
colcon build --symlink-install
source install/setup.bash
▶️ Running the Simulation
1. Launch robot in Gazebo
ros2 launch robot simulation.launch.py


👉 This will spawn the differential drive robot inside Gazebo.
👉 Control it with teleop key in another terminal.

🗺️ Running SLAM

Open a new terminal (don’t forget to source again):

source ~/ros2_ws/install/setup.bash

🔹 Online Mapping (recommended)
ros2 launch robot slam_simulation.launch.py use_slam_option:=online_async_slam

🔹 Localization with prebuilt map
ros2 launch robot slam_simulation.launch.py use_slam_option:=mapper_params_localization


