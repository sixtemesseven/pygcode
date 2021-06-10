# -*- coding: utf-8 -*-
"""
Created on Mon Jun  7 22:02:28 2021

@author: justrandom
"""

import serial
import time

        
class Gcode():
    def __init__(self, comport):
        self.c = serial.Serial('COM' + str(comport), 250000, timeout=0.5)
        time.sleep(2)
        self.c.read(100000)
        #Status dictionary
        self.position = {
            "X" : 0,
            "Y" : 0,
            "Z" : 0
            }   
        self.setMM()
        
        
    def setMM(self):
        return self.sendGcodeCommand("G21")
    
    def setAbsPos(self):
        return self.sendGcodeCommand("G90")
    
    def setRelPos(self):
        return self.sendGcodeCommand("G91")
    
    def setSteps2lenght(self, axis, factor):
        cmd = 'M92 ' + str(axis) + str(factor)
        return self.sendGcodeCommand(cmd)
    
    
    
    
    
    
    
    def sendGcodeCommand(self, command):
        self.c.write(command.encode('utf_8') + b'\n')
        if(self.c.readline == b'ok\n') :
            return True
        return False

    def moveAxis(self, axis, pos):
        if self.sendGcodeCommand("G0 " + str(axis) + str(pos)) == True:
            self.position[axis] = pos
            return True
        return False
          
    def __del__(self):
        self.c.close()
    
    
        
g = Gcode(17)
g.setSteps2lenght('X', 1)
g.moveAxis('X', 100)

del g
