#!/usr/bin/python

import os;
import time;

#Create a counter and pass this value to both the files
#Run this code in a loop

counter = 0
command = "/home/pi/sensor-learning/LCD.py "+ "Sleeping"
os.system(command) 
time.sleep(60)
while(counter < 1001):
   command = "/home/pi/sensor-learning/LCD.py "+ str(counter)
   print command
   os.system(command)
   command = "/home/pi/sensor-learning/continuousReading.py " + str(counter)
   print command
   os.system(command)
   time.sleep((1/3)) #sleep for 1 second
   counter+=1 
