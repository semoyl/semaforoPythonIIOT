from machine import Pin
from utime import sleep

# Definindo os pinos dos LEDs
red = Pin(15, Pin.OUT)
yellow = Pin(16, Pin.OUT)
green = Pin(17, Pin.OUT)

print("Sistema de Semáforo Iniciado")

while True:
    # Verde - 20s
    red.off()
    yellow.off()
    green.on()
    print("Sinal Verde, Prossiga!")
    sleep(20)
    green.off()
    sleep(0.5)

    # Amarelo - 10s
    yellow.on()
    print("Sinal Amarelo, Atenção!")
    sleep(10)
    yellow.off()
    sleep(0.5)

    # Vermelho - 7s
    red.on()
    print("Sinal Vermelho, Pare!")
    sleep(7)
    red.off()
    sleep(0.5)

    