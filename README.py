# esp-lcd-10segundos
import machine
from machine import Pin, SoftI2C
from lcd_api import LcdApi
from i2c_lcd import I2cLcd
import time

# Configuración del LCD
I2C_ADDR = 0x27
TOTAL_ROWS = 2
TOTAL_COLUMNS = 16

# Inicializa el bus I2C
i2c = SoftI2C(scl=Pin(22), sda=Pin(21), freq=10000)
lcd = I2cLcd(i2c, I2C_ADDR, TOTAL_ROWS, TOTAL_COLUMNS)

# Mensaje para desplazar
mess = " ANGEL FAJARDO - EDUARDO AUQUILLA "

# Función para desplazar texto en la pantalla LCD sin parpadeo
def scroll_text(lcd, message, delay=0.3):
    # Agrega espacios para crear el efecto de desplazamiento
    message = " " * TOTAL_COLUMNS + message + " " * TOTAL_COLUMNS
    for i in range(len(message) - TOTAL_COLUMNS + 1):
        lcd.move_to(0, 0)  # Mueve el cursor al inicio de la primera fila
        lcd.putstr(message[i:i+TOTAL_COLUMNS])  # Muestra una sección del texto
        time.sleep(delay)

# Bucle principal
while True:
    scroll_text(lcd, mess, delay=0.2)
