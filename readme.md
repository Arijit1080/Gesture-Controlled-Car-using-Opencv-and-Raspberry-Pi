# Hand Gesture Controlled Car

This project is a Python program that uses OpenCV and Mediapipe to detect hand gestures and control a car using Raspberry Pi and GPIO pins. The program can recognize five different hand gestures and perform corresponding actions:

- Four fingers up: Move the car forward with speed control
- Three fingers up: Move the car backward with speed control
- Zero fingers up: Stop the car and clean up GPIO settings
- Two fingers up: Take a photo of the current frame and save it with timestamp
- One finger up: No action

## Features

- The program uses a webcam to capture the live video feed and display it on the screen.
- The program uses the Mediapipe library to detect the hand landmarks and find the position and name of each finger joint.
- The program uses the OpenCV library to process the image and draw circles on the detected landmarks.
- The program uses the RPi.GPIO library to set up the GPIO pins and control the motor speed and direction using PWM signals.
- The program can handle multiple hand gestures and execute different commands based on the number of fingers up.

## Requirements

- Python 3.7 or higher
- OpenCV 4.5.3 or higher
- Mediapipe 0.8.7 or higher
- RPi.GPIO 0.7.0 or higher
- A Raspberry Pi board with GPIO pins
- A webcam or a camera module connected to the Raspberry Pi
- A DC motor driver module connected to the GPIO pins
- A car chassis with two DC motors and wheels

## Installation

To install the required libraries, run the following commands in your terminal:

```bash
pip install opencv-python
pip install mediapipe
pip install RPi.GPIO
pip uninstall protobuf
pip install protobuf==3.20
pip install gTTs
``````

To clone this repository, run the following command in your terminal:

```
git clone https://github.com/yourusername/hand-gesture-controlled-car.git
```

## Usage

To run the program, navigate to the project directory and run the following command in your terminal:

```
python3 RCcar.py
```

The program will start capturing the video feed from your webcam or camera module and display it on the screen. You can see the hand landmarks drawn on your hand as you move it in front of the camera. You can also see the name and position of each finger joint printed on the terminal.

To control the car, make one of the five hand gestures and hold it for a few seconds. The program will recognize your gesture and send commands to the GPIO pins to control the motor driver module. You can see the action performed by the car on the screen.

To stop the program, press ```s``` on your keyboard. The program will stop capturing the video feed, clean up the GPIO settings, and exit.

## Circuit Diagram

![dc_motor_devre_bb](https://github.com/Arijit1080/Gesture-Controlled-Car-using-Opencv-and-Raspberry-Pi/blob/main/RC_car_circuit.png)



## Demo

Demo
Here is a video demonstration of how this project works:

[![Hand Gesture Controlled Car Demo]]

