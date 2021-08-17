#The code will recieve a 4 digit number and check if it's and Ascending,Decending and/or Arithemtic 
#Sequance or none of them 
num = int(input("Please enter a positive 4-digit number: "))#Asking the user for a 4-digit number
if(0<num<1000): #Checking if the number is between 0 and 1000
    print(num, "is not a 4-digit number. Bye Bye.") #Telling the user the number isn't 4 digits with the number
elif(num>9999):#Checking if the nubmer is above 9999
    print(num, "is not a 4-digit number. Bye Bye.")#Telling the user the number isn't 4 digits witht the nubmer    
elif(num<0):#Checking if the number is negative
        print(num, "is a negative number. Bye Bye.")#Telling the user the number is negative with the number
else:#After checking that all the conditions above arn't true the following code will begin
    T = int(num/1000)       #Isolates the Thousands and stores the value in 'T'
    H = int((num%1000)/100) #Isolates the Hundreds and stores the value in 'H'
    D = int((num%100)/10)   #Isolates the Dozebs and stores the value in 'D'
    S = int(num%10)         #Isolates the Singles and stores the value in 'S'
#Checking if each digit is bigger than the other or equal to it from left to right 
#and the delta between them isn't the same 
    if(T>=H>=D>=S and not(((S-D)==(D-H)) and ((D-H)==(H-T)))):
        print("Descending Sequance(From Left to Right)") #Printing the string to the user
#Checking if each digit is bigger than the other from left to right and the delta is the same
    elif((S>D>H>T) and ((S-D)==(D-H)) and ((D-H)==(H-T))):
        print("Ascending arithmetic sequance(From Left to Right)")#Printing the string to the user
#Checking if each digit is samller than the other from left to right and the delta is the same    
    elif((S<D<H<T) and ((S-D)==(D-H)) and ((D-H)==(H-T))):
        print("Decsending arithmetic sequance(From Left to Right)")#Printing the string to the user
#Checking if each digit is bigger than the other or equal to it from right to left
#and the delta between them isn't the same         
    elif((S>=D>=H>=T) and not(((S-D)==(D-H)) and ((D-H)==(H-T)))):
        print("Ascending sequance(From Left to Right)")
    elif( (T==H) and (H==D) and (D==S) ):#Checkig if all the Digits are the same
        print("All Digits are the same")#Printing the string to the user
    else: #The last option is the the digits are Non Ascending or Dscending
        print("Non Ascending or Dscending")#Printing the string to the user
1