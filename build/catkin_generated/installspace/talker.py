import rospy
from std_msgs.msg  import String

if __name__ == '__main__':
    
    def talker():
        pub = rospy.Publisher('chatting' , String , queue_size=5)
        rospy.init_node('talker' , anonymous=True)
        rate = rospy.Rate(freq)
        while not rospy.is_shutdown():
            msg = ('hello, iam khaled %s'  % rospy.get_time())
            rospy.loginfo( msg )
            pub.publish ( msg )
            rate.sleep()
    
    try:
        global freq
        freq=rospy.get_param("freq")
       
        talker()
    except rospy.ROSInterruptException:
      pass    

