from tutorial_pkg.srv import AddTwoInts
from tutorial_pkg.srv import AddTwoIntsRequest
from tutorial_pkg.srv import AddTwoIntsResponse
import rospy
import sys

def add_two_ints_client(x,y):
    rospy.wait_for_service("add_two_ints")
    try:
        add_two_ints=rospy.ServiceProxy("add_two_ints",AddTwoInts)
        resp1=add_two_ints(x,y)
        return resp1.sum
    except rospy.ServiceException as e :
        print("service call failed :%s"%e)

if __name__=="__main__":
    if len (sys.argv)== 3:
        x=int(sys.argv[1])
        y=int(sys.argv[2])
    else:
        sys.exit(1)
    print("requesting%s+%s"%(x,y))
    print("%s+%s=%s"%(x,y,add_two_ints_client(x,y)))    
