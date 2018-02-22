# -*- coding: utf-8 -*-
"""
Created on Tue Apr 11 13:38:27 2017

@author: tanhowseng
"""

from time import sleep
import math
import libdw.util as util
import libdw.sm as sm
import libdw.gfx as gfx
from soar.io import io
from firebase import firebase

url = "https://my-awesome-project-2fdd3.firebaseio.com//" # URL to Firebase database
token = "P6WgJAORwZYOtqNNz7PFtOB40fbhfSmCN3x0wj7z" # unique token used for authentication
firebase = firebase.FirebaseApplication(url, token)
firebase.put('/','done','notdone')


        

def forward(speed, x):  #moving from x=0
    while io.SensorInput().odometry.x < x:
        print 'Sonar:'+str(io.SensorInput().sonars[2])
        if io.SensorInput().sonars[2]==0.18 or (io.SensorInput().sonars[2]>0.18 and io.SensorInput().sonars[2]<0.25):
            io.Action(fvel=0, rvel=0).execute()
            sleep(0.1)
            io.Action(0,0).execute()
        else:
            io.Action(fvel=speed, rvel=0).execute()
            sleep(0.1)
            io.Action(0,0).execute()
    #ebot.wheels(speed, speed)        
    pass 

def forwardy(speed, y): #moving from y to y=0
    while io.SensorInput().odometry.y > y:
        print 'Sonar:'+ str(io.SensorInput().sonars[2])
        if io.SensorInput().sonars[2]==0.18 or (io.SensorInput().sonars[2]>0.18 and io.SensorInput().sonars[2]<0.25):
            io.Action(0,0).execute()
            sleep(0.1)
            io.Action(0,0).execute()
           
        else:
            io.Action(speed,0).execute()
            sleep(0.1)
            io.Action(0,0).execute()
            
def forwardx(speed, x): #moving from x to 0
     while io.SensorInput().odometry.x> x:
        print 'Sonar:'+str(io.SensorInput().sonars[2])
        if io.SensorInput().sonars[2]==0.18 or (io.SensorInput().sonars[2]>0.18 and io.SensorInput().sonars[2]<0.25):
            io.Action(fvel=0, rvel=0).execute()
            sleep(0.1)
            io.Action(0,0).execute()
        else:
            io.Action(fvel=speed, rvel=0).execute()
            sleep(0.1)
            io.Action(0,0).execute()

    


#def rotate_angle(rot_angle):
#    start_angle = io.SensorInput().odometry.theta
#    angle = 0
#    while angle - start_angle < rot_angle:
#        io.Action(fvel=0, rvel=0.2).execute()
#        angle = io.SensorInput().odometry.theta
#        sleep(0.1)

def rotate_cw(speed, setangle):
    io.Action(fvel= 0, rvel= -1*speed).execute()
    sleep(5)
    io.Action(fvel=0, rvel=0).execute()    
    angle=True
    while angle :
        io.Action(fvel= 0, rvel= -1*speed).execute()
        sleep(0.1)
        io.Action(fvel=0, rvel=0).execute()
        if io.SensorInput().odometry.theta!=0:
            angle =  float(io.SensorInput().odometry.theta)>setangle
        print angle, io.SensorInput().odometry.theta
        
    #ebot.wheels(1*speed, -1*speed)
    #sleep(duration)
    pass


def rotate_ccw(speed, duration):
    io.Action(fvel=0, rvel=1*speed).execute()
    #ebot.wheels(-1*speed, 1*speed)
    sleep(duration)
    pass

def backward(speed, y): #moving from y=0
    while io.SensorInput().odometry.y < y:
        print 'Sonar:'+ str(io.SensorInput().sonars[5])
        if io.SensorInput().sonars[5]==0.18 or (io.SensorInput().sonars[5]>0.18 and io.SensorInput().sonars[5]<0.25):
            io.Action(0,0).execute()
            sleep(0.1)
            io.Action(0,0).execute()
           
        else:
            io.Action(-speed,0).execute()
            sleep(0.1)
            io.Action(0,0).execute()
    #ebot.wheels(speed, speed)
    
    pass

def gotolot1():
    print 'Now moving forward...'
    forward(0.1, 0.025)
    print (io.SensorInput().odometry)
    print 'turning clockwise...'
    #rotate_cw(1, 10)
    rotate_cw(0.1,3*math.pi/2.0+0.275)
    print io.SensorInput().odometry.theta
    print 'moving backwards...'
    backward(0.1, 0.155)
    print io.SensorInput().odometry
    firebase.put('/','done','done')
    #firebase.put('/', 'currentlot',1)
    
    pass


