def lst_sort(lst):
    for i in range(len(lst)):
        if(lst[i]>='a' and lst[i]<='z'):
            lst[-1-i] , lst[i] = lst[i] , lst[-1-i]       
    return lst

def main ():
    list1 = ['K', 'f', 'H', 'T', 'm']  
    print(lst_sort(list1))    
    return

main() 