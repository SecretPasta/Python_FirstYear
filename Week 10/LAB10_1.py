#The code check if a list of words are hidden inside a string 

#This function will find if a word is hidden inside the string
#by looking for the first letter of the word appears and then look for the subsequent 
#letter if not it'll reverse the string and check again once one of the strings is found it returns True if not
#it returns False
#The function recieves the string and word to find and returns a bool
def hidden_str(s1,s2):
    c = 0
    for i in range(len(s1)):
        if(s1[i]==s2[c]):
            c+=1
        if(c==len(s2)):
            return True
    s1 = s1[::-1]
    c = 0
    for i in range(len(s1)):
        if(s1[i]==s2[c]):
            c+=1
        if(c==len(s2)):
            return True

    return False

#the main function that will pring the results of which word appears and which doesn't appear
#and call the function above to solve the task
def main():
    s1 = "Computer Science"
    s2 = ['optic','nirto','option']
    for i in range(len(s2)):
        if(hidden_str(s1,s2[i])):
            print(s2[i],"is hidden in",s1)
        else:
            print(s2[i],"is not hidden in",s1)
      
    return 0

main()#Calling main