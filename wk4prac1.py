from unitconverter import temperature

convertFrom = input("Enter unit you wish to convert from: ")
convertTo = input("Enter unit you wish to convert to: ")
Val = input("Enter the value you wish to convert: ")

print(f'{Val} in {convertFrom} is {temperature(convertFrom,convertTo,Val)} in {convertTo}')