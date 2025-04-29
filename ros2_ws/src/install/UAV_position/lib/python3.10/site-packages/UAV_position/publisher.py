import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class SimplePublisher(Node):
    def __init__(self):
        super().__init__('simple_publisher')
        self.publisher=(self.create_publisher(String,'topic',10))
        self.timer=(self.create_timer(1.0,self.publish_message))
    def publish_message(self):
        msg = String()
        msg.data="Hola desde ROS2"
        self.publisher.publish(msg)
        self.get_logger().info(f'Publicando: {msg.data}')
rclpy.init()
node = SimplePublisher()
rclpy.spin(node)