#!/usr/bin/python3
#Author - Nagendra Thangella
#Disclaimer - No warranties or guaranties. Use this at your own risk.
#Prior to running this program, install Rpi-GPIO using command "sudo apt-get install rpi.gpio"
import RPi.GPIO as GPIO; import datetime; import time

#Define Static variables, file names and time format
#pollTime below is set to 1 second
#Besides the below pins, I use pin 1 for 3.3V and pin 34 for ground
rPin = 7; yPin = 11; gPin = 23  
rLed = 8; yLed = 12; gLed = 24; bLed = 16 
pollTime = 1; prevStatus = -1; timeFormat = "%I:%M:%S %p"

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
            print ("Status of water level at %s is %s \r\n" % (currentTime, levelIndicator))
        time.sleep(pollTime)
#when user interrupts, cleanup and exit
except KeyboardInterrupt:
    GPIO.cleanup()
print("Exiting")