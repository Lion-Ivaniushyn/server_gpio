from bottle import route, run
from gpiozero import LED, Button

leds = [LED(18),LED(21),LED(24)]
switch = Button(25)


#Status of the button in the system
def switch_status():
  if switch.is_pressed:
    return 'Wcisniety'
  else:
    return 'Niewcisniety'
#Tworzenie przycisków dla LEDow
def html_for_led(led_number):
  i = str(led_number)
  result = "<input type='button' onClick='changed(" + i +)' value='LED" + i + "'/>
  return result
@route('/')
@route('/<led_number>')
def index(led_number="n"):
  if led_number != "n":
    leds[int(led_number).toggle()]
    response = "<script>"
    response += "function changed(led)"
    response += "{"
    response += "window.location.href='/' + led"
    response += "}"
    response += "</script>"
    
    response += '<h1>Sterowanie gniazdem GPIO<h1>'
    response += '<h2>Przycisk='+switch_status()+'</h2>'
    response += '<h2>Diody</h2>'
    response += html_for_led(0)
    response += html_for_led(1)  
    response += html_for_led(2)
    return response

run(host='0.0.0.0', port=80)
