import launch
import launch_ros.actions


def generate_launch_description():
    return launch.LaunchDescription([
        # Keyboard Teleoperation
        launch_ros.actions.Node(
            package='teleop_twist_keyboard', executable='teleop_twist_keyboard', name='teleop_keyboard',
            output='screen',
            remappings=[('/cmd_vel', '/cmd_vel_keyboard')]
        ),
        
        # Twist Multiplexer (merging keyboard commands with navigation commands)
        launch_ros.actions.Node(
            package='twist_mux', executable='twist_mux', name='twist_mux',
            parameters=[{
                'topics': [
                    {'name': 'navigation', 'topic': '/cmd_vel', 'timeout': 0.5, 'priority': 10},
                    {'name': 'keyboard', 'topic': '/cmd_vel_keyboard', 'timeout': 0.5, 'priority': 20}
                ]
            }],
            remappings=[('/cmd_vel_out', '/cmd_vel')]
        )
    ])
