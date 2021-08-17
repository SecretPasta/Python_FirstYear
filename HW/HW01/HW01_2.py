#The code will recive a number and print a triangle and a parallelogram 
n = int(input("Enter a number:")) #Asking the user for a number
i = 1 #definding an index that will start in 1 to avoid multiplication by 0
while (i<(n+1)): #While the index 'i' is smaller then the input plus one loop the following lines
#printing a blank space times the index minus one and printing '*' an uneven number of times and reducing number 
#of '*' by 2 each loop and adding another blank space twise the number minus 2 and subtracting 2 each loop
# and printing '*'times the number
    print(" "*((n-i)) + '*' * ((i*2)-1) + " "*((2*n)-(i*2)) + "*"*n )
    i+=1 #Advance the index 'i' by one
    