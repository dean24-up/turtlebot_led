//toggle_led

#include <ros.h>
#include <std_msgs/Bool.h>

ros::NodeHandle nh;

void ledCallback( const std_msgs::Bool& toggle_msg){
  bool on_or_off = toggle_msg.data;
  if (on_or_off == true){
    digitalWrite(BDPIN_GPIO_2, HIGH); //turn off the LED
  }
  else {
    digitalWrite(BDPIN_GPIO_2, LOW);  //turn on the LED
  }
}

ros::Subscriber<std_msgs::Bool> sub("toggle_led", &ledCallback);

void setup() {
  pinMode(BDPIN_GPIO_2, OUTPUT);  //controlling LED in BDPIN_GPIO_2
  nh.initNode();
  nh.subscribe(sub);
}

void loop() {
  nh.spinOnce();
  delay(1);
}
