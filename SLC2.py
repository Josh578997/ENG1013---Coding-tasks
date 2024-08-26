"""SLC2.py: contains the generate_sequence function"""

__author__ = "Josh Valastro"
__date_created__ = "18/08/2024"
__Student_ID__ = "34976078"

def generate_sequence(startValue, maxValue):
    """
    a function that generates a sequence of numbers when given a start and end value

    Args:
        startValue: int - the starting value of the list, included in list output
        maxValue: float - the final value of the list is greater than this value
    """
    
    try:
        startValue = int(str(startValue))
        if not isinstance(startValue,int):
            return []
    except ValueError:
        return []
     
    try:

        if isinstance(maxValue,int):
            return []
        elif not isinstance(maxValue,float):
            if '.' in maxValue:
                pass
            else:
                return [] 
        maxValue = float(str(maxValue))
    except ValueError:
        return []
    
        
    sequence = []
    sequence.append(round(startValue,0))
    nextValue = startValue
    i = 0
    while nextValue <= maxValue:
        nextValue = round((sequence[i] + 4)**3-2.629952,0)    
        sequence.append(int(nextValue))
        i+=1
    return sequence

lst = generate_sequence(3,99999)
print(lst)