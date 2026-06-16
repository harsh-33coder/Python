import math

print("This is applicable only for a right-angled triangle")

# Get user inputs  
hgh = float(input("Enter height of triangle: "))
bse = float(input("Enter base of triangle: "))

# Calculate hypotenuse using the Pythagorean theorem
hypotenuse = math.sqrt(hgh**2 + bse**2)

print("The hypotenuse of the triangle is:", hypotenuse)
  
