from pymata4 import pymata4
import time

board = pymata4.Pymata4()
while True:
    board.set_pin_mode_analog_input(0)
    pin = (board.analog_read(0)[0])*(5/1023 )
    print(pin)
    time.sleep(1)