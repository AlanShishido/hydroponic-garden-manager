import random


def get_ph_simulate():
    return random.randrange(10, 50, 1)


def get_tds_simulate():
    return random.randrange(1000, 3000, 1)

def get_temperature_simulate():
    return random.randrange(23, 32, 1)
