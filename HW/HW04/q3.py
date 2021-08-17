def alt_sorted(lst):
    if (len(lst)==1 or len(lst)==2):
        return True
    
    if len(lst)==4:
        if (lst[0]<=lst[2] and lst[1]>=lst[3]):
               return True
        return False
    if not (lst[0]<=lst[2] and lst[1]>=lst[3]):
        return False
        
    return alt_sorted(lst[2:])

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

main()
