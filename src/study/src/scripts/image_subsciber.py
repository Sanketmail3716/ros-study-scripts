import rospy
from sensor_msgs.msg import Image


rospy.init_node('subscriber', anonymous=True)


def cb(data):
    print("Image height is ",data.height, "image_width is ",data.width)


rospy.Subscriber('/Image', Image, cb)  
rospy.spin()

"""

 Based on the code snippets you provided earlier, here's a summary of the image_subscriber and image_publisher scripts:

image_publisher

Publishes an image to a ROS topic called /Image
Reads an image file from a specific location ("/home/sanket/Desktop/work/src/study/src/scripts/cat_image.jpg")
Converts the image to a ROS image message using cv_bridge
Publishes the image message to the /Image topic at a rate of 10 Hz
Uses the rospy library to interact with the ROS environment
image_subscriber

Subscribes to the /Image topic to receive image messages
Defines a callback function 
cb
 that is called when an image message is received
The callback function prints the height and width of the received image
Uses the rospy library to interact with the ROS environment
In summary, the image_publisher script sends an image to the /Image topic, and the image_subscriber script receives and processes the image messages from that topic.

"""