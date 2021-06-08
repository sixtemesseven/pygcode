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
g.moveAxis('X', 10)
