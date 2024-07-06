a = float(input("Enter side a: "))
b = float(input("Enter side b: "))
c = float(input("Enter side c: "))
if a == b == c:
  print("The triangle is equilateral.")
elif a == b or b == c or c == a:
  print("The triangle is isosceles.")
else:
  print("The triangle is scalene.")