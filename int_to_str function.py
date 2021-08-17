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

