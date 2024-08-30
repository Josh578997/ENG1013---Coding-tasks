from pymata4 import pymata4
import time
board = pymata4.Pymata4()

lookupDictionary = {
    0: '11111100',
    1: '01100000',
    2: '11011010',
    3: '11110010',
    4: '01100110',
    5: '10110110',
    6: '10111110',
    7: '11100000',
    8: '11111110',
    9: '11110110',
    ' ': '00000000',
    '!': '01100001',
    '"': '01000100',
    '#': '01111110',
    '$': '10110110',
    '%': '01001011',
    '&': '01100010',
    "'": '00000100',  # Adjusted to match earlier correction for duplicate key
    '(': '10010100',
    ')': '11010000',
    '*': '10000100',
    '+': '00001110',
    '-': '00000010',
    '.': '00000001',
    '/': '01001010',
    '0': '11111100',
    '1': '01100000',
    '2': '11011010',
    '3': '11110010',
    '4': '01100110',
    '5': '10110110',
    '6': '10111110',
    '7': '11100000',
    '8': '11111110',
    '9': '11110110',
    ':': '10010000',
    ';': '10110000',
    '<': '10000110',
    '=': '00010010',
    '>': '11000010',
    '?': '11001011',
    '@': '11111010',
    'A': '11101110',
    'B': '00111110',
    'C': '10011100',
    'D': '01111010',
    'E': '10011110',
    'F': '10001110',
    'G': '10111100',
    'H': '01101110',
    'I': '00001100',
    'J': '01111000',
    'K': '10101110',
    'L': '00011100',
    'M': '10101000',
    'N': '11101100',
    'O': '11111100',
    'P': '11001110',
    'Q': '11010110',
    'R': '11001100',
    'S': '10110110',
    'T': '00011110',
    'U': '01111100',
    'V': '01111100',
    'W': '01010100',
    'X': '01101110',
    'Y': '01110110',
    'Z': '11011010',
    '[': '10011100',
    '\\': '00100110',
    ']': '11110000',
    '^': '11000100',
    '_': '00010000',
    '`': '01000000',
    'a': '11111010',
    'b': '00111110',
    'c': '00011010',
    'd': '01111010',
    'e': '11011110',
    'f': '10001110',
    'g': '11110110',
    'h': '00101110',
    'i': '00001000',
    'j': '00110000',
    'k': '10101110',
    'l': '00001100',
    'm': '00101000',
    'n': '00101010',
    'o': '00111010',
    'p': '11001110',
    'q': '11100110',
    'r': '00001010',
    's': '10110110',
    't': '00011110',
    'u': '00111000',
    'v': '00111000',
    'w': '00101000',
    'x': '01101110',
    'y': '01110110',
    'z': '11011010',
    '{': '01100010',
    '|': '00001100',
    '}': '00001110',
    '~': '10000000'
}


def dispChar(char,pos):
    for bit in lookupDictionary[char][::-1]:
        board.digital_write(8,int(bit))

        board.digital_write(10,1)
        board.digital_write(10,0)

    board.digital_write(9,1)
    board.digital_write(9,0)

    if pos == 0:
        board.digital_write(7,0)
        board.digital_write(6,1)
        board.digital_write(5,1)
        board.digital_write(4,1)
    elif pos == 1:
        board.digital_write(7,1)
        board.digital_write(6,0)
        board.digital_write(5,1)
        board.digital_write(4,1)
    elif pos == 2:
        board.digital_write(7,1)
        board.digital_write(6,1)
        board.digital_write(5,0)
        board.digital_write(4,1)
    elif pos == 3:
        board.digital_write(7,1)
        board.digital_write(6,1)
        board.digital_write(5,1)
        board.digital_write(4,0)

def dispWord(word:str) -> None:
    if len(word)>4:
        print("wordlength must be less than 4")
        exit()
    while True:
        for pos, character in enumerate(word):
            dispChar(character,pos)



pins = [4,5,6,7,8,9,10]
for pin in pins:
    board.set_pin_mode_digital_output(pin)

dispWord("OPP")
  

