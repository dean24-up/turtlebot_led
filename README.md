# turtlebot_led

Adds LED to turtlebot3_core via Arduino code (turtlebot3_core).
  Creates toggle_led topic which receives Bool messages.
  Subscriber subscribes to toggle_led, turns on the LED when message.data = true and off when message.data = false.
  
  turtlebot3_core must be uploaded directly to the OpenCR, in place of turtlebot3_core already on OpenCR.

toggle_led_sketch includes only the code that was added to turtlebot3_core (subscriber setup for LED). Theoretically you could run this code with rosserial, but it hasn't been tested. Not necessary to run. 

turn_signal.py is a simple turn signal program that turns on the LED when the Turtlebot has angular velocity != 0. Run with teleop via ROS master.

This program is set up to operate with an LED in BDPIN_GPIO_2 or pin 4 of OpenCR's GPIO.




