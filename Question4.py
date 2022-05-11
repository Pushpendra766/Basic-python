principle = int(input("Enter principle : "))
rate = int(input("Enter rate : "))
time = int(input("Enter time : "))
amount = principle*(pow((1+rate/100), time))
compound_intrest = amount - principle
print("Compound Interest = ", round(amount, 1))
