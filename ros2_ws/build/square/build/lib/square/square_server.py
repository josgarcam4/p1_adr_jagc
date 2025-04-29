import rclpy
from rclpy.node import Node
from square.srv import Square  # Usamos un servicio estándar para la demostración

class SquareNumberService(Node):
    def __init__(self):
        super().__init__('square_number_service')
        self.srv = self.create_service(Square, 'square_number', self.square_callback)
        self.get_logger().info('Service ready to square numbers.')

    def square_callback(self, request, response):
        response.sum = request.a * request.a  # Calculamos el cuadrado del número
        self.get_logger().info(f'Calculating square of {request.a}: {response.sum}')
        return response

def main(args=None):
    rclpy.init(args=args)
    service = SquareNumberService()
    rclpy.spin(service)
    rclpy.shutdown()

if __name__ == '__main__':
    main()
