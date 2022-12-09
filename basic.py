#Se importa la libreria de Raspberri
import RPi.GPIO as GPIO
import time

#Se establece el pin donde se conecta el sensor
lightSensor = 37

GPIO.setmode(GPIO.BOARD)
GPIO.setup(lightSensor, GPIO.IN)

try:
    while True:
        if GPIO.input(lightSensor):
            print('Luminosidad Alta')
        else:
            print('Luminosidad Baja')
            
        time.sleep(0.2)
#       Se guarda la información de luminosidad en la base de datos que consulta la app.

finally:
    GPIO.cleanup