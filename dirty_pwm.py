import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False) # Ignore warning for now
GPIO.setmode(GPIO.BOARD) # Use physical pin numbering
GPIO.setup((11, 13, 15, 19), GPIO.OUT)

def pwm(pin, brightness, feq, duration):
  brightness1 = 100 - brightness 
  delay0 = 1 / feq / 100 * brightness
  delay1 = 1 / feq / 100 * brightness1
  for i in range(duration):
    GPIO.output(pin, 1)
    time.sleep(delay0)
    GPIO.output(pin, 0)
    time.sleep(delay1)

pwm((11, 13, 15, 19), 50, 100, 100)