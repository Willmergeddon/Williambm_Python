import serial

#Global Variables
s = 0

#Innitialises serial port communication
def init_serial():
    CM = 1          #the port
    global s          
    s = serial.Serial()    
    s.baudrate = 9600
    s.port = CM
    s.open()        

    #test variable to check if open
    if ser.isOpen():
        print 'Open: ' + ser.portstr

        