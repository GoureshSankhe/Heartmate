
import serial # import Serial Library
import numpy  # Import numpy
import matplotlib.pyplot as plt #import matplotlib library
from drawnow import *
 
ecgF= []

arduinoData = serial.Serial('com6', 9600) #Creating our serial object named arduinoData
plt.ion() #Tell matplotlib you want interactive mode to plot live data

 
def makeFig(): #Create a function that makes our desired plot
    plt.plot(ecgF)
    
 
while True: # While loop that loops forever
    while (arduinoData.inWaiting()==0): #Wait here until there is data
        pass #do nothing
    arduinoFloat = arduinoData.readline() #read the line of text from the serial port
    ecg=arduinoFloat          #Convert second element to floating number and put in P
    ecgF.append(ecg)  
    #print(ecg)                   #Build our tempF array by appending temp readings                   #Building our pressure array by appending P readings
    drawnow(makeFig)                       #Call drawnow to update our live graph
    plt.pause(.000001)                     #Pause Briefly. Important to keep drawnow from crashing
    