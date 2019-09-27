
How can you monitor the water level from anywhere in the world? This part shows how to expose the water level monitor over internet.

[Video Link](https://youtu.be/xBGxMl_61Mw) -https://youtu.be/xBGxMl_61Mw

Additional materials to complete this part:

- NodeJs software. It may have been already installed on the Pi.
- Express, a NodeJS module.
- Access to your network router to forward web requests to the server where you run this code.
- Your internet public IP address


### How to run the code:

- Use help guide that comes with your router to setup a port forward request. This code listens on the port 8900.
- On google.com, type 'what is my IP address'. In results you can see your network's public address.
- Download the above code files to your folder '/home/pi/code'.
- Open a console and type the command `python3 /home/pi/code/waterLevelDemo4.py`
- Open another console and type the command `nodejs /home/pi/code/waterLevelStatusServerDemo4.js`
- To stop the code, press ctrl+c on both opened cosoles.
- Open browser window and type "localhost:8900" in url box.
- You should be able to see the water level status.
- On the browser now enter <publicIpAddress>:8900. You should see the status.
