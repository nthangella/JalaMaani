### Part - 1

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

### Concepts used in this part:

#### Regular water conducts electricity.
While distilled and pure water contains no salts, regularly used water contains some salts dissolved in the water. These salts give the property electrical conductivity to water. An open circuit becomes closed when both open ends come in caontact with each other.
#### Raspberry PI GPIO pins.
Many of the Raspberry Pi's GPIO (General Purpose Input Output) pins can be used to set (OUTPUT) or detect (INPUT) an electrical signal. A signal can be either HIGH or LOW. Pin configuration and their status (HIGH or LOW) can be controlled using software. Some of the pins supply power. When a power supplying pin and an INPUT pin are shorted in water, the INPUT pin's status becomes 'HIGH'. 
#### Water bottle as a water storage tank.
In the project, we will use three INPUT pins. Each pin end is at a different height relative to the power supply pin whose end will be placed at the bottom of the water. When water contacts and one or more pins is set HIGH when water connects the IN
