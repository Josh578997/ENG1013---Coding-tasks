def genarate_multiplication_table(tableNum:int,min:int,max:int) -> str:
    count = min
    outstr = ''
    while count<=max:
        mulStr = f'\n{tableNum} x {count} = {tableNum*count}'
        outstr = outstr + mulStr
        count += 1
    return outstr

if __name__ == "__main__":
    print(genarate_multiplication_table(24,1,12))
