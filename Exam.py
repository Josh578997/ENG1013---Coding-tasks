"""

Answer to question 36 on the 1013 exam.

Creator: Joshua Valastro
Date created: 5/11/2024
Date last modified: 5/11/2024

"""

import math

def input_sum_values():
    """
    Takes valid inputs and performs operations as specified by questions in the 1013 exam.
    Parameters: None
    Returns: resultsDict
    """
    nums = ['1','2','3','4','5','6','7','8','9','0']
    asciiLetters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    invalidVals = []
    validVals = []
    notAcceptedValues = []
    numAlpha = 0
    while True:
        valid = True
        userVal = input("Please enter a value: ")
        for char in userVal:
            if char == 'q':
                print(f'The valid inputs in list format: {validVals}')
                print(f'The list of not accepted values: {notAcceptedValues}')
                resultsDict = {"sumUserInputs":sum(validVals),"numAlphabetical":numAlpha}
                return resultsDict
            if char in asciiLetters:
                numAlpha +=1
                valid = False
                continue
            if char not in nums:
                valid = False
                break
            
        if not valid:
            invalidVals.append(char)
            print("Invalid value input")
            continue
        if int(userVal)%7 != 0:
            notAcceptedValues.append(userVal)
            print(f'The value {userVal} is not accepted')
            continue
        validVals.append(int(userVal))


if __name__ == "__main__":
    resultsDict = input_sum_values()
    print(resultsDict)