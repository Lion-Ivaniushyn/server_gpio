from gpiozero import LED
from gpiozero import PWMOutputDevice
from gpiozero import DigitalOutputDevice
from gpiozero import App, PushButton
from gpiozero import Slider
from time import sleep

pin = PWMOutputDevice(18)

##############################################################
Buttons ON/OFF
##############################################################
def start():
  start_button.disable()
  start_button.enable()
  pin.on()

def stop():
  start_button.enable()
  stop_button.disable()
  pin.off()

app = App(width=100, height=150)
start_button=PushButton(app, command=start, text="On")
start_button.text_size = 30
start_button = PushButton(app, command=stop, text="Off", enabled=False)
app.display()

##############################################################
Slider
##############################################################
def slider_changed(percent):
  pin.value = int(percent)/100
app = App(title='Regulacja mocy(PWM)', width=500, height=150)
slider = Slider(app, command=slider_changed, width='fill', height=500)
slider.test_size=30
app.display()

###############################################################
LED Control
###############################################################
#led = LED(18)

#while True:
#  led.on()
#  sleep(0.5)
#  led.off()
#  sleep(0.5)
