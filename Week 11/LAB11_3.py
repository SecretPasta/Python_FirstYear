#This code will sort a list of numbers entered by the user

#this function will sort the list using the maxSort alogrithm 
#the function receives and returns a list
def maxSort(a,n):
    for i in range(n-1,1,-1):
        maxIndex=i
        for j in range(i):
            if (a[maxIndex]<a[j]):
                maxIndex=j
            a[i],a[maxIndex]=a[maxIndex],a[i]   
    return a

#main function that will ask the user to enter a list of numbers, and call the
#function above to sort the list and print the result to the user. The function
#will run until the user enters a list size of 0
def main():
    while(1):
        a = []
        n = int(input("Please eneter the nubmer of elements in the list:" ))
        if(n==0):
            print("Thank you for exploring max sort")
            break
        for i in range(n):
            a.append(input())
        print("The list, before sorting: ", a)
        print("The list, after sorting: ",maxSort(a,n))     
    return 0

main()#Calling main