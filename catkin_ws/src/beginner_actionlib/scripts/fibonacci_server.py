#!/usr/bin/env python
import rospy
import actionlib
import beginner_actionlib.msg

class FibonacciAction (object):

    _feedback = beginner_actionlib.msg.FibonacciFeedback()
    _result = beginner_actionlib.msg.FibonacciResult()
    
    def __init__(self,name):
        self._action_name=name
        self._as=actionlib.SimpleActionServer(self._action_name,beginner_actionlib.msg.FibonacciAction, execute_cb=self.execute_cb, auto_start=False)
        self._as.start()
    
    def execute_cb(self,goal):
        r = rospy.Rate(1)
        success = True
        
        self._feedback.sequence = []
        self._feedback.sequence.append(0)
        self._feedback.sequence.append(1)
        
        rospy.loginfo('%s: Executing, creating fibonacci sequence of order %i with seeds %i, %i'%(self._action_name, goal.order, self._feedback.sequence[0], self._feedback.sequence[1]))


        for i in range(1,goal.order):
            if self._as.is_preempt_requested():
                rospy.loginfo('%s: Preempted'%self._action_name)
                self._as.set_preempted()
                success = False
                break
            self._feedback.sequence.append(self._feedback.sequence[i]+self._feedback.sequence[i-1])
            self._as.publish_feedback(self._feedback)
            
            r.sleep()
        
        if success:
            self._result.sequence=self._feedback.sequence
            rospy.loginfo('%s: Succeeded'%self._action_name)
            self._as.set_succeeded(self._result)



if __name__ == '__main__':
    rospy.init_node('fibonacci')
    server = FibonacciAction(rospy.get_name())
    rospy.spin()
