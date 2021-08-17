#The code will recive a note and two numbers and perfrom and action with those numbers based on the
#Note that has been entered
while 1: #An infinite loop
#Printing the table of contents of each note and the assosiated action it will perform
    N = str(input('''Enter a char: 
a or A for Average
*    Multiply
m    minimum
M    maximum
^    Power 
Q or q to quit\n'''))
    if(N=='Q' or N=='q'): #Checking if the note is 'q' or 'Q'
        print("Finish") #If so printing "Finish" to the user
        break#Ending the inifinite loop
    d1,d2 = eval(input("Enter two integers: ")) #Asking for 2 integers, will be stored in 'd1'&'d2'
    if(N == 'a' or N == 'A'):#Checking if the note is 'a' or 'A'
        ans = (d1+d2)/2 #'ans' will recieve the average of the two numbers
        if((ans%1)== 0):#Checkig if the answer is an integer
            print("The average is an integer number: ",ans) #if so will print the string with 'ans'
        else:#if the number isn't an integer
            print("The average is not an integer number: ",ans)#will print the string with 'ans'
    elif(N == '*'):#Checking if the note is '*'
        ans = d1*d2 #'ans' will get the multiplication of the two numbers
        print("The multiplication is: ",ans)#will print the string with 'ans'
    elif(N == 'M'):#Checking if the note is 'M''
        if(d1>=d2): #Checking if 'd1' is bigger than 'd2' and taking into account they might be equal
            print("The bigger number is: ",d1)#will print the string with 'd1' 
        else:#if the other way around is true
            print("The bigger number is: ",d2)#will print the string with 'd2'
    elif(N == 'm'):#Checking if the note is 'm'
        if(d1<=d2):#Checking if 'd1' is smaller than 'd2' and taking into account they might be equal
            print("The smaller number is: ",d1) #will print the string with 'd1'  
        else:#if the other way around is true
            print("The smaller number is: ",d2)#will print the string with 'd2'
    elif(N == '^'):#Checking if the note is '^'
        if(d1==0 and d2<=0):#Checking to make sure we're not deviding by zero
            print("You cannot devide by Zero")#Printing the string
        else:#If we're not deviding by zero
            ans = d1**d2 #'ans' will recive the calculation of 'd1' to the power of 'd2'
            if((ans%1)== 0):#Checkig if the answer is an integer
                print("The power is an integer number: ",ans)#will print the string with 'ans'
            else:#If the number isn't an integer
                print("The power is not an integer number: ",ans)#will print the string with 'ans'
    else:#Last option if a note has been entered that isn't in the table of contents 
        print("Error")#Printing "Error" to the user            