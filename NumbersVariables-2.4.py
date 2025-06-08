## 4.	Swap Two Variables - Write a program to swap the values of two variables.

variable1 = float(input("Enter Variable 1: "))
variable2 = float(input("Enter Variable 2: "))

print("Current values of varibales:", variable1, variable2)


print("Swapping the values of variables:")

tmp_var = variable1
variable1 = variable2
variable2 = tmp_var

print("The swapped values are as follows: ", variable1, variable2)