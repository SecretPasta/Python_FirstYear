#The code will recieve the area of a right triangle and is isosceles and calulate the sides of it
Triangle = float(input("Please enter the area of a right triangle and is isosceles: " )) #Requesting the user to input the area of the triangle, will be stored in 'Triangle'
side = (Triangle*2)**0.5 #Calulating the side by reversing the triangle area formula
c = (side**2 + side**2)**0.5 #The variable 'c' will receive the calculation of the third side using Pythagoras' Formula
print("Side A %.2f"%side + " Side B %.2f"%side + " Side C %.2f"%c  ) #Printing the sides of the triangle with 2 numbers after the decimal point
