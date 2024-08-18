def generate_sequence(startValue,maxValue) -> list[int,float]:
    """
    a function that generates a sequence of numbers when given a start and end value

    Args:
        startValue - the starting value of the list, included in list output
        maxValue - the limiting value of the list, not included in list output
    """
    if type(startValue) is not int:
        return []
    
    if type(maxValue) is not float:
        return []
    
    sequence = []
    sequence.append(round(startValue,0))
    nextValue = startValue
    while nextValue <= maxValue:
        nextValue = round((sequence[0] + 4)**13-2.629952,0)    
        sequence.append(nextValue)
    return sequence

lst = generate_sequence(3,9999999.9)
print(lst)