def gotolot2():
    print 'Now moving forward...'
    forward(0.1, 0.22)
    print (io.SensorInput().odometry)
    print 'turning clockwise...'
    #rotate_cw(1, 10)
    rotate_cw(0.1,3*math.pi/2.0+0.275)
    print io.SensorInput().odometry.theta
    print 'moving backwards...'
    backward(0.1, 0.155)
    print io.SensorInput().odometry
    firebase.put('/','done','done')
    #firebase.put('/', 'currentlot',2)    
    pass

def gotolot3():
    print 'Now moving forward...'
    forward(0.1, 0.4)
    print (io.SensorInput().odometry)
    print 'turning clockwise...'
    #rotate_cw(1, 10)
    rotate_cw(0.1,3*math.pi/2.0+0.275)
    print io.SensorInput().odometry.theta
    print 'moving backwards...'
    backward(0.1, 0.155)
    print io.SensorInput().odometry
    firebase.put('/','done','done')
    #firebase.put('/', 'currentlot',3)    
    pass

def gotolot4():
    print 'Now moving forward...'
    forward(0.1, 0.555)
    print (io.SensorInput().odometry)
    print 'turning clockwise...'
    #rotate_cw(1, 10)
    rotate_cw(0.1,3*math.pi/2.0+0.275)
    print io.SensorInput().odometry.theta
    print 'moving backwards...'
    backward(0.1, 0.155)
    print io.SensorInput().odometry
    firebase.put('/','done','done')
    #firebase.put('/', 'currentlot',4)    
    pass

def getoutlot():
    forwardy(0.1,0.09)
    rotate_cw(0.1,math.pi+0.275)
    forwardx(0.1,0)
    firebase.put('/', 'carpark', 0)

class MySMClass(sm.SM):
    startState='stop'
    def __init__(self):
        self.ls=[]
    def getNextValues(self, state, inp):
        print inp# list
        if inp not in self.ls:
            self.ls.append(inp)
        print self.ls
        if state=='stop':
            
            if  inp!=0 and type(inp)==int:
                nextState='drive'
                return (nextState, io.Action(fvel=0.0, rvel=0.0).execute())
            elif inp==0 or inp=='leave':
                state='stop'
                return (state, io.Action(fvel=0.0, rvel=0.0).execute())
            else:
                return 'error'
        elif state=='drive':
            if inp==1:
                return ('park', gotolot1())
            elif inp==2:
                return ('park', gotolot2())
            elif inp==3:
                return('park', gotolot3())
            elif inp==4:
                return ('park', gotolot4())
                
            
#            elif inp!=self.ls[0]:
#                state='park'
#                return(state, io.Action(fvel=0.0, rvel=0.0).execute())
            else:
                return 'error'
        elif state=='park':
            if inp!='leave':
                return (state, io.Action(fvel=0.0, rvel=0.0).execute() )
            else:#elif inp=='leave':
                print'I am leaving!'
                return('stop', getoutlot())
               
        
            
            
                
#            if inp.sonars[3]<=0.5 :
#                return (state, io.Action(fvel=0.1, rvel=0.5))
#            
#    
##            elif inp.sonars[1]>0.5:
##                return (state, io.Action (fvel=0.1, rvel=0.5))
#            elif inp.sonars[3]>0.5:
#                return (state, io.Action(fvel=0.1, rvel=-0.5))
#            else:
#                state==0
#                return (state,io.Action(0.0, 0.0))
mySM = MySMClass()
mySM.name = 'brainSM'

######################################################################
###
###          Brain methods
###
######################################################################

def plotSonar(sonarNum):
    robot.gfx.addDynamicPlotFunction(y=('sonar'+str(sonarNum),
                                        lambda: 
                                        io.SensorInput().sonars[sonarNum]))

# this function is called when the brain is (re)loaded
def setup():
    robot.gfx = gfx.RobotGraphics(drawSlimeTrail=True, # slime trails
                                  sonarMonitor=False) # sonar monitor widget
    
    # set robot's behavior
    robot.behavior = mySM

# this function is called when the start button is pushed
def brainStart():
    robot.behavior.start(traceTasks = robot.gfx.tasks())

# this function is called 10 times per second
def step():
#    no_commands = True
#
#    while no_commands == True:
#    # Check the value of movement_list in the database at an interval of 0.5
#    # seconds. Continue checking as long as the movement_list is not in the
#    # database (ie. it is None). If movement_list is a valid list, the program
#    # exits the while loop and controls the eBot to perform the movements
#    # specified in the movement_list in sequential order. Each movement in the
#    # list lasts exactly 1 second.
#    
#    # Get movement list from Firebase
#        movement_list = firebase.get('/carpark')
#        if movement_list!= '0':
#            no_commands = False
#        else:
#            no_commands = True
#        sleep(0.5)
    inp = firebase.get('/carpark')
    #inp=4
    print io.SensorInput().odometry.theta

    robot.behavior.step(inp)
    io.done(robot.behavior.isDone())

# called when the stop button is pushed
def brainStop():
    
    pass

# called when brain or world is reloaded (before setup)
def shutdown():
    pass