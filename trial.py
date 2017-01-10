import serial # Import pyserial library for serial interfacing with ELM327
import time # Import time library for delays
import re

elm = serial.Serial ('COM5',250000)
f = open('myData.txt','w')

def receiveData(flag=0, flag2=0, flag3=0):
    global elm
    global f
    outData = ''
    outArray = []
    c = 0

    time.sleep(0.1)
    while elm.inWaiting()>0 or flag3==1:
        s = elm.read(1)
        c = c + 1
        if c > 7:
            flag3 = 0
        if s !='>':
            outArray.append(s)
    outData = ''.join(outArray)
    print outData

    
    if flag2 == 1:
        f.write(outData.replace('BUFFER FULL',''))
    if flag == 1:
        timeout = time.time() + 25 #time now + 1 minute (60 seconds)
        if ('BUFFER FULL' in outData) :
            while (time.time() < timeout):
                elm.write('\r\n')
                receiveData(0,1)

def main():
    global elm
    global f
    
    #f.write('>')
    
    #elm.write("ATZ\r\n")
    #receiveData()
    elm.write("ATL0\r\n")
    receiveData()
    elm.write("ATH1\r\n")
    receiveData()
    elm.write("ATS1\r\n")
    receiveData()
    elm.write("ATAL\r\n")
    receiveData()
    elm.write("ATRV\r\n")
    receiveData()
    elm.write("ATMA\r\n")
    receiveData(1,0,1)
    
    elm.close()
    f.close()

if __name__ == "__main__":
    main()

