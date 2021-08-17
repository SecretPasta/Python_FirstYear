#The code will recive a number and show all the dividers and count how many are there
num = int(input("Please enter a number: "))#Asking for a number will be stored in 'num'
count = 0 #'count' will house the ammount of deviders
if (num == 0): #Checking if the numbers isn't '0'
    print("Infinty") #If True printing "Infinity" to the user
else: #If not proceed to the following lines
    if(num<0): #Checking if the number is negative
        i = 1 #Creating an index and defining it at '1'
        num = abs(num) #Taking the absolute unit of the number
#printing the string with the number inside and making sure the next output is on the same line    
        print("List of divsors of", num , ":" , end=' ')
        while(i<=num):#While 'i' is smaller or equal to 'num' loop the following lines
            if((num%i)==0):#Cheking the the number is a devider
                count+=1#Advancing the counter by 1
                print(i , end=' ') #Printing the devidider and making sure the next output is on the same line
            i+=1#Advancing the index by 1
        print("\n Number of divisors is: ", count)#Printing the string and the number of deviders
    else:#If the number is positive do the following lies
        i = 1#Creating an index and defining it at '1
#printing the string with the number inside and making sure the next output is on the same line   
        print("List of divsors of", num , ":" , end=' ')
        while(i<num):#While 'i' is smaller then 'num' loop the following line
            if((num%i)==0):#Cheking the the number is a devider
                count+=1 #Advancing the counter by 1
                print(i , end=' ')#Printing the devidider and making sure the next output is on the same line
            i+=1 #Advancing the index by 1
        print("\n Number of divisors is: ", count) #Printing the string and the number of deviders