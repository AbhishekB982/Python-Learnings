## 2.6.	Speed Calculator - Given distance in kilometers and time in hours, calculate speed in km/h.

kilometers = float(input("Enter the kilometers: "))
time_in_hours = float(input("Enter the time in hours: "))

speed_calculator = kilometers/time_in_hours

print("The speed for the given kilometers is " + str(kilometers) + " and the time in hours is " + str(time_in_hours) + " is", str(speed_calculator) + "km/h")