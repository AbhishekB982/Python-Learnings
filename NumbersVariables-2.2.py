##2.2	Simple Interest Calculator - Calculate simple interest using the formula: SI = (P * R * T) / 100.

principle_amt = float(input("Enter the principle amount: "))
rate_of_interest = float(input("Enter the rate of interest: "))
time = float(input("Enter the time period in years: "))

Simple_Interest = [(principle_amt * rate_of_interest * time)/100]

print("The simple interest will be: ", Simple_Interest)