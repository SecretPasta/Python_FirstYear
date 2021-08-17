#This code will check if cells at the even location are in a none descending 
#order and the cells at the uneven locations are in a non ascending using recursion

#This function will check 4 cells at a time if the match the requirments and then
#call itself after slicing out the first two cells out of the list. The recursion
#will stop and return False if the requirmetns are not met and will return True
#if entered single cell or dual cell list as we assume this lists are sorted
def alt_sorted(lst):
    if (len(lst)==1 or len(lst)==2):
        return True
    if len(lst)==3:
       return lst[0]<=lst[2]
           
    if not (lst[0]<=lst[2] and lst[1]>=lst[3]):
        return False
        
    return alt_sorted(lst[2:])

#main function to ask for input and check if the list is alternatly sorted by 
#calling the function above and print a message accordingly
def main():
    n = int(input("Enter list length:" ))
    print("Enter integers: ")
    list1 = []
    for i in range(n):
        list1.append(int(input()))
    if (alt_sorted(list1)):
        print(list1,"\nalternately sorted")
    else:
        print(list1,"\nnot alternately sorted")
   
    return 

main()#calling main
 