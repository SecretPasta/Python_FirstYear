#The code will receive a number and check if ever 3
# numbers don't share the same %3
#Asking for input, will be stored in 'num'
num = int(input("Enter a number please: "))
if(num<10):#Checking if the number is a singal digit
    print("OK")#Printing 'OK' to the user
elif(num<100):#Checking if the number is a double digit
#Isolating the Dozens and performing %3 and storing in 'D'
    D = (num//10%10)%3 
#Isolating the Singles and performing %3 and storing in 'S'
    S = (num%10)%3   
    if(D==S): #Checking if 'D' and 'S' are equal
        print("Error")#Printing "Error" to the user
    else:
        print("OK")#If not Printing "OK" to the user
else:#If the number is triple digit or more
    while(num>99):#While the number is triple digit loop these lines
        trio = num%1000 #Isolating the last 3 Digits
#Isolating the Hundreds and performing %3 and storing in 'H'        
        H = (trio//100)%3
#Isolating the Dozens and performing %3 and storing in 'D'        
        D = (trio//10%10)%3 
#Isolating the Singles and performing %3 and storing in 'S'        
        S = (trio%10)%3
#Checking to see if all the number are different and doing a 'not'        
        if(not(H!=D and D!=S and H!=S)):
            print("Error")#Printing "Error" to the user
            break#Ending the loop
        num/=10 #Dividing by 10 to get rid of the last digit
    if num<99: #If the number is larger then 99   
        print("OK")#Printing "OK" to the user
        