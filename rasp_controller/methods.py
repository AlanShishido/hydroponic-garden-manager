import random
import time
import Adafruit_ADS1x15
import RPi.GPIO as gpio


adc = Adafruit_ADS1x15.ADS1115()
GAIN = 1


def setup_gpio_pins():
    gpio.setmode(gpio.BOARD)
    gpio.setup(5, gpio.OUT)
    gpio.setup(6, gpio.OUT)
    gpio.setup(12, gpio.OUT)
    gpio.setup(13, gpio.OUT)
    gpio.output(12, gpio.HIGH)


def get_ph_simulate():
    return random.randrange(10, 50, 1)


def get_tds_simulate():
    return random.randrange(1000, 3000, 1)


def get_temperature_simulate():
    return random.randrange(23, 32, 1)


def get_ph_rasp(samples: int):

    values = [0]*samples

    for i in samples:
        values[i] = adc.read_adc(0, gain=GAIN)
        time.sleep(0.2)

    Ph_av = sum(values) / samples
    print(Ph_av)
