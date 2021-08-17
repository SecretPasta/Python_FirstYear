#The code will accept 4 points from the user, calculate the incline of 
#each line and calculate the point of intersection
#Ask for 2 points of the first line
A1_x , A1_y , A2_x , A2_y = eval(input("Enter Line A Data: "))
#Ask for  2 points of the second line
B1_x , B1_y , B2_x , B2_y = eval(input("Enter Line B Data: "))
mA = (A2_y - A1_y)/(A2_x - A1_x)#Calculating inclination of Line A
mB = (B2_y - B1_y)/(B2_x - B1_x)#Calculating inclination of Line B
x = ( (mA*A1_x) - (mB*B1_x) + B1_y - A1_y ) / (mA-mB) #Calculation of the X Axis Coordinate 
y =( (mA*x) - mA*A1_x + A1_y )#Calculation of the Y Axis Coordinate 
print("x = %.1f"%x + "y = %.1f"%y)#Printing the result to the user
