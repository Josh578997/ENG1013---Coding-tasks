"""
Speeding Penalty in Taylorsville Calculator
Author: Josh Valastro
Date: 11/08/2024
Last Modified: 12/08/2024
ID: 34976078
"""
while True:
    roadSpeed = input("Please enter the road speed limit in km/h: ")
    try:
        roadSpeed = int(roadSpeed)
    except:
        print('invalid input')
        continue
    if not (30<= roadSpeed <= 120):
        print('invalid input')
        continue

    try:
        vehicleSpeed = float(input("Please enter the vehicle speed in km/h: "))
    except:
        print('invalid input')
        continue

    if vehicleSpeed <0:
        print('invalid input')
        continue
    speedExeeded = round(vehicleSpeed - float(roadSpeed),3)
    penaltyAmount = None
    licenseSuspension = None
    demeritPoints = None

    if speedExeeded > 0:

        if roadSpeed == 110 and (20 <= speedExeeded < 25):
            penaltyAmount = 370
            licenseSuspension = 3
        elif speedExeeded >= 45:
            penaltyAmount = 925
            licenseSuspension = 12
        elif speedExeeded >= 40:
            penaltyAmount = 786
            licenseSuspension = 6
        elif speedExeeded >= 35:
            penaltyAmount = 693
            licenseSuspension = 6
        elif speedExeeded >= 30:
            penaltyAmount = 601
            licenseSuspension = 3
        elif speedExeeded >= 25:
            penaltyAmount = 509
            licenseSuspension = 3
        elif speedExeeded >= 10:
            penaltyAmount = 370
            demeritPoints = 3
        else:
            penaltyAmount = 231
            demeritPoints = 1


        
    else:
        print('speed limit not exceeded')
        continue

    if demeritPoints is None:
        print(f'amount speed limit exceeded by = {speedExeeded:.2f}\npenalty = ${penaltyAmount:.2f}\nlicense suspension = {licenseSuspension} months ')
    
 
    elif licenseSuspension is None:
        print(f'amount speed limit exceeded by = {speedExeeded:.2f}\npenalty = ${penaltyAmount:.2f}\ndemerit points = {licenseSuspension} points ')
    cont = input("Do you want to rerun(Y/N)?: ")
    if cont == "N":
        break
    


