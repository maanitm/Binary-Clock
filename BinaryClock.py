import RPi.GPIO as GPIO
import time

GPIO.setmode (GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(2,GPIO.OUT)
GPIO.setup(18,GPIO.OUT)
GPIO.setup(23,GPIO.OUT)
GPIO.setup(25,GPIO.OUT)
GPIO.setup(5,GPIO.OUT)
GPIO.setup(19,GPIO.OUT)
GPIO.setup(21,GPIO.OUT)

hourStr = time.strftime("%I")
minuteStr = time.strftime("%M")

hourInt = int(float(hourStr))
minuteInt = int(float(minuteStr))

hourBin = "{0:b}".format(hourInt)
minuteBin = "{0:b}".format(minuteInt)

hourArray = []
minuteArray = []

for hour in hourBin:
  hourArray.append(hour)

for minute in minuteBin:
  minuteArray.append(minute)

hourArray.reverse()
minuteArray.reverse()

extra = 6 - len(hourArray)

for num in range(0,extra):
  hourArray.append("0")

extra = 7 - len(minuteArray)

for num in range(0,extra):
  minuteArray.append("0")

outputsArray = [2, 18, 23, 25, 5, 19]

for out in range(0,len(hourArray)):
  if int(hourArray[out]) == 1:
    GPIO.output(outputsArray[out],GPIO.HIGH)
  else:
    GPIO.output(outputsArray[out],GPIO.LOW)

time.sleep(4)

for out in range(0,len(hourArray)):
  GPIO.output(outputsArray[out],GPIO.LOW)

time.sleep(2)

outputsArray = [2, 18, 23, 25, 5, 19, 21]

for out in range(0,len(minuteArray)):
  if int(minuteArray[out]) == 1:
    GPIO.output(outputsArray[out],GPIO.HIGH)
  else:
    GPIO.output(outputsArray[out],GPIO.LOW)

time.sleep(4)

for out in range(0,len(hourArray)):
  GPIO.output(outputsArray[out],GPIO.LOW)

time.sleep(2)
