#include "ros/ros.h"
#include "beginner_tutorials/Num.h"

int main(int argc, char **argv)
{
    ros::init(argc,argv,"talker");
    ros::NodeHandle n;
    ros::Publisher pub = n.advertise<beginner_tutorials::Num>("talker",1);
    
    ros::Rate loop_rate(10);
    
    while(ros::ok())
    {
        beginner_tutorials::Num msg;
        msg.num = 4;
        ROS_INFO("%ld",msg.num);
        pub.publish(msg);
        
        ros::spinOnce();
        loop_rate.sleep();
    }
    
    return 0;
}
