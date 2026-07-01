# ---------------------------------------------------------------------------- #
#                                                                              #
# 	Module:       main.py                                                      #
# 	Author:       mattyu                                                       #
# 	Created:      4/10/2026, 6:53:39 PM                                        #
# 	Description:  V5 project                                                   #
#                                                                              #
# ---------------------------------------------------------------------------- #

#region VEXcode Generated Robot Configuration
from vex import *
import urandom
import math

# Brain should be defined by default
brain=Brain()

# Robot configuration code
left1 = Motor(Ports.PORT1, GearSetting.RATIO_6_1, True)
left2 = Motor(Ports.PORT2, GearSetting.RATIO_6_1, True)
left3 = Motor55(Ports.PORT3, True)
left_drive_bottom = MotorGroup(left1, left2)
right1 = Motor(Ports.PORT4, GearSetting.RATIO_6_1, False)
right2 = Motor(Ports.PORT5, GearSetting.RATIO_6_1, False)
right3 = Motor55(Ports.PORT6, False)
right_drive_bottom = MotorGroup(right1, right2)
drivetrain_inertial = Inertial(Ports.PORT7)
drivetrain_bottom = SmartDrive(left_drive_bottom, right_drive_bottom, drivetrain_inertial, 319.19, 320, 40, MM, 1)
ytracking_wheel = Rotation(Ports.PORT8, True)
xtracking_wheel = Rotation(Ports.PORT9, False)
distfront = Distance(Ports.PORT10)
distback = Distance(Ports.PORT11)
distright = Distance(Ports.PORT12)
distleft = Distance(Ports.PORT13)
gps = Gps(Ports.PORT14, 0, 0, MM, 0)
controller1 = Controller(PRIMARY)


# wait for rotation sensor to fully initialize
wait(30, MSEC)


# Make random actually random
def initializeRandomSeed():
    wait(100, MSEC)
    random = brain.battery.voltage(MV) + brain.battery.current(CurrentUnits.AMP) * 100 + brain.timer.system_high_res()
    urandom.seed(int(random))
      
# Set random seed 
initializeRandomSeed()


def play_vexcode_sound(sound_name):
    # Helper to make playing sounds from the V5 in VEXcode easier and
    # keeps the code cleaner by making it clear what is happening.
    print("VEXPlaySound:" + sound_name)
    wait(5, MSEC)

# add a small delay to make sure we don't print in the middle of the REPL header
wait(200, MSEC)
# clear the console to make sure we don't have the REPL in the console
print("\033[2J")

#endregion VEXcode Generated Robot Configuration


"""useful tools"""

def distance_to_degrees(distance, wheel_radius):
    return (distance*360) / (2 * math.pi * wheel_radius)


def degrees_to_distance(degrees, wheel_radius):
    return (degrees*(2 * math.pi * wheel_radius)) / 360


def inch_to_mm(inch):
    return (inch*25.4)


def mm_to_inch(mm):
    return (mm/25.4)


"""configuration set up & calibration tuning"""

#Function: stores robot location in coordinate system with (0,0) at bottom left corner.
#Format: list (mm = unit)
#Default: starting position (0,0).
#Uses: use_odom(), get_pos(), go_to()
xpos = [0.0]
ypos = [0.0]

#Function: storage – robot heading in coordinate system with (0,0) at bottom left corner.
#Format: list (degree = unit)
#Default: append reading from inertia sensor as initial heading
#Uses: turn_to(), update_rotation(), get_pos(), go_to()
headings = [drivetrain_inertial.rotation(DEGREES)]

#Function: storage – stores last gps reading of robot location in coordinate system with (0,0) at bottom left corner
#Format: list (mm = unit)
#Default: 0.0
#Uses: use_gps()
oldgpsx = 0.0
oldgpsy = 0.0

#Function: input – for distance between odom tracking wheel and center of drivetrain.
#Format: variable (inch = input unit, mm = stored unit)
#Default: 3 inch
#Uses: use_odom()
xwheeloffset = inch_to_mm(3.0)
ywheeloffset = inch_to_mm(3.0)

#Function: input – for radius of odom tracking wheel.
#Format: variable (inch = input unit, mm = stored unit)
#Default: 1 inch
#Uses: use_odom()
trackingwheelradius = inch_to_mm(1.0)

