## 10.	BMI Calculator - Take weight (kg) and height (m) as input and calculate the Body Mass Index: BMI = weight / (height ** 2).

weight = float(input("Enter the weight(kg) - "))
height = float(input("Enter the height(m) - "))

print("Accepted weight is ", weight)
print("Accepted height is ", height)

body_mass_index = weight / (height ** 2)  ## In Python, ** is an exponentials operator. It means “raise to the power of”.

print("The body mass index is: ", body_mass_index)