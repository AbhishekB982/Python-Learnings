## 9.	Multiplication Table Generator - Input a number and print its multiplication table up to 10.

number = int(input("Enter the number to print its multiplication table up to 10: "))

print(f"\n Multiplication table for {number}:\n")

for i in range(1, 11):
    result = number * i
    print(f"{number} x {i} = {result}")