#Function: input – rpm of drivetrain
#Format: variable (rpm = unit)
#Default: 360 rpm
#Uses: odomdisplacement = 
driverpm = 360

#Function: input – wheel diameter of drivetrain
#Format: variable (inch = input unit, mm = stored unit)
#Default: 3.25 inch
#Uses: odomdisplacement = 
drivewheeldiameter = inch_to_mm(3.25)

#Function: input – field dimension
#Format: variable (inch = input unit, mm = stored unit)
#Default: 8feet * 6feet
#Uses: use_echo()
fieldwidth = inch_to_mm(8*12)
fieldlength = inch_to_mm(6*12)

#Function: input – cpu run time for odom & echolocation calculations
#Format: variable (millisecond = unit)
#Default: 5 milisecond, 5 milisecond
#Uses: 
odomruntime = 5.0
echoruntime = 5.0

#Function: calibration – update period of robot coordinate locationing
#Format: variable (milisecond = unit)
#Default: 10 milisecond
#Uses: get_pos(), positioning_loop()
positioningloopfrequency = 10.0

#Function: calibration – threshold for determining robot slow movement
#Format: variable (mm/s = unit)
#Default: 300 mm/s
#Uses: use_echo()
slowmovethreshold = 300.0

#Function: calibration – echolocation margin for error
#Format: variable (mm = unit)
#Default: 20mm
#Uses: use_echo()
echoerrortolerance = 20.0

#Function: input – offset of each distance sensor from drivetrain center in x & y axis
#Format: tuple of (offsetx, offsety) (mm = unit)
#Default: (0mm, 0mm)
#Uses: use_echo()
frontdistanceoffset = (0.0, 0.0)
backdistanceoffset = (0.0, 0.0)
rightdistanceoffset = (0.0, 0.0)
leftdistanceoffset = (0.0, 0.0)

#Function: calibration – how quickly robot responds to joystick control.
#Format: variable (whole number percentage = unit, 1 = max)
#Default: 1
#Uses: drivetrain_control_loop()
acceleration = 1.0

#Function: calibration – how quickly robot responds to joystick turning.
#Format: variable (whole number percentage = unit, 1 = max)
#Default: 1
#Uses: drivetrain_control_loop()
turnsensitivity = 1.0

#Function: calibration – margin for error of inertia sensor heading
#Format: variable (degree = unit)
#Default: 0.5 degrees
#Uses: turn_to(), go_to()
headingtolerance = 0.5

#Function: calibration – margin for error of location coordinate
#Format: variable (mm = unit)
#Default: 0.5mm
#Uses: go_to()
distancetolerance = 0.5

#Function: calibration – speed of auton navigation
#Format: variable (wholepercentage = unit)
#Default: 60%
#Uses: go_to()
autonspeed = 60.0

#Function: calibration – maximum heading adjustment velocity of autonomous navigation
#Format: variable (percentage = unit)
#Default: 10%
#Uses: go_to()
maxadjustment = 10.0

#Function: calibration – predicted odometry variance for auton navigation
#Format: variable (mm = unit, degree = unit, mm = unit)
#Default: 2.9718, 50.44
#Uses: use_gps()
autondisplacement = driverpm * drivewheeldiameter *1/60 * positioningloopfrequency/1000 * autonspeed/100
autonangle = 5.0
autonodomvariance = 0.5 * autondisplacement**2 + 2 * autonangle**2

#Other Calibration Functions:
#- Odom Variance = 0.05*dify^2 + 0.05*difx^2 + 2*angle^2
#- Echo Variance = 1.25^wallerror
#- Adjustment = heading_error / 6
#- gpsquality = 0.002 * (1000 * autonodomvariance - (1000 * autonodomvariance + 10^-9) / 100 * gps.quality())
#- gpsquality = autonodomvariance * (1 - (gps.quality()/100)**3) + 10**-9 for gps.quality() > 70



"""configure useful robot actions"""

