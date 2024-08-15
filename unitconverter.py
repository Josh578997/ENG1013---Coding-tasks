# Module Converter
# Version 1.0
# Author: ENG1013
# License: MIT

def temperature(fromUnit, toUnit, value):
    """
        convert between temperature units
        parameters:
            fromUnit (str): unit to convert from. Accepts "K", "F", "R", "D", "C"
            toUnit (str): unit to convert to. Accepts "K", "F", "R", "D", "C"
            value (float/int): value to convert.
    """
    # Convert to a common unit, C
    if fromUnit == 'K':
        conVal = value  - 273.15 
    elif fromUnit =='F':
        conVal = (value -32)*(5/9)
    elif fromUnit == 'R':
        conVal = (value -491.67)*(5/9)
    elif fromUnit =='D':
        conVal = 100 - (value )*(2/3)
    else:
        conVal = value 
    
    # Convert from C to required unit
    if toUnit == 'K':
        conVal = conVal + 273.15
    elif toUnit =='F':
        conVal = (conVal*9/5) +32
    elif toUnit == 'R':
        conVal = (conVal*9/5) +491.67
    elif toUnit =='D':
        conVal = (100 - conVal)*3/2
    else:
        conVal = conVal

    # Return converted value
    return conVal


# print(temperature("C","K",100))