#The code will receive a letter and a number and will call a
#Function to draw a triangle 

#defining a function called 'triangle' and it has two 
#variables 'letter' and 'num'
def triangle(letter,num):
#A 'for' loop that will run from the unmber entered to zero 
#substracting one in each run
    for i in range(num,0,-1):
        print(letter*i) #Printing the letter times the index value

#main function 
#asking for a letter, will be stored in 'letter'
letter = str(input("Please enter a letter: "))
#asking for a number, will be stored in 'num'
num = int(input("Pleae enter a number: "))
#Calling the function 'triangle' and sending it the values of
#'letter' and 'num'
triangle(letter,num)