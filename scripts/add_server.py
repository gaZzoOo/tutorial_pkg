from tutorial_pkg.srv import AddTwoInts
from tutorial_pkg.srv import AddTwoIntsRequest
from tutorial_pkg.srv import AddTwoIntsResponse
import time
import rospy

def handle_add_two_ints(req):
    print("returning[%s+%s=%s]" %(req.a,req.b,(req.a+req.b)))
    time.sleep(3)
    sum_response=AddTwoIntsResponse(req.a + req.b)
    return sum_response
def add_two_ints_server():
    rospy.init_node("add_two_ints_server")
    s=rospy.Service("add_two_ints",AddTwoInts,handle_add_two_ints)
    print("ready to add ints , gaZzO")
    rospy.spin()

if __name__== "__main__" :
    add_two_ints_server()    
