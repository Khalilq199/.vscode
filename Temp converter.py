unit = input("Is this temperature in Celcius or Farenheit (C / F)?: ")
temp = float(input("Enter the temperature: "))
if unit.lower() == "c":
    print(f"The temperature in Farenheit is {round((temp * (9/5)) + 32, 2)} degrees")
elif unit.lower() == "f":
    print(f"The temperature in Celsius is {round((temp - 32) * (5/9), 2)} degrees")
else:
    print("The unit is invalid")