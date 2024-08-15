from pymata4 import pymata4
import time
board = pymata4.Pymata4()

def main1():
    board.set_pin_mode_digital_output(8)
    while True:
        board.digital_write(8,1)
        time.sleep(1)
        board.digital_write(8,0)
        time.sleep(0.1)
def main2():
    board.set_pin_mode_digital_input(3)
    while True:
        read = board.digital_read(3)[0]
        if read == 1:
            print("switch pressed")
        time.sleep(0.1)

def main3():
    board.set_pin_mode_digital_input(3)
    board.set_pin_mode_digital_input(4)
    board.set_pin_mode_digital_input(5)
    board.set_pin_mode_digital_input(6)
    board.set_pin_mode_digital_input(7)
    while True:
        read1 = board.digital_read(3)[0]
        if read1 == 1:
            print("switch 1 pressed")
        read2 = board.digital_read(4)[0]
        if read2 == 1:
            print("switch 2 pressed")
        read3 = board.digital_read(5)[0]
        if read3 == 1:
            print("switch 3 pressed")
        read4 = board.digital_read(6)[0]
        if read4 == 1:
            print("switch 4 pressed")
        read5 = board.digital_read(7)[0]
        if read5 == 1:
            print("switch 5 pressed")
        time.sleep(0.1)
if __name__ == '__main__':
    try:
        main3()
    except KeyboardInterrupt:
        print("Keyboard interrupt")
        exit()

