def gen_spec_seq(num):
    """
    generates a special squences as per 1013 assignment description
    Inputs: maximumVal, can be number or list of numbers
    Outputs: Dictionary containing number of user inputs and all sequences generated
    """
    nums = ['0','1','2','3','4','5','6','7','8','9','-']
    isInteger = True
    inputCount = 0 
    allSeqs = []
    for maximumVal in num:
        inputCount+=1
        for val in str(maximumVal):
            if str(val) not in nums:
                print('You must provide a valid input')
                isInteger = False
                break
        if isInteger == False:
            continue
        else:
            if int(maximumVal) > 0:
                if len(str(maximumVal))>3:
                    print('Invalid value detected, restarting program')
                    continue
                if int(maximumVal) <= 590:
                    continue
            else:
                continue
        res = []

        first = 74
        maximumVal = int(maximumVal)
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
            allSeqs.append(output)

        return {"inputCount":inputCount,"AllSequencesGenerated":allSeqs}
    
a = [5000,4,66666]
gen_spec_seq(a)