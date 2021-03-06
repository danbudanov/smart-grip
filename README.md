# Smart Gripper
*Project for HackGT 4*

A smart prosthetic hand that uses object recognition, vision processing, 
and sensor feedback to grasp at commonly used objects.

* __vision__ contains an overarching script for the system that 
  * retrieves and packages frames, 
  * sends them to the cloud where object recognition is performed, 
  * checks the relative object position and distance, and
  * commands the gripping motion
* __firmware__ contains the firmware that runs on the Arduino, which receives
UART signals from the computer, and either sends back distance data from the
distance sensor or grips the object by a specified amount.
