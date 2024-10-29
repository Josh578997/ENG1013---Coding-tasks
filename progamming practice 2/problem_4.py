def generate_fibonacci_sequence(n,maxVal):
    try:
        n = int(n)
        maxVal = int(maxVal)
    except ValueError:
        return []
    if maxVal <= n or maxVal <= 2 or type(n) is not int or type(maxVal) is not int:
        return []
    
    
    n1 = 0
    n2= 1
    output = [n1,n2]
    next = n2
    while next <= maxVal and len(output)<=n:
        output.append(next)
        n1,n2 = n2,next
        next = n1+n2
    return output
if __name__ == "__main__":
    print(generate_fibonacci_sequence(9,10))