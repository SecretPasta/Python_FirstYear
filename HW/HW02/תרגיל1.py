import random

def generate_list(ticket_size):
    a = [0]*ticket_size
    for i in range(0,ticket_size):
        a[i] = random.randint(1, 100)        
    return a

def print_ticketArray(a,n):
    for i in range(n):
        print(a[i] , end = ' ')
    return 0

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
            

def play(players):
    n = 10
    Biggest = []
    Winner = 0
    for i in range(players):
        a = generate_list(n)
        print("Player" ,i+1,"tickets: " , end = ' ')
        print_ticketArray(a,n)
        print("\n")
        Biggest.append(longest_Subarray(a,n))
    print(Biggest)
    
    Biggest_sorted=Biggest.copy()
    Biggest_sorted.sort()
    T = Biggest_sorted[-1]
    print(T)
    Winner = Biggest.index(T)
        
    print("***Player number" , Winner+1, "is the winner***")
            
    return 0   
 
        
play(players = int(input("Please enter the number of players: ")))
#play(10)  
#generate_list(10)
#a = [1,2,3,2,1,2,3,4,5,9]
#print(longest_Subarray(a, 10))

