import time
import ADS1115 as analogic
#todo verifcar instalação a import do RPi.GPIO "pip install RPi.GPIO"
#todo verificar a instalação da aplicação no raspberry


adc = analogic.ADS1115()

GAIN = 1
    '''
    Choose a gain of 1 for reading voltages from 0 to 4.09V.
    Or pick a different gain to change the range of voltages that are read:
    - 2/3 = +/-6.144V
    -   1 = +/-4.096V
    -   2 = +/-2.048V
    -   4 = +/-1.024V
    -   8 = +/-0.512V
    -  16 = +/-0.256V
    See table 3 in the ADS1015/ADS1115 datasheet for more info on gain.
    '''


print('Reading ADS1x15 values, press Ctrl-C to quit...')
print('| {0:>6} | {1:>6} | {2:>6} | {3:>6} |'.format(*range(4)))
print('-' * 37)

while True:
    values = [0]*4
    for i in range(4):
        values[i] = adc.read_adc(i, gain=GAIN)
    print('| {0:>6} | {1:>6} | {2:>6} | {3:>6} |'.format(*values))
    time.sleep(0.5)