#This function will draw a 10 number lottery ticket for every player participating
#The amount of players is chosen by the user


#importing random library to use for number generation
import random

#This function will generate a lottery ticket for each player by creating an 
#empty list and filling it with random numbers between 1 and 100
#the function recives the ticket size and returns the list 'a' that is the ticket
def generate_list(ticket_size):
    a = [0]*ticket_size
    for i in range(ticket_size):
        a[i] = random.randint(1, 100)        
    return a


#this function will print the ticket
#the function receives the ticket list and the number of numbers on each ticket
#and returns nothing
def print_ticketArray(a,n):
    for i in range(n):
        print(a[i] , end = ' ' )
    return 0

#this function will find the largest sub-array of ascending numbers within the array
#and returns how many numbers the biggest sub-array has.
#the function receives the ticket list and number of numbers on the ticket
def longest_Subarray(a,n):
    j = 1
    biggest = 0
    for i in range(n-1):
        if(a[i+1]>a[i]):
            j+=1                
        else:
            if(j>biggest):
                biggest = j
            j=1
        if(j>biggest):
                biggest = j                
    return biggest

#this is the main function in charge of printing the strings and calling all the 
#functions above to complete the task at hand.
#the function receives the number of players           
def play(players):
    n = 10 #the amount of numbers on each ticket
    Biggest_SA = [] #an empty list that will house the biggest sub-array of each ticket
#This loop will generate a ticket than print it, afterwards it will find the longest sub-array
#of this ticket and add that value to the 'Biggest_SA' list
    for i in range(players):
        a = generate_list(n)
        print("Player" ,i+1,"ticket: " , end = ' ')
        print_ticketArray(a,n)
        print("\n")
        Biggest_SA.append(longest_Subarray(a,n))    
    Biggest_sorted=Biggest_SA.copy() #Creating a copy of the "Biggest_SA" list
    Biggest_sorted.sort()      #Sorting the copy to isolate the largest sub-array value
#'Winner' will recieve the first index of the 'Biggest_SA' list that houses the value of the biggest number
    Winner = Biggest_SA.index(Biggest_sorted[-1]) 
#Printing the string and adding 1 to 'Winner' cause lists start at 0
    print("***Player number" , Winner+1, "is the winner***")

#Asking the user to enter the amount of players and sending it to 'play'
play(players = int(input("Please enter the number of players: ")))
