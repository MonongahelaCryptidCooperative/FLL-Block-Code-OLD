# Pybricks FLL Block code created by Julian Huss
Code to use Pybricks for competitive robotics

Hey everyone,

I wanted to share a project I worked on for first lego league. 
One of the things our team did this year was to use the Lego Bluetooth remotes to control our robot while we were developing new attachments for our robot as well as mission strategies. This allowed for a rapid development cycle as we didn't have to worry about coding. We also used the remote code to take measurements so we did not have to "guess and check" when programming the robot.
Previously we did this in text Pybricks python. However Pybricks recently released a block interface. They also added Xbox controller support. This is better than using the Lego Bluetooth controllers as it allows for analog inputs vs the binary inputs on the Lego controllers. 


Included here is some example code to show how to use Pybricks for FLL. For one thing Pybricks does not have a user interface to select programs. An example one is given along with 3 example programs (drive in a circle, triangle, square). All start with the gyro off, then turn it on, do the movements, then turn off the gyro and head back home. This lets you pick up/place the robot. All programs also autoadvance to the next one. This is very good in the tournament as it saves valuable seconds as you don't have to manually select th next program. There is also an example that shows how you can square off of the back wall to line up the robot, this can also be a good strategy.


IF YOU DO NOT HAVE AN XBOX CONTROLLER YOU WILL HAVE TO REMOVE THE "XBOX" BLOCK OTHERWISE THE CODE WILL TIME OUT/STOP. A CONTROLLER WILL HAVE TO BE TURNED ON/READY TO BE PAIRED WHENVER THIS CODE IS RAN IF THE XBOX BLOCK IS IN THE STARTUP SECION!! Alternatively you can use the NoRemote version of the code. Obviously you will have to disable/remove the XBOX block during the tournament. 


The remote mode is accessed by selecting program "0 0" (hit left to go backwards in the program list) and launched by hitting the center button. 


The left joystick makes the robot go fowards/backwards

The right joystick turns

The right trigger controls the right motor, pushing down the right bumper and the right trigger reverses the right motor. This is done via analog inputs so fine control is possible. 

The left trigger controls the left attachment motor in the similar manner. 

The "a" button is very cool. It prints off how far the robot drove/turned and how far the attachment motors moved. These values can be used to directly program the FLL robot and eliminated "guessing and checking" or having to use a ruler to figure out how far to make the robot drive/turn/move an attachment, etc. 



SETTINGS THAT WILL NEED TO BE CHANGED!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
1. In the hub block you will have to set which direction your hub is facing. Front is the axis of the usb port, top is the screen. Unless you also have a vertically oriented hub design these values will be wrong. YOU WILL LIKELY HAVE TO CHANGE THESE VALUES


2.  You also have to give the drivebase class the layout/dimensions of your robot. It needs both the wheel spacing (in mm) and wheel diameter (in mm). This is how the drivebase module is able to do accurate driving commands. SMALL SPIKE WHEELS ARE 56 mm LARGE SPIKE WHEELS ARE 88 mm. You can look up the dimensions of other wheels at http://www.wheels.sariel.pl/. Technic holes are spaced 8 mm apart so you can either count the holes or use a ruler to determine your wheel spacking. 


Enjoy! Please contact me with any questions! Please credit our team (the Monongahela Cryptid Cooperative) and our coder (Julian Huss) if our code is used.
