nums = [0,1,2,3,4,5,6,7,8,9]
isInteger = True
while True:
    maximumVal = str(input("Please enter a numeric input: "))
    for val in maximumVal:
        if val not in nums:
            print('You must provide a valid input')
            isInteger = False
            break
    if isInteger == False:
        continue
    else:
        maximumVal = int(maximumVal)
        if maximumVal <= 590:
            continue
    res = []
    if maximumVal == "":
        exit()
    first = 74
    if first > maximumVal:
        print(res)
        print("")
        continue
    else:
        res.append(first)
        n=first
        while n<=maximumVal:
            n = (n+4)**3
            if n<=maximumVal:
                res.append(n)
        output = str(res).replace(',',' ') #replaces a specific character in a string with another character https://www.w3schools.com/python/ref_string_replace.asp
        print(output)
        print("")

