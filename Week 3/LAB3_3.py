#The code will recive 2 sides of a triangle, calculate the third side,primter, area and will print the results to the user
a , b = eval(input("Enter triangle sides, use a comma between the numbers: \n")) #Requesting 2 numbers from the user,will be stored in 'a' , 'b'
c = (a**2 + b**2)**0.5 #The variable 'c' will receive the calculation of the third side using Pythagoras' Formula
Perimter = a + b + c #The varaible 'Perimiter' will recive the perimiter calculation
Area = a*b/2 #The variable 'Area' will recieve the area calculation
print("The Perimiter is: %.3f"%Perimter) #Printing the value stored in Perimter with 3 numbers after the decimal point with the string beforehand 
print("The area is: %.3f"%Area) #Printing the value stored in Area with 3 numbers after the decimal point with the string beforehand 
