#writing down pi in 100 decimal places
pi = 3.14159265358979323846264338327950288419716939937510582097494459230781640628620899862803482534211706798214808651328230664709384460955058223172535940812848111745028410270193852110555964462294895493038196

#area of a circle = pi x radius squared
#code is to calculate the area of a circle based on the radius the user inputs.
# let radius = r and Area = A

r = float(input('enter radius: '))

A = pi * (r**2)

print('Area of a circle with radius ' + str(r) + ' is ' + str(round(A, 2)))