def turn_to(degree):
    global headingtolerance, headings
    global turnvelocity, turnmax

    brain.screen.print("VEXcode")

    #get target heading
    targetheading = degree
    
    #get current heading
    update_headings()
    currentheading = headings[-1]

    #calculate necessary turn amount
    difference = (targetheading - currentheading + 180) % 360 - 180

    #while loop to turn until target heading has been reached
    while abs(difference) > headingtolerance:
        #sets turn speed based on turn amount required, capped between 10 & 50
        speed = max(1, min(turnmax, abs(difference)*turnvelocity))
        left1.set_velocity(speed, PERCENT)
        left2.set_velocity(speed, PERCENT)
        left3.set_velocity(speed, PERCENT)
        right1.set_velocity(speed, PERCENT)
        right2.set_velocity(speed, PERCENT)
        right3.set_velocity(speed, PERCENT)

        #initiates turn
        if difference > 0:
            left1.spin(FORWARD)
            left2.spin(FORWARD)
            left3.spin(FORWARD)
            right1.spin(REVERSE)
            right2.spin(REVERSE)
            right3.spin(REVERSE)
        else: 
            left1.spin(REVERSE)
            left2.spin(REVERSE)
            left3.spin(REVERSE)
            right1.spin(FORWARD)
            right2.spin(FORWARD)
            right3.spin(FORWARD)

        #wait to carry out turn
        wait(20, MSEC)

        #updates turn
        brain.screen.next_row()
        update_headings()
        currentheading = headings[-1]
        difference = (targetheading - currentheading + 180) % 360 - 180

    #stop rotation
    left1.stop()
    left2.stop()
    left3.stop()
    right1.stop()
    right2.stop()
    right3.stop()
    

"""coordinate locationing system"""

def update_rotation():
    global headings
    headings.append(drivetrain_inertial.rotation(DEGREES))
    if len(headings) > 5:
        headings.pop(0)


def use_odom(difx, dify, heading, angle):
    global xwheeloffset, ywheeloffset
    """Odometry"""
    #get rotation arch
    archx = -1 * (math.radians(angle)) * xwheeloffset
    archy = -1 * (math.radians(angle)) * ywheeloffset

    #calculate predicted location
    difx -= archx
    dify -= archy
    forwardx = math.sin(math.radians(heading))*dify
    strafingx = math.sin(math.radians(90+heading))*difx
    forwardy = math.cos(math.radians(heading))*dify
    strafingy = math.cos(math.radians(90+heading))*difx
    odomxpos = (xpos[-1] + forwardx + strafingx)
    odomypos = (ypos[-1] + forwardy + strafingy)
    
    #calculate weight of prediction
    odomxvariance = 0.05*dify**2 + 0.05*difx**2 + 2*angle**2
    odomyvariance = 0.05*dify**2 + 0.05*difx**2 + 2*angle**2

    #return values
    return [odomxpos, odomxvariance, odomypos, odomyvariance]


def use_echo(speed, heading, angle, odomx, odomy):
    global slowmovethreshold
    global fieldwidth, fieldlength
    global echoerrortolerance
    global frontdistanceoffset, backdistanceoffset
    global rightdistanceoffset, leftdistanceoffset

    theta = math.radians(heading)

    #find sensor offset from center in coordinate plane
    def rotate_offset(offsetx, offsety):
        worldx = offsetx * math.cos(theta) - offsety * math.sin(theta)
        worldy = offsetx * math.sin(theta) + offsety * math.cos(theta)
        return worldx, worldy

    frontoffx, frontoffy = rotate_offset(*frontdistanceoffset)
    backoffx, backoffy = rotate_offset(*backdistanceoffset)
    rightoffx, rightoffy = rotate_offset(*rightdistanceoffset)
    leftoffx, leftoffy = rotate_offset(*leftdistanceoffset)

    #quit measurement if robot is turning or speeding 
    if abs(angle) > 1 or speed > slowmovethreshold:
        return [odomx, 1e9, odomy, 1e9]

    #read sensors measurements
    front = distfront.object_distance(MM)
    back = distback.object_distance(MM)
    right = distright.object_distance(MM)
    left = distleft.object_distance(MM)

    #sensor beam directions
    front_theta = theta
    back_theta = theta + math.pi
    right_theta = theta + math.pi/2
    left_theta = theta - math.pi/2

    #calculate distance between robot & wall
    frontx = front * math.sin(front_theta) + frontoffx
    fronty = front * math.cos(front_theta) + frontoffy

    backx = back * math.sin(back_theta) + backoffx
    backy = back * math.cos(back_theta) + backoffy

    rightx = right * math.sin(right_theta) + rightoffx
    righty = right * math.cos(right_theta) + rightoffy

    leftx = left * math.sin(left_theta) + leftoffx
    lefty = left * math.cos(left_theta) + leftoffy

    #choose sensor that fully measures wall distance
    if 0 <= heading < 90:
        xright = max(frontx, rightx)
        xleft = max(backx, leftx)
        yfront = max(fronty, lefty)
        yback = max(backy, righty)
    elif 90 <= heading < 180:
        xright = max(frontx, leftx)
        xleft = max(backx, rightx)
        yfront = max(backy, lefty)
        yback = max(fronty, righty)
    elif 180 <= heading < 270:
        xright = max(backx, leftx)
        xleft = max(frontx, rightx)
        yfront = max(backy, righty)
        yback = max(fronty, lefty)
    else: #270 <= heading < 360:
        xright = max(backx, rightx)
        xleft = max(frontx, leftx)
        yfront = max(fronty, righty)
        yback = max(backy, lefty)

    #x-wall validation
    xwallerror = abs(fieldwidth - (abs(xright) + abs(xleft)))
    if xwallerror < echoerrortolerance:
        #append robot coordinates based on distance to walls
        echox = ((fieldwidth - abs(xright)) + (abs(xleft))) / 2
    else:
        echox = odomx

    #y-wall validation
    ywallerror = abs(fieldlength - (abs(yfront) + abs(yback)))
    if ywallerror < echoerrortolerance:
        #append robot coordinates based on distance to walls
        echoy = ((fieldlength - abs(yfront)) + (abs(yback))) / 2
    else:
        echoy = odomy

    #calculate the variance number based on wall error amount
    echoxvariance = 1.25**xwallerror
    echoyvariance = 1.25**ywallerror

    #return measurement & variance
    return [echox, echoxvariance, echoy, echoyvariance]

