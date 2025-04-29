import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class SimpleSubscriber(Node):
    def __init__(self):
        super().init('simple_subscriber')
        self.subscription=(self.create_subscription(String,'topic',self.callback,10))
    def callback(self,msg):
        self.get_logger().info(f'Recibido:{msg.data}')
        rclpy.init()
        node=SimpleSubscriber()
        rclpy.spin(node)