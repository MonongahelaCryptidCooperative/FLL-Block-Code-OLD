from pybricks.parameters import Button
from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Remote, Motor
from pybricks.robotics import DriveBase
from pybricks.tools import wait

def setup_hub(hub:PrimeHub):
    """ Need to change the shutdown button to left and right at same time otherwise
    it will shutdown when the center button is pressed. Currently not possible to do 
    in the block interface"""
    hub.system.set_stop_button([Button.LEFT, Button.RIGHT])

def drive_base_reset(drive_base:DriveBase):
    drive_base.reset()

def stick_drift(stick:int):
    if stick < 7 and stick > -7:
        return 0
    else:
        return stick
