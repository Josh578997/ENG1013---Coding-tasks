running = True
while running:
    colorvals = {'Black':[0,1,0],'Brown':[1,10,0.01],'Red':[2,100,0.02],'Orange':[3,1000,0.03],'Yellow':[4,10000,0.04],'Green':[5,100000,0.005],'Blue':[6,1000000,0.0025],'Violet':[7,10000000,0.001],'Grey':[8,100000000,0.005],'White':[9,1000000000,None],'Gold':[None,0.1,0.05],'Silver':[None,0.01,0.1],"No band":[None,None,0.2]}
    color1 = str(input('Enter first colour value: '))
    color2 = str(input('Enter 2nd colour value: '))
    color3 = str(input('Enter 3rd colour value: '))
    multcolour = str(input('Enter multiplier color value: '))
    tolcolour = str(input('Enter tolerance colour value: '))

    resistance = int(str(colorvals[color1][0]) + str(colorvals[color2][0]) + str(colorvals[color3][0]))*colorvals[multcolour][1]
    tolerance = colorvals[tolcolour][2]

    print(f'resistance: {resistance} ohms, tolerance: +/-{tolerance*100}%')
    exitmessage = input("would you like to exit? (Yes/No)?")
    
    if exitmessage == "Yes":
        exit()