from bottle import route, run
from gpiozero import LED, Button

leds = [LED(18),LED(21),LED(24)]
switch = Button(25)

def switch_status():
  if switch.is_pressed:
    return 'Wcisniety'
  else:
    return 'Niewcisniety'

def html_for_led(led_number):
  i = str(led_number)
  result = "<input type='button' onClick='changed(" + i +)' value='LED" + i + "'/>
