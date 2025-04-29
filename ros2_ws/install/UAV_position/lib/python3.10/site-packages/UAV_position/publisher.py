import rclpy
from rclpy.node import Node
from sensor_msgs.msg import NavSatFix

class GPSTrackerPublisher(Node):
    def __init__(self):
        super().__init__('gps_tracker_publisher')
        # Crear el publicador para el mensaje NavSatFix
        self.publisher = self.create_publisher(NavSatFix, 'gps_topic', 10)
        # Crear el temporizador para publicar cada 1 segundo
        self.timer = self.create_timer(1.0, self.publish_gps_data)

    def publish_gps_data(self):
        # Crear un mensaje de tipo NavSatFix
        msg = NavSatFix()
        msg.latitude = 37.7749  # Latitud de ejemplo (San Francisco)
        msg.longitude = -122.4194  # Longitud de ejemplo (San Francisco)
        msg.altitude = 10.0  # Altitud de ejemplo en metros

        # Publicar el mensaje
        self.publisher.publish(msg)
        self.get_logger().info(f'Publicando GPS: Latitud={msg.latitude}, Longitud={msg.longitude}, Altitud={msg.altitude}')

rclpy.init()
node = GPSTrackerPublisher()
rclpy.spin(node)
