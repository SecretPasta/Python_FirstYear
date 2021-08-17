#The code will check if a prefix exists in a string 

#This function will use recursion to slicing the string from the begining
#and comparing the first letters of the prefix and the string 

def recursive_has_prefix(str1,prefix):
    if(str1=='' and prefix==''):        
        return 1
    if(prefix=='' and str1!=''):
        return 1
    if(len(prefix)>len(str1)):
        return 0
    if(str1[0]!=prefix[0]):
        return 0
    if(len(prefix)==1):
        if(str1[0]==prefix[0]):
            return 1
    
    return recursive_has_prefix(str1[1:], prefix[1:])

#main function that will ask or input and call the function above 
#to check if a prefix exists and print a message accordingly 
def main():
    isPrefix = True
    while isPrefix:
        str1 = input("Please enter a string: ")
        pref = input("Please enter a prefix string: ")
        isPrefix = recursive_has_prefix(str1, pref)
        if isPrefix:
            print("The text has the prefix")
        else:
            print("No prefix")
    print()
main()#calling main
