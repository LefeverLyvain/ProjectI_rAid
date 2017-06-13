import time
import RPi.GPIO as GPIO

# GPIO.setmode(GPIO.BCM)
# pir = 8
# led = 21
# GPIO.setup(pir, GPIO.IN)
# GPIO.setup(led, GPIO.OUT)



# while True:
   # i = GPIO.input(pir)
   # if i == 1:
   #    print("Motion detected!")
   #    GPIO.output(led, GPIO.HIGH)
   #    time.sleep(0.9)
   #
   #    tijdEinde = time.time()
   #    tijd = tijdEinde - tijdStart
   #    print(tijd)
   # else:
   #    print("No motion detected!")
   #    GPIO.output(led, GPIO.LOW)
   #    time.sleep(0.9)
   # time.sleep(0.1)

GPIO.setmode(GPIO.BCM)
PIR_PIN = 8
LED_PIN = 21
GPIO.setup(PIR_PIN, GPIO.IN)
GPIO.setup(LED_PIN, GPIO.OUT)

tijdStart = 0
tijdEinde = 0

tijdStart = time.time()

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

