#The code will receive a string and a substring to uppercase inside the main string


#This function will create a new empty string and add letters from the original
#string untill it finds a matching letter to the first letter of the substring
#Then it will check if the remaining letters match if so it will add the uppercased
#substring to the new string if not it will continue adding letters untill it does
#after adding the uppercased substring it will continue untill it enoucnters a 
#matching letter again
#the funcion receives the string and substring and returns a new string
def my_replace(s1,sub):
    new_string = ''
    i = 0
    while(i<len(s1)):    
        if(s1[i]==sub[0]):
            if sub in s1[i:i+(len(sub))]:
                new_string+=sub.upper()
                i+=len(sub)
            else:
                new_string+=s1[i]
                i+=1
        else:
            new_string+=s1[i]
            i+=1
    return new_string
#main function that will recieve input from the user and print the new string
#as well as call the function above to complete the task.
def main():
    while(1):
        s1 = str(input("Enter text: "))
        if(s1 == ' '*len(s1)):
            print("Finish")
            break
        sub = str(input("Enter Substring: "))
        if(sub==' '*len(sub)):
            print("Finish")
            break            
        print(my_replace(s1,sub))
    
    return 0

main()#Calling main function