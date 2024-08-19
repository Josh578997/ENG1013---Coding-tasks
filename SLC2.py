"""SLC2.py: contains the generate_sequence function"""

__author__ = "Josh Valastro"
__date_created__ = "18/08/2024"
__Student_ID__ = "34976078"

def generate_sequence(startValue: int, maxValue: float) -> list[int,float]:
    """
    a function that generates a sequence of numbers when given a start and end value

    Args:
        startValue: int - the starting value of the list, included in list output
        maxValue: float - the final value of the list is greater than this value
    """
    if type(startValue) is not int:
        return []
    
    if type(maxValue) is not float:
        return []
    
    sequence = []
    sequence.append(round(startValue,0))
    nextValue = startValue
    while nextValue <= maxValue:
        nextValue = round((sequence[0] + 4)**3-2.629952,0)    
        sequence.append(nextValue)
    return sequence

lst = generate_sequence(3,9999999.9)
print(lst)