def use_gps():
    global autonodomvariance
    global fieldwidth, fieldlength

    #extract gps readings
    gpsx = gps.x_position(MM) + fieldwidth/2
    gpsy = gps.y_position(MM) + fieldlength/2
    gpsquality = gps.quality()

    #calculate gps weight
    if gpsquality > 70:
        gpsvariance = autonodomvariance * (1 - (gps.quality()/100)**3) + 10**-9
    
    #ignore if quality below 70
    else:
        gpsvariance = 10**9

    return [gpsx, gpsy, gpsvariance]

def get_pos():
    global positioningloopfrequency, headings

    #take basic measurements
    difx = degrees_to_distance(xtracking_wheel.position(DEGREES), trackingwheelradius) #travel distance
    dify = degrees_to_distance(ytracking_wheel.position(DEGREES), trackingwheelradius) #strafe distance
    speed = abs(dify) * (1000 / positioningloopfrequency) #robot traveling velocity
    update_rotation()
    heading = drivetrain_bottom.heading(DEGREES)%360 #robot orientation heading
    angle = (headings[-1] - headings[-2] + 180) % 360 - 180 #turn angle of robot

    #reset sensors
    xtracking_wheel.set_position(0, DEGREES)
    ytracking_wheel.set_position(0, DEGREES)

    #get odom prediction
    odomx, odomxvariance, odomy, odomyvariance= use_odom(difx, dify, heading, angle)

    #get echolocation
    echox, echoxvariance, echoy, echoyvariance = use_echo(speed, heading, angle, odomx, odomy)

    """Kalman Filter"""

    #calculate kalmangain
    kalmangainx = odomxvariance / (odomxvariance + echoxvariance + 10**-9)
    kalmangainy = odomyvariance / (odomyvariance + echoyvariance + 10**-9)

    #limit kalmangain
    kalmangainx = max(0, min(kalmangainx, 1))
    kalmangainy = max(0, min(kalmangainy, 1))

    #combine reading
    xpos.append(odomx + kalmangainx*(echox - odomx))
    ypos.append(odomy + kalmangainy*(echoy - odomy))

    if len(xpos) > 5:
        xpos.pop(0)
    if len(ypos) > 5:
        ypos.pop(0)

