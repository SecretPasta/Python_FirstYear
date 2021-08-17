#This code will receive a string and compress it then it will receive a compressed string
#and restore it

#This function will separate the numbers and letters into a list and a string
#It does so by reversing the string as this will insure the last letter is an alphabetical char
#Then it creates an empty list and string and defines an index at zero. afterwards it checks if each
#characters is a number if it encounters a number it counts how many numbers are there once it enoucnters
#a letter it slices the string and adds it to the new list, then when that main 'if' encouters a letter
#it adds the letter to the new string. After completeing the seperation it reverses the numbers in each
#cell of list and then it reverses the list and string to return everything to the correct order
#The function receives the string and returns a list of numbers and string of letters with a matching index
#for each number and character
def spliter(string):
    r_string = string[::-1]
    temp_s = '' 
    temp_l = [] 
    i = 0
    while(i<len(string)):
        if(r_string[i].isdigit()):
            j=0
            while(r_string[i+j].isdigit()):         
                j+=1                                             
            temp_l.append(r_string[i:i+j])                
            i=(i+j)
        else:
            temp_s+=r_string[i]
            i+=1
    for k in range(len(temp_l)):
        temp = temp_l[k]
        temp_l[k]=temp[::-1]
    
    temp_l.reverse()
    temp_s = temp_s[::-1]
    
    return temp_s,temp_l

#This function will compress a string by creating a new string and definding a counter at '1'
#The it will check if two neighbouring nubmers are matching if yes it will advance the counter, once it 
#encounters a different letter it will add the previos letter and number to the new string and reset the counter
#It will do so one last time after the loop to add the final character and number
#the function receives a string and returns a new compressed string
def strCompress(string):
    count = 1
    compressed = ''
    for i in range(len(string)-1):
        if(string[i]==string[i+1]):   
           count+=1
        else:
            compressed+= string[i]
            compressed+=str(count)
            count = 1
    compressed+= string[i+1]
    compressed+=str(count)
    return compressed

#This function will restore a string by calling the "spliter" function to split the numbers
#from the characters. Afterwards it will add each character and multiply it by the number next
#to it(The list and string have a matching length and indexes) and add this to the new string
#The function receives a string and returns a restored string                                
def strRestore(string):
    letters,numbers = spliter(string)
    decomp = ''
    for s in range(len(letters)):
        decomp += letters[s]*int(numbers[s])
        
    return decomp 
#Main function to receive a string and print its' compression and afterwards receives a
#compressed string and prints the restored string by calling the functions above
def main():
    string = str(input("Enter a section chain to compress: "))
    print(strCompress(string))  
    string = str(input("Enter a compressed chain: "))
    print(strRestore(string))

main()#Calling main