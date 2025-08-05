import rospy
from std_msgs.msg import String 

rospy.init_node('publisher', anonymous=True)
rate = rospy.Rate(1)  # 1 Hz
pub=rospy.Publisher('/chatter', String, queue_size=10)

string="Hello, ROS!"
value=String()
value.data=string

while 1:
    pub.publish(value)  
    rate.sleep()  # Sleep for 1 second to control the publishing rate


rospy.spin()