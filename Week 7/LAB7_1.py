#The Code will receive a number and check if it's well mixed

#This function will check if the input is correct by making sure it greater 
#or equal to 10, the functions receives the value of num and returns True or False
#If the value is smaller than 10, the code will print an error message and end the program
def check_num(num):
    if(num>=10):
        return True
    else:
        print(num , "Needs to be a positive number With at leaset 2 digits")
        return False

#This function will check if there are any repeating digits by turing the number into a string
#and checking if each note is equal to any other note, the function receives the value of num
#and returns True or False
def digit_dif(num):
    num = str(num)
    i = 0
    while(i<len(num)):
        j = i+1
        while(j<len(num)):
            if(num[i]==num[j]):
                return False
            j+=1
        i+=1
    return True

#This function will check if any 2 neighboring digits have a delta of '1' by taking
#the last two digits of the number and checking if the delta exists and devides by 10
#To remove the last digit each run. the functions receives the value of num
#And returns True or False
def check_seq(num):
    while(num>=10):
        D = int((num%100)/10)
        S = int(num%10)
        if(D==(S+1) or D==(S-1)):
            return False
        num/=10
    return True

#Asking the user for input, will be stored in 'num'
num = int(input("Enter a Positive Integer (no less than 2 digits): "))
if(check_num(num)): #Checking if the input is valid by calling 'check_num' function and sending it the value of 'num'
    flag1 = digit_dif(num) #flag1 will recieve the statment from 'digit_dif' function 
    flag2 = check_seq(num) #flag2 will recieve the statment from 'check_seq' function 
    if(flag1 and flag2):#Checking if both flags are True
        print(num, "is a Well mixed number") #If yes printing this string
    else:
        print(num, "is NOT a Well mixed number")#If not printing this string

