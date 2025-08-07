# Add image and open cv2

import rospy
import cv2 as cv
from cv_bridge import CvBridge
from sensor_msgs.msg import Image


rospy.init_node('publisher', anonymous=True)
rate = rospy.Rate(10)  # 1 Hz

pub=rospy.Publisher('/Image',Image, queue_size=10)

bridge=CvBridge()
img=cv.imread("/home/sanket/Desktop/work/src/study/src/scripts/cat_image.jpg")
ros_image= bridge.cv2_to_imgmsg(img,"bgr8")

while not rospy.is_shutdown():
    
    pub.publish(ros_image)  
    rospy.loginfo("Image published")
    rate.sleep()  # Sleep for 1 second to control the publishing rate

#cv.imshow('/Image', img)
#cv.waitKey(0)  # Wait for a key press to close the window