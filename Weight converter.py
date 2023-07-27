weight = float(input("Enter your weight: ") )
unit = input("Killograms (kg) or Pounds (lbs): ")
if unit.lower() == "kg":
    print(f"Your weight is {round(weight * 2.205, 2)} lbs")
elif unit.upper() == "lbs":
    print(f"Your weight is {round(weight / 2.205, 2)} kgs")
else:
    print(f"{unit} is an invalid unit of measurment")