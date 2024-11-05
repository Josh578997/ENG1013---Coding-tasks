"""
Solution to Question 37 on eng 1013 exam
Creator: Josh Valastro
Date Created: 5/11/2024
"""
def gen_freq_words():
    """
    Function as per specification in 1013 exam.
    parameters: None
    returns: None
    """
    invalidChars = "1234567890!@#$%^&*()_+-=<>,.?/:;"'{[}]|\~`} '
    asciiLowercase = 'abcdefghijklmnopqrstuvwxyz'
    freqDict = {}
    invalidInputs = 0
    lowercaseList = []

    for char in asciiLowercase:
        freqDict[char] = 0
    while True:
        valid = False
        try:
            userVal = input('Enter a value: ')
            for char in userVal:
                if char in invalidChars:
                    print(f'input should contain no numbers or symbols')
                    invalidInputs+=1
                    break
                if char in asciiLowercase:
                    valid = True
                    freqDict[char] += 1
            if valid == True:
                lowercaseList.append(userVal)
                continue
        except KeyboardInterrupt:
            print("The letters accepted were:\n")
            for key in freqDict:
                if freqDict[key] > 0:
                    print(f"{key} : {freqDict[key]} times\n")
            print(f'The total number of valid inputs was: {len(lowercaseList)}\n')
            print(f'The total number of invalid inputs was {invalidInputs}')
            exit()

if __name__ == "__main__":
    gen_freq_words()