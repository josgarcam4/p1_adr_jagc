import rclpy
from rclpy.node import Node
from square.srv import SquareNumber  # Importa el mismo servicio que el servidor

class SquareNumberClient(Node):
    def __init__(self):
        super().__init__('square_number_client')
        self.client = self.create_client(SquareNumber, 'square_number')
        while not self.client.wait_for_service(timeout_sec=1.0):
            self.get_logger().info('Service not available, waiting again...')
        self.request = SquareNumber.Request()

    def send_request(self, number):
        self.request.a = number  # Establece el número a enviar
        self.future = self.client.call_async(self.request)  # Llama al servicio
        self.future.add_done_callback(self.callback)

    def callback(self, future):
        try:
            response = future.result()
            self.get_logger().info(f'El cuadrado de {self.request.a} es: {response.sum}')
        except Exception as e:
            self.get_logger().error(f'Error al llamar al servicio: {e}')

def main(args=None):
    rclpy.init(args=args)
    client = SquareNumberClient()
    client.send_request(5)  # Cambia este valor por cualquier número que quieras probar
    rclpy.spin(client)
    rclpy.shutdown()

if __name__ == '__main__':
    main()
