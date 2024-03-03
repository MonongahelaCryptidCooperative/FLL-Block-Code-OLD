# FLL
Code to use Pybricks for competitive robotics

Hey everyone,

I wanted to share a project I worked on for first lego league. 
One of the things our team did this year was to use the Lego Bluetooth remotes to control our robot while we were developing new attachments for our robot as well as mission strategies. This allowed for a rapid development cycle as we didn't have to worry about coding. We also used the remote code to take measurements so we did not have to "guess and check" when programming the robot.
Previously we did this in text Pybricks python. However Pybricks recently released a block interface. They also added Xbox controller support. This is better than using the Lego Bluetooth controllers as it allows for analog inputs vs the binary inputs on the Lego controllers. 


Included here is some example code to show how to use Pybricks for FLL. For one thing Pybricks does not have a user interface to select programs. An example one is given along with 3 example programs (drive in a circle, triangle, square). All 3 example programs first have the robot square off against the back wall, then turn on the gyro (for accurate movements), do the movements, then return home and turn off the gyro (so you could pick up the robot/switch attachments etc.). 


The remote mode is accessed by selecting program "0 0" (hit left to go backwards in the program list) and launched by hitting the center button. 


The left joystick makes the robot go fowards/backwards

The right joystick turns

The right trigger controls the right motor, pushing down the right bumper and the right trigger reverses the right motor. This is done via analog inputs so fine control is possible. 

The left trigger controls the left attachment motor in the similar manner. 

The "a" button is very cool. It prints off how far the robot drove/turned and how far the attachment motors moved. These values can be used to directly program the FLL robot and eliminated "guessing and checking" or having to use a ruler to figure out how far to make the robot drive/turn/move an attachment, etc. 



Other settings that will need to be changed: 
1. In the hub block you will have to set which direction your hub is facing. Front is the axis of the usb port, top is the screen. Unless you also have a vertically oriented hub design these values will be wrong. 


2.  You also have to give the drivebase class the layout/dimensions of your robot. It needs both the wheel spacing (in mm) and wheel diameter (in mm). This is how the drivebase module is able to do accurate driving commands. 

Two files are required. One is the "BlockStarterPackXBOX" the other is a text-python file called "extra_code" that contains 3 functions we couldn't figure out how to do easily in the block interface that are then imported into the Block interface/BlockStartPackXBOX file. 
Enjoy! Please contact me with any questions!
