import machine
import time

led_pin = machine.Pin(2, machine.Pin.OUT) # Pin 2 controls the onboard LED

while True:
    led_pin.value(1) # Turn on the LED
    time.sleep(0.5) # Wait for half a second
    led_pin.value(0) # Turn off the LED
    time.sleep(0.5) # Wait for half a second
