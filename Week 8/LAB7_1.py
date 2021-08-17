#The code will receive 7 numbers from the user and an additional number that will be a limit
#all numbers under the limit will be placed in a list on the left before the limit, numbers above the limit
#will be placed to the right of the limir


#This function will place numbers in a new empty list according to the limit set but the user,
#numbers smaller than the limit will be placed to the left using the 'insert' method and a secondary index,
# numbers larger than the limit will be placed to the right of the limit using the 'append' method
#The function receives the nubmers entered by the user in a form of a list and the limit.
#the function returns the new list
def create_new_list(List,x):
    new_list = []
    j=0
    for i in range(len(List)):
        if(List[i]<x):
            new_list.insert(j, List[i])
            j+=1
        else:
            new_list.append(List[i])
    return new_list

#This function will receive numbers from the user and store them in a list.
#The function will create a new empty list the size of the number that's in the first command of the code
#and store the numbers entered by the user in it
#The function receive the ammount of numbers and returns the list 'a'
def input_list(n):
    a = [0]*n
    for i in range(n):
      a[i] = int(input("Enter integer: ")) 
    return a

#this main function will print the list entered by the user as well as the final list 
#in addition it calls all the functions above
#the function receives the number of numbers the user will enter and returns nothing.
def main(n):
    Old_List = input_list(n)
    print("Original List: ", Old_List)
    x = int(input("Enter x: "))
    print("New List: ", create_new_list(Old_List,x))
    return 0

main(7)#Starting command calling main and sending the ammount of numbers the user will enter