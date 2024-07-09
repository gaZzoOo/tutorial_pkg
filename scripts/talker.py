import rospy
from std_msgs.msg  import String
from tutorial_pkg.msg import V2V

if __name__ == '__main__':
    
    def talker():
        pub = rospy.Publisher('chatting' , String , queue_size=5)
        pub_car = rospy.Publisher("car_chan" , V2V , queue_size=10)
        rospy.init_node('talker' , anonymous=True)
        rate = rospy.Rate(1)
        my_car_info = V2V()
        my_car_info.id = 1000173989
        my_car_info.battery_level = 0.90
        my_car_info.car_pose.x = 10
        my_car_info.car_speed.linear.x = 50
        msg = ("hello,iam gazzo %s" % rospy.get_time())

        while not rospy.is_shutdown():
            pub_car.publish (my_car_info)
            
            rospy.loginfo( msg )
            rospy.loginfo(my_car_info)
            pub.publish ( msg )
            rate.sleep()
    
    try:
        #global word
        #word=rospy.get_param("word")
       
        talker()
    except rospy.ROSInterruptException:
      pass    

