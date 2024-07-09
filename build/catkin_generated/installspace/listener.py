import rospy
from std_msgs.msg import String

if __name__ == '__main__':
    
    def callback(my_string):
        rospy.loginfo('i heared %s' % my_string.data)

    
    def listener():
        rospy.init_node('listener' , anonymous=True)
        rospy.Subscriber('chatting' , String , callback)
        rospy.spin()

    try :
        listener()
    except rospy.ROSInterruptException:
     pass
    

