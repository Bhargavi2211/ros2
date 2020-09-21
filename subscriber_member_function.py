# Copyright 2016 Open Source Robotics Foundation, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import rclpy
from rclpy.node import Node
from array import *
from std_msgs.msg import String

x_p = array("f", [0])
y_p = array("f", [0])

class MinimalSubscriber(Node):

    def __init__(self):
        super().__init__('minimal_subscriber')
        self.subscription = self.create_subscription(String, 'topic', self.listener_callback, 10)
        self.subscription  # prevent unused variable warning

    def listener_callback(self, msg):
        waypoint = msg.data.split(" ")
       
        x_pos = x_p[-1]
        y_pos = y_p[-1]
        way_x = float(waypoint[0])
        way_y = float(waypoint[1])
        print("\n")
        self.get_logger().info('Currently UAV at \"( "%s" , "%s" )\"'%(str(x_pos),str(y_pos)))
        x = x_pos
        y = y_pos
        distance = (((x_pos - way_x) ** 2 + (y_pos - way_y) ** 2) ** 0.5)
        vector_x = (((way_x - x_pos) / distance) * 0.1)
        vector_y = (((way_y - y_pos) / distance) * 0.1)
        while (vector_x < way_x) and (vector_y < way_y):
            x = x + vector_x
            y = y + vector_y

            if x >= way_x and y >= way_y:
                self.get_logger().info('Currently UAV at \"( "%s" , "%s" )\"'%(str(way_x),str(way_y)))
                break
            else:
                self.get_logger().info('Currently UAV at \"( "%s" , "%s" )\"'%(str(x),str(y)))
                
        x_p.append(way_x) 
        y_p.append(way_y)
        

        
def main(args=None):
    rclpy.init(args=args)

    minimal_subscriber = MinimalSubscriber()
    
    rclpy.spin(minimal_subscriber)

    # Destroy the node explicitly
    # (optional - otherwise it will be done automatically
    # when the garbage collector destroys the node object)
    minimal_subscriber.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()

