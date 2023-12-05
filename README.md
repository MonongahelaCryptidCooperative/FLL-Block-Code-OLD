# FLL-Block-Code

Hey everyone. This is the MonongahelaCryptidCooperative (an upcoming FTC team, who did FLL this year). We want to share some starter code to help newer teams who are not yet ready to use text-based python be able to experience all the advantages that using the Pybricks firmware/software can provide. This includes much more accurate driving with the DriveBase module (particularly when the gyro is turned on) and fun things like using Bluetooth remotes. However there is a bit of a learning curve and to overcome this we decided to release a starter pack to entice teams not yet ready to use text-based python to make the switch. There is a small fee to use Pybrick's block interface (after a one-week trial), but it is worth the price in our opinion.

First you will have to reflash your hub. Pybricks has a great video tutorial on how to do this. The only problem you will likely have is Windows choosing the wrong USB driver (the Pybricks tutorial goes over how to fix this). It is easy to reflash it back to the default Lego firmware if you decide you do not like Pybricks (but doubt that will be the case).



Two files are required. The first is the BlockStarterPack.py. The second is labeled extra_code.py. The second file is required as a couple necessary methods are not accessible through the block interface (namely making it so that the center button doesn't just end the program, instead you have to push both the right and left buttons as the same time and also you cannot reset the DriveBase counters currently with the block interface).

Initial Setup once Pybricks is flashed to the hub/files loaded:

You will have to change the settings to match your robot. In the prime hub block you need to set the top and front axis of your robot. Our robot is weird and has a vertically oriented hub and thus has the top axis as Y and the front as Z. Most robots will have the front axis be Y and (depending on orientation) the top axis as either Z or X (positive or negative). If these settings are wrong the DriveBase will do really weird things when the gyro is turned on.

motors/sensors will have to be assigned to the correct ports with the correct direction of the drive motors given (counterclockwise vs clockwise).

You will also have to change the DriveBase setting to match the wheel size and wheel spacing of your robot. The DriveBase uses this information to calculate everything for you allowing for accurate movements.

What the code does:

One of the difficulties with Pybricks is that it doesn't have much of a built-in user interface. Unlike with the Lego education software there are not slots that you put separate programs in. Rather you load up one large program to the entire robot. While this presents a barrier (you have to code some sort of user interface) it is ultimately an advantage as you can have your robot auto-advance between runs saving valuable seconds (you shouldn't have to do anything other than hit the "launch" button during matches). Included in the code is a rudimentary user interface. There is a counter that can be decreased or increased by pressing the left/right buttons and is displayed on the display that represents the current active program. There is then a large conditional statement that associates each program with a number (example programs are square, circle, triangle, example). If the number matches, the program is launched when the center button is pressed. The runs do auto-advance as currently coded. More advanced user interfaces are possible, but this is a start.

When programming a run it is advised to first square off against the back wall, then turn on the gyro. The gyro should then be turned off before the end of the run (otherwise the robot will try to maintain its current heading when you pick it up to reposition it). The examples do this.

Also included is code to control the robot and take measurements via a Lego Bluetooth powered up remote Electric Powered Up Bluetooth Speed Remote Control Unit with Light Bluish Gray Base : Part 28739c01 | BrickLink. If you do not own a powered up remote you will have to remove the remote block from the setup section (the code will crash if a remote is not paired within one minute). It is the very last block in the startup code. Obviously, such would have to be removed before using the code in competition.

The remote code is very useful as you can partially program a run, then have it enter the remote control mode at the very end so you can drive the robot to take measurements (press the center button to print off the cumulative movements/reset). These measurements can then be used to program the next steps. To us this is a much more fun way to interact with and program the robot.

Video tutorials and more thorough documentation will eventually be made.

If you are able to use text-python it is still advised that you go that route (example code for such is also on our github) as it is a bit more elegant.
