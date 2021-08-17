#this code will count how many times each number from 0-9 appears in a number
#entered by the user 

#This function takes a number and returns the absolute unit of it to work with
#negative numbers as well as positive
def absoluter(num):
    num = abs(num)
    return num

#This function will count how many times each number from 0-9 appears
#by creating a list full of 0 the size of 10 and take the last digit, use it as an index in the list
#and advance it by one, than it will divide the number by 10 to advance to the next digit until reaching 0
#if the user enters '0' then it will advance the list at index 0 by one and return the list immediately 
#the function receives the number entered by the user and returns the 'common_digits' list
def count_digits(num):
    common_digits = [0]*10
    if(num == 0):
        common_digits[0]+=1
    else:
        while(num>0):
            digit = num%10
            common_digits[digit]+=1
            num //=10 
    return common_digits

#This function will print all the appearing digits and how many times
def print_digits_amount(Arr):
    for i in range(len(Arr)):
        if(Arr[i]>0):
            print("The digit", i ,"appears" ,Arr[i],"Times")
    return 0

#this function will find the most commond digits and how many times the occure
# by creating a copied list of the digits amount and sorting it to place the most common number on the right 
#of the list and addition creates a new list that will house the most common digits.
#the function receives the 'digits_amount' list and returns the most common digits and how many times it/they occure
def most_common_digits(amount):
    arr = amount.copy()
    arr.sort()
    common = []
    for i in range(len(amount)):
        if(arr[-1] == amount[i]):
            common.append(i)
    return common,arr[-1]

#this function will print the most common digits
#the function receives the most common digits and returns nothing
def print_common_digits(common_nums):
    for i in range(len(common_nums)):
        print(common_nums[i], end=' ')    
    return 0

#this main function will call all the functions above and print the most frequen digits and how many times it occures
#the function recives the number enterd by the user and returns nothing
def main(num):
    num = absoluter(num)    
    digits_amount = count_digits(num)
    print_digits_amount(digits_amount)
    final_CD,amount = most_common_digits(digits_amount)
    print("The most frequent digit/s is/are:" , end = ' ')
    print_common_digits(final_CD)
    print("\n It occures" , amount, "Times")
    return 0