import rospy
from sensor_msgs.msg import Image


rospy.init_node('subscriber', anonymous=True)


def cb(data):
    print("Image height is ",data.height, "image_width is ",data.width)


rospy.Subscriber('/Image', Image, cb)  
rospy.spin() 