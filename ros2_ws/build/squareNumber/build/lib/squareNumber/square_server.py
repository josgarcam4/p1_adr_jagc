import rclpy
from rclpy.node import Node
from example_interfaces.srv import AddTwoInts

class SquareServer(Node):
    def __init__(self):
        super().__init__('square_service')
        self.srv = self.create_service(
            AddTwoInts,
            'square',
            self.calculate_square_callback)
        self.get_logger().info('Square service server has been started')

    def calculate_square_callback(self, request, response):
        response.sum = request.a * request.b  # a * b (como a² si a == b)
        self.get_logger().info(
            f'Request: {request.a} * {request.b} = {response.sum}')
        return response

def main(args=None):
    rclpy.init(args=args)
    node = SquareServer()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main()
