try:
    mthincome = float(input("Enter your monthly income ($): "))
    mthexpenses = float(input("Enter your fixed expenses ($): "))
    mthvarexpenses = float(input("Enter your variable expenses ($): "))
    mthSavingsGoal = float(input("Enter your monthly savings goal ($): "))
except:
    print("All datatypes must be numeric")

if mthincome < 0 or mthexpenses < 0 or mthvarexpenses < 0 or mthSavingsGoal < 0:
    print("invalid amount")

totalExpenses = mthexpenses + mthvarexpenses
totalSavings = mthincome - totalExpenses

percentage = totalSavings/mthSavingsGoal

if percentage 

