import time
import serial

ser =serial.Serial(
    port='COM5',   #set to el COM PORT bta3ak
    baudrate=250000 #set to el Baudrate bta3 ahlk
    )

ser.isOpen()

substring1 = "STOPPED"
substring2 = "<D"

index=0
array = []
L = open("myData.txt", "r").read().splitlines();
for line in L:  # opened in text-mode; all EOLs are converted to '\n'
    line = line.rstrip('\n')
    if(substring1 not in line and substring2 not in line and line !=""):
        array.append(line)
        index=index +1

headers= []
data = []
for line in array:
    headers.append("ATSH "+line[0 : 3])
    data.append(line[4 : -3])

##counter = 0
##while counter <  index:
##    print(headers[counter])
##    print(data[counter])
##    counter = counter +1


counter = 0
ser.write('ATH1' + '\r\n')
time.sleep(0.02)
ser.write('ATAL' + '\r\n')
time.sleep(0.02)
ser.write('ATSP6' + '\r\n')
time.sleep(0.02)

##ser.write(headers[1] + '\r\n')
##time.sleep(0.02)

while counter < index:
    time.sleep(0.01)
    ser.write(headers[counter] + '\r\n')
    time.sleep(0.01)
    s = ' '
    while ser.inWaiting()>0:
            s = s + ser.read(1)
            #time.sleep(0.001)
    print(s)
    ser.write(data[1] + '\r\n')
    time.sleep(0.01)
    s = ' ' 
    while ser.inWaiting()>0:
        s = s + ser.read(1)
        #time.sleep(0.001)
    print(s)
    if ser.inWaiting()>0:
        ser.write('\r\n')
    time.sleep(0.01)
    while ser.inWaiting()>0:
        s = s + ser.read(1)
        #time.sleep(0.001)
    print(s)
    
    print(headers[counter])
    print(data[counter])
    counter = counter +1


ser.close()



