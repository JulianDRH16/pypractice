side_a = float(input("Insert the side 'a' of a triangle "))
side_b = float(input("Insert the side 'b' of a triangle "))

side_c = ((side_a)**2 + (side_b)**2)**(1/2)

print(f"The hypotenuse of the triangle is {side_c}")

x_1 = ((-side_b) + ((side_b)**2 - 4*(side_a*side_c) )*(1/2) )/(2*side_a)
x_2 = ((-side_b) - ((side_b)**2 - 4*(side_a*side_c) )*(1/2) )/(2*side_a)

print(f"The solution X1 for cuadratic is {x_1}")
print(f"The solution X2 for cuadratic is {x_2}")