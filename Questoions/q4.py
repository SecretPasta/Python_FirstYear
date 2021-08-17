def longest_Subarray(a):
    j = 1
    biggest = 0
    for i in range(len(a)-1):
        if(a[i+1]>a[i]):
            j+=1                
        else:
            if(j>biggest):
                biggest = j
            j=1
        if(j>biggest):
                biggest = j
    if(j>biggest):
                biggest = j
    return biggest

def main():
    print(longest_Subarray([1,2,3,2,3,4,5]))
    print(longest_Subarray([9,8,7,6,5,4,3,2,1,0]))
    print(longest_Subarray([1,1,1,1,1,1,1]))
    print(longest_Subarray([17]))
    return

main()