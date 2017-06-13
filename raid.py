import time
from time import gmtime, localtime
import datetime
import RPi.GPIO as GPIO

from DbClass import DbClass

GPIO.setmode(GPIO.BCM)
PIR_PIN = 8
LED_PIN = 21
GPIO.setup(PIR_PIN, GPIO.IN)
GPIO.setup(LED_PIN, GPIO.OUT)

tijdStart = 0
tijdEinde = 0
tijdStart = time.time()

#Starttijd DB
tijdstipStart = time.strftime("%Y-%m-%d %H:%M:%S", localtime())
print(tijdstipStart)

temp = DbClass()
temp.setDataToDatabaseBoekCursus(tijdstipStart)



def MOTION(PIR_PIN):
    global tijdStart
    print("Motion Detected!")
    tijdEinde = time.time()
    calculateTime(tijdStart, tijdEinde)
    tijdStart = time.time()


def calculateTime(pTijdStart, pTijdEinde):
    tijd = pTijdEinde - pTijdStart
    print(tijd)




print("PIR Module Test (CTRL+C to exit)")
time.sleep(2)
print("Ready")

try:
    GPIO.add_event_detect(PIR_PIN, GPIO.RISING, callback=MOTION)
    while 1:
       time.sleep(100)
except KeyboardInterrupt:
    print("Quit")
    GPIO.cleanup()