def get_pos2():
    global xpos, ypos
    global oldgpsx, oldgpsy
    global positioningloopfrequency, headings, loopcount, gpsloopfrequency, odomruntime

    #take basic measurements
    difx = degrees_to_distance(xtracking_wheel.position(DEGREES), trackingwheelradius) #travel distance
    dify = degrees_to_distance(ytracking_wheel.position(DEGREES), trackingwheelradius) #strafe distance
    speed = abs(dify) * (1000 / positioningloopfrequency) #robot traveling velocity
    update_rotation()
    heading = drivetrain_bottom.heading(DEGREES)%360 #robot orientation heading
    angle = (headings[-1] - headings[-2] + 180) % 360 - 180 #turn angle of robot

    #reset sensors
    xtracking_wheel.set_position(0, DEGREES)
    ytracking_wheel.set_position(0, DEGREES)

    #get odom prediction
    odomx, odomxvariance, odomy, odomyvariance = use_odom(difx, dify, heading, angle)

    #get gps measurement
    gpsx, gpsy, gpsvariance = use_gps()
    
    #integrates gps readings if gps measurements are fresh
    if gpsx != oldgpsx or gpsy != oldgpsy:

        """Kalman Filter"""

        #calculate kalmangain
        kalmangainx = odomxvariance / (odomxvariance + gpsvariance + 10**-9)
        kalmangainy = odomyvariance / (odomyvariance + gpsvariance + 10**-9)

        #caps kalmangain between 0 & 1
        kalmangainx = max(0, min(kalmangainx, 1))
        kalmangainy = max(0, min(kalmangainy, 1))

        #combine reading
        xpos.append(odomx + kalmangainx*(gpsx - odomx))
        ypos.append(odomy + kalmangainy*(gpsy - odomy))

        #update stored gps values
        oldgpsx = gpsx
        oldgpsy = gpsy

    #just use odometry prediction
    else: 
        xpos.append(odomx)
        ypos.append(odomy)

    #trim position log to recent 5
    if len(xpos) > 5:
        xpos.pop(0)
    if len(ypos) > 5:
        ypos.pop(0)


def positioning_loop():
    global positioningloopfrequency
    while competition.is_autonomous():
        get_pos()
        wait(positioningloopfrequency, MSEC)

def positioning_loop2():
    global positioningloopfrequency
    while competition.is_autonomous():
        get_pos2()
        wait(positioningloopfrequency, MSEC)


def go_to(x, y, direction):
    global xpos, ypos
    global distancetolerance, headingtolerance
    global autonspeed, maxadjustment

    #calculate distance
    difx = (x - xpos[-1])
    dify = (y - ypos[-1])
    distance = [math.sqrt(difx**2 + dify**2)]
    targetheading = math.degrees(math.atan2(difx, dify))

    #initialize motor velocity
    left_drive_bottom.set_velocity(autonspeed, PERCENT)
    left3.set_velocity(autonspeed, PERCENT)
    right_drive_bottom.set_velocity(autonspeed, PERCENT)
    right3.set_velocity(autonspeed, PERCENT)

    #turn + move
    if direction == "FORWARD":
        turn_to(targetheading)
        left_drive_bottom.spin(FORWARD)
        left3.spin(FORWARD)
        right_drive_bottom.spin(FORWARD)
        right3.spin(FORWARD)
    else:
        turn_to((targetheading + 180)%360)
        left_drive_bottom.spin(REVERSE)
        left3.spin(REVERSE)
        right_drive_bottom.spin(REVERSE)
        right3.spin(REVERSE)
    
    #until arrives at target
    while distance[-1] > distancetolerance:
        wait(10, MSEC)

        #update position
        difx = (x - xpos[-1])
        dify = (y - ypos[-1])
        distance.append(math.sqrt(difx**2 + dify**2))

        #calculate drift heading correction (capped at 10)
        targetheading = math.degrees(math.atan2(difx, dify))
        update_rotation()
        currentheading = headings[-1]
        heading_error = (targetheading - currentheading + 180) % 360 - 180
        adjustment = min(abs(heading_error) / 12, maxadjustment)

        #implement drift heading correction
        if heading_error > headingtolerance:
            leftvelocity = autonspeed
            rightvelocity = autonspeed - adjustment
        elif heading_error < -headingtolerance:
            leftvelocity = autonspeed - adjustment
            rightvelocity = autonspeed
        else:
            leftvelocity = autonspeed
            rightvelocity = autonspeed
        left_drive_bottom.set_velocity(abs(leftvelocity), PERCENT)
        left3.set_velocity(abs(leftvelocity), PERCENT)
        right_drive_bottom.set_velocity(abs(rightvelocity), PERCENT)
        right3.set_velocity(abs(rightvelocity), PERCENT)

    drivetrain_bottom.stop()
    left3.stop(FORWARD)
    right3.stop(FORWARD)


