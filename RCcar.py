import cv2
from collections import Counter
from module import findnameoflandmark,findpostion,speak
import math
import time
import RPi.GPIO as GPIO
from datetime import datetime


cap = cv2.VideoCapture(0)
tip=[8,12,16,20]
tipname=[8,12,16,20]
fingers=[]
finger=[]

# Set the GPIO mode to BCM
GPIO.setmode(GPIO.BCM)

# Define the GPIO pins for motor control
motor1_in1 = 5  
motor1_in2 = 6  
motor2_in1 = 13  
motor2_in2 = 19  
motor1_pwm_pin = 20  
motor2_pwm_pin = 21  

# Set up the GPIO pins as output
GPIO.setup(motor1_in1, GPIO.OUT)
GPIO.setup(motor1_in2, GPIO.OUT)
GPIO.setup(motor2_in1, GPIO.OUT)
GPIO.setup(motor2_in2, GPIO.OUT)
GPIO.setup(motor1_pwm_pin, GPIO.OUT)
GPIO.setup(motor2_pwm_pin, GPIO.OUT)

# Set up PWM for speed control
frequency = 100  
motor1_pwm = GPIO.PWM(motor1_pwm_pin, frequency)
motor2_pwm = GPIO.PWM(motor2_pwm_pin, frequency)





# Function to move the car forward with speed control
def move_forward(speed):
    GPIO.output(motor1_in1, GPIO.HIGH)
    GPIO.output(motor1_in2, GPIO.LOW)
    GPIO.output(motor2_in1, GPIO.HIGH)
    GPIO.output(motor2_in2, GPIO.LOW)
    motor1_pwm.start(speed)
    motor2_pwm.start(speed)

# Function to move the car backward with speed control
def move_backward(speed):
    GPIO.output(motor1_in1, GPIO.LOW)
    GPIO.output(motor1_in2, GPIO.HIGH)
    GPIO.output(motor2_in1, GPIO.LOW)
    GPIO.output(motor2_in2, GPIO.HIGH)
    motor1_pwm.start(speed)
    motor2_pwm.start(speed)

# Cleanup GPIO settings on program exit
def cleanup():
    motor1_pwm.stop()
    motor2_pwm.stop()

    

#Create an infinite loop which will produce the live feed to our desktop and that will search for hands
while True:
     ret, frame = cap.read() 
     
     
     #Determines the frame size, 640 x 480 offers a nice balance between speed and accurate identification
     frame1 = cv2.resize(frame, (640, 480))
    
    #Below is used to determine location of the joints of the fingers 
     pos=findpostion(frame1)
     landmark=findnameoflandmark(frame1)
     
    
     
     if len(landmark and pos)!=0:
        finger=[]
        if pos[0][1:] < pos[4][1:]: 
           
           print (landmark[4])
          
        else:
           
            pass
        
        fingers=[] 
        for id in range(0,4):
            if pos[tip[id]][2:] < pos[tip[id]-2][2:]:
               

               fingers.append(1)
    
            else:
               fingers.append(0)

        x=fingers + finger
        c=Counter(x)
        fingerNum=c[1]
        
     else:
        fingerNum = 9
     
     if fingerNum == 4:
      move_forward(20)
     elif fingerNum == 3:
      move_backward(20)
     elif fingerNum == 0:
      cleanup()
     elif fingerNum == 2:
      current_time = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
      filename = f'{current_time}.jpg'
      cv2.imwrite(filename, frame1)
     else:
      cleanup()

     
     
     
     cv2.imshow("Frame", frame1);
     key = cv2.waitKey(1) & 0xFF
     
     
     
     #Below states that if the |s| is press on the keyboard it will stop the system
     if key == ord("s"):
       break
