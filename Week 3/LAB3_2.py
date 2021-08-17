#The code will recieve three numbers from the use and calculate the perimter and area of a triangle
a , b , c = eval(input("Enter three numbers, use a comma between nubmers: \n")) #Requesting three numbers from the use that will be stored in 'a' 'b' 'c' in that order
Perimiter = a + b + c #Perimiter calculation that will be stored in variable 'Perimiter'
p = Perimiter/2 #Storing half the value of the perimiter invariable 'p' for ease of use in Heron's formula
Area = (p*(p-a)*(p-b)*(p-c))**0.5 #The variable 'Area' will reveive the area calcultion of the triangle using Heron's formula
print("The Perimter of the triangle is: %.3f"%Perimiter) #Will print the perimter of the triangle with 3 numbers after the decimal point
print("The Area of the triangle is: %.3f"%Area) #Will print the area of the triangle with 3 numbers after the decimal point