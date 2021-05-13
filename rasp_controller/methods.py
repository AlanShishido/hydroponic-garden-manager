import random
import time
import Adafruit_ADS1x15
import RPi.GPIO as gpio
from rasp_controller import piChoices

adc = Adafruit_ADS1x15.ADS1115()
GAIN = 1


def setup_gpio_pins():
    gpio.setmode(gpio.BCM)
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


def pi_get_ph(samples: int):
    values = [0] * samples
    for i in range(samples):
        values[i] = Adafruit_ADS1x15.ADS1115().read_adc(piChoices.PI_GPIO_ADC_PH, gain=GAIN)
        time.sleep(0.2)
    ph_av = sum(values) / samples
    return ph_av


def pi_get_tds(samples: int):
    values = [0] * samples
    for i in range(samples):
        values[i] = Adafruit_ADS1x15.ADS1115().read_adc(piChoices.PI_GPIO_ADC_TDS, gain=GAIN)
        time.sleep(0.2)
    tds_av = sum(values) / samples
    return tds_av
