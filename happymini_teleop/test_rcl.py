import threading
import rclpy
import time

def main():
    rclpy.init()
    node = rclpy.create_node('test_node')
    thread = threading.Thread(target=rclpy.spin, args=(node, ), daemon=True)
    thread.start()

    rate = node.create_rate(2)

    try:
        while rclpy.ok():
            print(rclpy.ok())
            rate.sleep()
    except KeyboardInterrupt:
        #time.sleep(1.0)
        print(f"Ctrl + c >>> {rclpy.ok()}")
    
    node.destroy_node()
    rclpy.shutdown()
    thread.join()
