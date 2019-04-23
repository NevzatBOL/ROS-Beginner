#!/usr/bin/env python
import rospy
import actionlib
import beginner_actionlib.msg
import sys

def fibonacci_client():
    client = actionlib.SimpleActionClient('fibonacci',beginner_actionlib.msg.FibonacciAction)
    client.wait_for_server()
    goal = beginner_actionlib.msg.FibonacciGoal(order=20)
    client.send_goal(goal)
    client.wait_for_result()
    return client.get_result()

if __name__ == '__main__':
    try:
        rospy.init_node('fibonacci_client')
        result = fibonacci_client()
        print "Result:", ', '.join([str(n) for n in result.sequence])
    except rospy.ROSInterruptException:
        print "program inerrupted before comletion", file(sys.stderr)
