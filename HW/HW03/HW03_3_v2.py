#This code will receive a string and compress it then it will receive a 
#compressed string and restore it

#This funciton turns an integer into a string by replaceing each digit with the
#same digit but in string format and at the end reversing the string
def int_to_str(num):
    string =''
    str_num = ['0','1','2','3','4','5','6','7','8','9']
    if(num==0):
        string+='0'
    while(num>0):
        temp=num%10
        string+=str_num[temp]
        num = num//10
    string = string[::-1]    
    return string

#This function will compress a string by creating a new string and definding a 
#counter at '1' The it will check if two neighbouring nubmers are matching if 
#yes it will advance the counter, once it encounters a different letter it will
#add the previos letter and number to the new string and reset the counter
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
            compressed+=int_to_str(count)
            count = 1
    compressed+= string[i+1]
    compressed+=int_to_str(count)
    return compressed

#This function will restore a string, it does so by every time it encouters a 
#letter it will store it in 'curLetter',afterwards it will encounter a number 
#and will begin to adding each digit to 'curNum' after encountering a letter
#again it will take the 'curLetter' and multiply it by 'curNumber' and add it
#to the 'ans' string and the process will repeat itself untill the string 
#is comeplete, the code receives a string and returns the restored string
def strRestore(string):
    i=0
    ans=""
    curLetter=''
    while i<len(string):
        if string[i].isdigit(): 
            curNum=0
            while i<len(string) and string[i].isdigit():
                curNum=curNum*10+int(string[i]) 
                i+=1
            ans+=curLetter*curNum 
        else:
            curLetter=string[i] 
            i+=1
    return ans
#Main function to receive a string and print its' compression and afterwards receives a
#compressed string and prints the restored string by calling the functions above
def main():
    string = str(input("Enter a section chain to compress: "))
    print(strCompress(string))  
    string = str(input("Enter a compressed chain: "))
    print(strRestore(string))

main()#Calling main