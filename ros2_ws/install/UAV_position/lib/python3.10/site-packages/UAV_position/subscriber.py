import rclpy
from rclpy.node import Node
from sensor_msgs.msg import NavSatFix

class GPSTrackerSubscriber(Node):
    def __init__(self):
        super().__init__('gps_tracker_subscriber')
        # Crear el suscriptor para el mensaje NavSatFix
        self.subscription = self.create_subscription(
            NavSatFix,
            'gps_topic',  # El tema al que se suscribe
            self.callback,
            10
        )

    def callback(self, msg):
        # Mostrar los datos recibidos del GPS
        self.get_logger().info(f'Recibido GPS: Latitud={msg.latitude}, Longitud={msg.longitude}, Altitud={msg.altitude}')

rclpy.init()
node = GPSTrackerSubscriber()
rclpy.spin(node)
