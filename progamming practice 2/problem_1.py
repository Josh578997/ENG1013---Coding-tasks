while True:
    try:
        width = float(input("Enter width in cm: "))
        length = float(input("Enter length in cm: "))
        print("""
        The perimeter with width {0}cm and length {1}cm is {2}cm.
        """.format(width,length,(2*width+2*length)))
    except:
        print("An error occured, please make sure both inputs are valid number types.")