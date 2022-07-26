#turn_signal.py
#turns on a turn signal (static light) if the robot is turning and otherwise does nothing

import rospy 
from geometry_msgs.msg import Twist
from std_msgs.msg import Bool
pub = None

#Calls whenever new vel message
def turn_callback(twist):
    #if the new angular velocity greater or less than than 0, turn the light on
    if twist.angular.z != 0:  
        pub.publish(True)

    else:
        pub.publish(False)


if __name__ == '__main__':
    try: 
        
        rospy.init_node('turn_signal')

        #Publishes to toggle_led, to set LED
        pub = rospy.Publisher('toggle_led', Bool, queue_size=1000)
        #Subscribes to cmd vel
        sub = rospy.Subscriber("cmd_vel", Twist, turn_callback)

        rospy.spin()

    except rospy.ROSInterruptException:
        pass