lookupDictionary = {"0":"1111110","1":'0110000',"2":"1101101",'3':'1111001','4':'0110011','5':'1011011','6':'1011111',
                    '7':'1110000','8':"1111111",'9':'1111011',
                    'A':'1110111', 'a':'1111101','b':'0011111','C':'1001110','c':'0001101','d':'0111101','E':'1001111','F':'1000111',
                    'G':'1011110','H':'0110111','h':'0010111','I':'0000110','J':'0111100','L':'0001110','n':'0010101','O':'1111110',
                    'o':'0011101','P':'1100111','q':'1110011','r':'0000101','S':'1011011',"t":'0001111','U':'0111110','u':'0011100',
                    'y':'0111011'}

char = input('please enter a character: ')
charlist = []
for char in char:
    charlist.append(char)

for char in charlist:
    if char in lookupDictionary:
        print(lookupDictionary[char])
    else:
        print('character not in lookup dictionary')