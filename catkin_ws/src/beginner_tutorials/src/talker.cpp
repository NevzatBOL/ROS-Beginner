#include "ros/ros.h"
#include "std_msgs/String.h"
#include <sstream>

int main(int argc,char **argv)
{
	ros::init(argc,argv,"talker"); //Node'u başlatır.
	ros::NodeHandle n; //node'u başlatır ve sonlandırır.
	ros::Publisher chatter_pub = n.advertise<std_msgs::String>("chatter",1000); 

	ros::Rate loop_rate(10); //çalışma hızını 10hz

 	int count=0;
	while(ros::ok())
	{
		std_msgs::String msg; //yayınlanacak mesaj türünü belirleriz.
		
		std::stringstream ss;
		ss<<"hello world"<<count;
		msg.data=ss.str();

		ROS_INFO("%s",msg.data.c_str());

		chatter_pub.publish(msg); //mesajı yayınladık.

		ros::spinOnce();	
		loop_rate.sleep();
		++count;
	}
	return 0;
	
}
