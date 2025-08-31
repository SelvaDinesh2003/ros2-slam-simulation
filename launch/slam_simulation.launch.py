import os
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription, DeclareLaunchArgument
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch_ros.actions import Node
from launch.substitutions import LaunchConfiguration, PythonExpression
from launch.conditions import IfCondition

def generate_launch_description():

    package_name= 'robot'
    package_dir= get_package_share_directory(package_name) 

    use_sim_time = LaunchConfiguration('use_sim_time')
    map = LaunchConfiguration('map')
    use_slam_option = LaunchConfiguration('use_slam_option')
    
    declare_use_sim_time= DeclareLaunchArgument(
        'use_sim_time',
        default_value='true',
        description='If true, use simulated clock'
    )  

    declare_map= DeclareLaunchArgument(
        'map',
        default_value='./src/minibot/maps/sample_map.yaml',
        description='If true, use simulated clock'
    )

    declare_use_slam_option = DeclareLaunchArgument(
        'use_slam_option',
        default_value='online_async_slam',
        description='Choose SLAM option: amcl, mapper_params_localization, or online_async_slam'
    )  

    mapper_params_online_async_file = os.path.join(
        package_dir, 
        'config', 
        'mapper_params_online_async.yaml'
    )

    mapper_params_localization_file = os.path.join(
        package_dir, 
        'config', 
        'mapper_params_localization.yaml'
    )


 
        
    # online_async_slam launch 
    online_async_slam = IncludeLaunchDescription(
                PythonLaunchDescriptionSource([os.path.join(
                    get_package_share_directory('slam_toolbox'),
                    'launch',
                    'online_async_launch.py'
                )]), 
                launch_arguments={
                    'slam_params_file': mapper_params_online_async_file,
                    'use_sim_time': use_sim_time
                }.items(),
                condition=IfCondition(PythonExpression(["'", use_slam_option, "' == 'online_async_slam'"]))         
    )


     # Create the launch description and populate
    ld = LaunchDescription()
    
    # Add the launch arguments
    ld.add_action(declare_use_sim_time)
    ld.add_action(declare_map)
    ld.add_action(declare_use_slam_option)

    # Add SLAM options
    ld.add_action(online_async_slam)

    # Generate the launch description and 
    return ld

    