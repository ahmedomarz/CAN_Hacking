# -*- coding: utf-8 -*-
"""
Created on Sat Dec 10 20:17:28 2016

@author: Ahmed
"""


import serial # Import pyserial library for serial interfacing with ELM327
import time # Import time library for delays


def clearArray(string, myArray):
    newArray = []
    n=len(string)
    for i,x in enumerate(myArray[n:]):
        if x!='\r' and x!='>':
            newArray.append(x)
    return newArray

            
# Define the serial connection on COM4 with baudrate 38400, no parity, 1 stop bit, 8 bytes data

elm = serial.Serial ('COM4',38400)
f = open('myData.txt','w')

#elm.isOpen()

print 'Enter your commands below\r\nInsert "exit" to leave the application'


inData = 1
outData = []

while 1:
    inData = raw_input (">>")
    if inData == 'exit':
        break
    
    else:
        elm.write(inData+'\r\n')
        time.sleep(1)
        del outData[:]
        while elm.inWaiting()>0:
            outData.append(elm.read(1))
        print outData
       
        f.write(''.join( clearArray(inData,outData) ))
elm.close()
f.close()
