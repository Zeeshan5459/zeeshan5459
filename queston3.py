x = float(input("Enter the temperature: "))
unit = input("Enter the unit (C, F, K): ")


if unit.upper() == "C":
  fahrenheit = 59 * x + 32
  x = x + 273.15
  print(f"{x}°C is equal to {fahrenheit}°F and {x}°K")
elif unit.upper() == "F":
  celsius = (x - 32) / 1.8
  x = (x - 32) / 1.8 + 273.15
  print(f"{x}°F is equal to {celsius}°C and {x}°K")
elif unit.upper() == "K":
  celsius = x- 273.15
  fahrenheit = (x - 273.15) * 1.8 + 32
  print(f"{x}°K is equal to {celsius}°C and {fahrenheit}°F")
else:
  print("Invalid unit. Please enter C, F, or K.")