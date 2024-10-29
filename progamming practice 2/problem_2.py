price = float(input("Enter the meal price($): "))
tipPercentage = float(input("Enter the tip percentage(%): "))
numberOfFriends = int(input("Enter the number of friends you want to split the cost by(int): "))

tip = price*(tipPercentage/100)
mealTotal = price+tip
amountPerPerson = mealTotal/numberOfFriends

print("""
-The meal total (with tip) is ${0}
-Each person should pay ${1}
""".format(mealTotal,amountPerPerson))