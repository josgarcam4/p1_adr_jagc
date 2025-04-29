import rclpy
from rclpy.node import Node
from square.srv import Square
import sys

class SquareClient(Node):
    def __init__(self):
        super().__init__('square_client')
        self.cli = self.create_client(Square, 'square')
        while not self.cli.wait_for_service(timeout_sec=1.0):
            self.get_logger().info('service not available, waiting again...')
        self.req = Square.Request()
        
    def send_request(self, x):
        self.req.x = x
        self.future = self.cli.call_async(self.req)
        rclpy.spin_until_future_complete(self, self.future)
        return self.future.result()

def main(args=None):
    rclpy.init(args=args)
    square_client = SquareClient()
    
    if len(sys.argv) != 2:
        square_client.get_logger().info('Usage: ros2 run p1_adr_pkg square_client <number>')
        return 1
    
    try:
        x = float(sys.argv[1])
    except ValueError:
        square_client.get_logger().error('Input should be a number')
        return 1
    
    response = square_client.send_request(x)
    square_client.get_logger().info(
        f'Square of {x:.2f} = {response.x_squared:.2f}')
    
    square_client.destroy_node()
    rclpy.shutdown()
    return 0

if __name__ == '__main__':
    main()