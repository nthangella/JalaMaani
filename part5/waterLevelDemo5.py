#!/usr/bin/python3
#Author - Nagendra Thangella
#Disclaimer - No warranties or guaranties. Use this at your own risk.
#Prior to running this program, install Rpi-GPIO using command "sudo apt-get install rpi.gpio"
import RPi.GPIO as GPIO; import datetime; import time

#Common function to write to files
def write2File(filename, mode, content):
    file = open(filename,mode) 
    file.write(content + "\r\n")
    file.close()
    return

#Define Static variables, file names and time format
#pollTime below is set to 1 second
#Besides the below pins, I use pin 1 for 3.3V and pin 34 for ground
rPin = 7; yPin = 11; gPin = 23  
rLed = 8; yLed = 12; gLed = 24; bLed = 16
pollTime = 1; prevStatus = -1 

timeFormat = "%A %B %d %Y %I:%M:%S %p"
#File name definition. Make sure the path (folder) exists
logFile = "/home/pi/logs/waterLevelStatusLog.txt"
htmlFile = "/home/pi/html/index.html"
statusFile = "/home/pi/logs/waterLevelStatus.txt"

#Get start time
monitorStartTime = datetime.datetime.now().strftime(timeFormat)
#Write monitor start time
write2File(logFile,"a+", "Monitor started at : " + str(monitorStartTime))

#Setup GPIO
GPIO.setwarnings(False); GPIO.setmode(GPIO.BOARD)
#Setup various pins
GPIO.setup([gPin,yPin,rPin], GPIO.IN, GPIO.PUD_DOWN)
GPIO.setup([bLed,gLed,yLed,rLed], GPIO.OUT, initial = 0)

#Run infintely until user interrupts
try:
    while 1:
        #Get status of input pins
        red = GPIO.input(rPin); yellow = GPIO.input(yPin); green = GPIO.input(gPin)
        status = (red * 4) + (yellow * 2) + (green * 1)
        #If status changes, set out leds accordingly and write to console 
        #Blue LED is on only if red, yellow and green are off
        if status != prevStatus:
            levelIndicator = ((("blue","green")[green == 1],"yellow")[yellow == 1],"red")[red == 1]
            GPIO.output([rLed,yLed,gLed,bLed],
                        ((status >= 4)*1,(status == 2 or status == 3)*1,(status == 1)*1, (status==0)*1))
            prevStatus = status
            currentTime = datetime.datetime.now().strftime(timeFormat)
            #Following line commented out compared to Demo2 code.
            #print ("Status of water level at %s is %s \r\n" % (currentTime, levelIndicator))
            #Write to file
            write2File(logFile,"a+", currentTime + " : " + levelIndicator)
            write2File(htmlFile,"w+", ("<html><head></head><body><p>Monitor Start Time: %s" +
                                        "<br> Last change in water level was at : %s <br>" +
                                        "</p> <br> <img src = 'images/%s.jpg' /></body></html>") 
                                        % (monitorStartTime, currentTime,  levelIndicator))
            write2File(statusFile,"w+", (" %s as on %s") % (levelIndicator, currentTime))
        time.sleep(pollTime)
#when user interrupts, cleanup and exit
except KeyboardInterrupt:
    GPIO.cleanup()
print("Exiting")
