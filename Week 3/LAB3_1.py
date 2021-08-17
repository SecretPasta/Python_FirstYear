#The code will receive a number from the user and perform  an equation and out put the equation and result
x = float(input("Please enter a number: ")) #Asking the user for an input, will be stored in 'x'
answer = x + (x**(1/3)+x**2)**0.5 #The variable 'answer' will reieve the result of the equation
equation = "{}+sqrt({}^(1/3)+{}^2)=" #The varaible 'equation' will recieve a string that conatins the equation itself with the curly braces being placeholders for variables
print(equation.format(x,x,x),"%.2f"%answer) #printing the string that is stored in 'equation' and replacing each curly braces with the vaule of 'x' and printing the value of 'answer' with 2 numbers after the decimal point