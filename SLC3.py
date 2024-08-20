from pymata4 import pymata4
import random
import time

board = pymata4.Pymata4()

def main():
    board.set_pin_mode_digital_output(8)
    board.set_pin_mode_digital_output(9)
    board.set_pin_mode_digital_output(10)
    board.set_pin_mode_digital_output(11)
    board.set_pin_mode_digital_output(12)

    pinorder = []
    for _ in range(4):
        pin = random.randint(8,12)
        board.digital_write(pin,1)
        time.sleep(0.1)
        board.digital_write(pin,0)
        time.sleep(0.8)
        pinorder.append(pin)
    print(pinorder)

    board.set_pin_mode_digital_input(3)
    board.set_pin_mode_digital_input(4)
    board.set_pin_mode_digital_input(5)
    board.set_pin_mode_digital_input(6)
    board.set_pin_mode_digital_input(7)
    
    guess = []
    current_time_elapsed = 0
    target_time = 100
    while current_time_elapsed <= target_time:
        reads = [0]
        read1 = board.digital_read(3)[0]
        if read1 is 1:
            reads.append(8)

        read2 = board.digital_read(4)[0]
        if read2 is 1:
            reads.append(9)

        read3 = board.digital_read(5)[0]
        if read3 is 1:
            reads.append(10)

        read4 = board.digital_read(6)[0]
        if read4 is 1:
            reads.append(11) 

        read5 = board.digital_read(7)[0]
        if read5 is 1:
            reads.append(12)

        current_time_elapsed+=1
        
        if reads[-1] in [8,9,10,11,12]:
            guess.append(reads[-1])
        
        time.sleep(0.1)
        if guess == pinorder:
            print('well Done!')
            break

    print('timeout')
    print(guess)
    print(reads)
if __name__ == '__main__':
    main()