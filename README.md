# JalaMaani


In an Indian language, `Jala` means water and `Maani` means a measuring device. This repository has the code to build a simple water level monitor using Raspberry Pi and expose the monitor via web and Amazon Alexa.

I split the project into five parts to simplify the understanding of the code build. I am hoping that this creates interest in youngsters as well elders to get a grasp on using very cost effective devices to build great stuff. I made videos of each part and uploaded them to YouTube. You can find those links below.

## Part - 1

In this part we will build a simple water level monitor using simple materials and Raspberry Pi. The console shows the status as blue, green, yellow and red depending on the water level. GPIO pins are used to capture the water level.

[Video Link](https://youtu.be/5YWfMaGPp3I) - https://youtu.be/5YWfMaGPp3I

Required materials to complete this part:

- [Raspberry Pi](https://www.raspberrypi.org/products/) any model. Older and zero models have lesser processing power. Pi 3 is recommended. 
- [Raspbian Stretch](https://www.raspberrypi.org/downloads/raspbian/) with desktop operating system, installed on the Pi. 
- Most likely already installed [Python3](https://www.python.org/downloads/) software 
- GPIO Pyhton module. Install using the command 'sudo apt-get install rpi-gpio'.
- A folder named 'code' under the Pi home folder /home/pi/code. Command `mkdir /home/pi/code`.
- [Balsa Stick](https://www.hobbylobby.com/Crafts-Hobbies/Painting-Surfaces/Wood/36-Balsa-Stick-Pack/p/20138). You can find small kids using balsa stick for their creative school projects. Any piece of thin wood stick works.
- A cable with four wires. This project uses a old phone cable with black, green, yellow and red colored wires.
- Dupont jumper connectors. Search on eBay. 
- Bottle of regular tap water. Pure and distilled water may not work.
- Electrical tape.

## Part - 2

In this part we will extend the code built in Part-1 to indicate the water level by litting appropriate colored LED (light emitting diode). 

[Video Link](https://youtu.be/mLumtc2Q0uA) - https://youtu.be/mLumtc2Q0uA

Additional materials to complete this part:

- Bread Board
- Four colored LEDs - This project uses blue, green, yellow and red colored LEDs
- Optional t-Cobbler connector. This helps making connections very easy but not a must.
- Two resistors of 300 ohms. To reduce current levels in the circuits, I ultimately ended up using 5K resistors.

## Part - 3

In this part, we will further extend the code to capture the status to a file for purposes of history. Additionally we will learn how to  run the code in background upon reboot of the Raspberry Pi.

[Video Link](https://youtu.be/ERrCAJt_940) -https://youtu.be/ERrCAJt_940

Additional materials to complete this part:

- Create a folder 

## Part - 4

How can you monitor the water level from anywhere in the world? This part shows how to expose the water level monitor over internet.

[Video Link](https://youtu.be/xBGxMl_61Mw) -https://youtu.be/xBGxMl_61Mw

Additional materials to complete this part:

- NodeJs software. It may have been already installed on the Pi.
- Express, a NodeJS module.


## Part - 5

Did you ever have a reliable and loyal assistant? Alexa can help you get the status of water level monitor status. In this part, we will  show how to integrate our monitor with Amazon Alexa.

[Video Link](https://youtu.be/2s9v6wwBHQc) -https://youtu.be/2s9v6wwBHQc

Additional materials to complete this part:

- Account to use Amazon Web Services - [AWS](https://aws.amazon.com/)
- Account to access [Amazon developer portal](https://developer.amazon.com/).
- Any [Alexa device](https://www.amazon.com/Amazon-Echo-And-Alexa-Devices/b?ie=UTF8&node=9818047011) or Alexa application.