def drivetrain_control_loop():
    global acceleration, turnsensitivity, joystickdeadband
    global driverpm
    while driverpm == 360:
        #get current velocity
        currentvelocityleft = left_drive_bottom.velocity(PERCENT)
        left1.set_velocity(currentvelocityleft, PERCENT)
        currentvelocityright = right_drive_bottom.velocity(PERCENT)
        right1.set_velocity(currentvelocityright, PERCENT)

        #get target velocity
        speed_input = (controller1.axis3.position()*100/127)
        if abs(speed_input) < 0:
            speed_input = 0
        turn_input = (controller1.axis1.position()*100/127 * turnsensitivity)
        if abs(turn_input) < 0:
            turn_input = 0
        targetvelocityleft = speed_input + turn_input
        targetvelocityleft = max(-100, min(100, targetvelocityleft))
        targetvelocityright = speed_input - turn_input
        targetvelocityright = max(-100, min(100, targetvelocityright))

        #define new velocity
        newvelocityleft = currentvelocityleft + acceleration*(targetvelocityleft - currentvelocityleft)
        newvelocityright = currentvelocityright + acceleration*(targetvelocityright - currentvelocityright)

        #implement new velocity
        left_drive_bottom.set_velocity(abs(newvelocityleft), PERCENT)
        left3.set_velocity(abs(newvelocityleft), PERCENT)
        right_drive_bottom.set_velocity(abs(newvelocityright), PERCENT)
        right3.set_velocity(abs(newvelocityright), PERCENT)

        #move
        if targetvelocityleft > joystickdeadband:
            left_drive_bottom.spin(FORWARD)
            left3.spin(FORWARD)
        elif targetvelocityleft < -joystickdeadband:
            left_drive_bottom.spin(REVERSE)
            left3.spin(REVERSE)
        else:
            left_drive_bottom.stop()
            left3.stop()

        if targetvelocityright > joystickdeadband:
            right_drive_bottom.spin(FORWARD)
            right3.spin(FORWARD)
        elif targetvelocityright < -joystickdeadband:
            right_drive_bottom.spin(REVERSE)
            right3.spin(REVERSE)
        else:
            right_drive_bottom.stop()
            right3.stop()

        #wait
        wait(10, MSEC)

def test_turn_to():
    if controller1.buttonX == True:
        turn_to(0)
    if controller1.buttonA == True:
        turn_to(90)
    if controller1.buttonB == True:
        turn_to(180)
    if controller1.buttonY == True:
        turn_to(270)
    if controller1.buttonUp == True:
        turn_to(45)
    if controller1.buttonRight == True:
        turn_to(135)
    if controller1.buttonDown == True:
        turn_to(225)
    if controller1.buttonLeft == True:
        turn_to(315)
    

def when_started1():
    drivetrain_bottom.set_stopping(BRAKE)
    left1.set_max_torque(100, PERCENT)
    left2.set_max_torque(100, PERCENT)
    left3.set_stopping(BRAKE)
    right3.set_stopping(BRAKE)
    right1.set_max_torque(100, PERCENT)
    right2.set_max_torque(100, PERCENT)
    Thread(drivetrain_control_loop)
    Thread(test_turn_to)

def onauton_autonomous_0():
    drivetrain_inertial.calibrate()
    wait(20, MSEC)
    gps.calibrate()
    wait(20, MSEC)
    drivetrain_bottom.set_stopping(BRAKE)
    drivetrain_bottom.set_stopping(BRAKE)
    left3.set_stopping(BRAKE)
    right3.set_stopping(BRAKE)
    Thread(positioning_loop)
    

# create a function for handling the starting and stopping of all autonomous tasks
def vexcode_auton_function():
    # Start the autonomous control tasks
    auton_task_0 = Thread(onauton_autonomous_0 )
    # wait for the driver control period to end
    while( competition.is_autonomous() and competition.is_enabled() ):
        # wait 10 milliseconds before checking again
        wait( 10, MSEC )
    # Stop the autonomous control tasks
    auton_task_0.stop()


def vexcode_driver_function():
    # Start the driver control tasks

    # wait for the driver control period to end
    while( competition.is_driver_control() and competition.is_enabled() ):
        # wait 10 milliseconds before checking again
        wait( 10, MSEC )
    # Stop the driver control tasks


# register the competition functions
competition = Competition( vexcode_driver_function, vexcode_auton_function )


when_started1()
