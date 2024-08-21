from pymata4 import pymata4
import random
import time

board = pymata4.Pymata4()
    
led_pins = [8,9,10,11,12]
for pin in led_pins:
    board.set_pin_mode_digital_output(pin)

button_pins = [3,4,5,6,7]
for pin in button_pins:
    board.set_pin_mode_digital_input(pin)

def main():
    pinorder = []
    playing = True
    p = 4
    round_num = 1


    while playing:
        print(f'begin round {round_num}')
        pinorder.clear()
        for _ in range(p):
            pin = random.choice(led_pins)
            board.digital_write(pin,1)
            time.sleep(0.5)
            board.digital_write(pin,0)
            time.sleep(0.5)
            pinorder.append(pin)

        print(pinorder)
        
        guess = []
        current_time_elapsed = 0
        target_time = 1000
        while current_time_elapsed <= target_time:
            for i, button_pin in enumerate(button_pins):
                if board.digital_read(button_pin)[0]==1:
                    guess.append(led_pins[i])
                    while board.digital_read(button_pin)==1:
                        count += 0.1
                        time.sleep(count)
                    time.sleep(0.001)
                if len(guess) == len(pinorder):
                    break
                current_time_elapsed += 1
                time.sleep(0.01)
        print(guess)
        if guess == pinorder:
            round_num += 1
            p+=1
            print(f'well Done!, moving to round {round_num}')
        else:
            print('timeout')
            playing = False

    print('game over')
if __name__ == '__main__':
    main()