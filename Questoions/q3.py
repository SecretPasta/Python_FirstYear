def ranger(A):
    supA = []
    infA = []
    i = 0
    supA.append(A[i])
    while (i<len(A)-1):       
       if not ((A[i]+1)==A[i+1]):
           infA.append(A[i])
           i+=1
           supA.append(A[i])
       else:       
           i+=1
    infA.append(A[i])
    return  [supA,infA]

def print_mat(mat2):
    for i in range(len(mat2)):
        print("│" ,end =' ')
        for j in range(len(mat2[0])):
            print("%4d" %mat2[i][j], end=' ')
        print("│")
    return 0

def main():
    a = [-10,-9,-8,-7,-6,3,7,8,9,10,11,12]
    arr2D = ranger(a)
    print_mat(arr2D)
    return

main()