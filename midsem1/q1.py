a = 9
b = 9.1

def doSomething():
    global a
    c = 12/b 
    a+=c

doSomething()
doSomething()

print(round(a,2))