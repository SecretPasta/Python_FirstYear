def one_layer_off(matrix):
    for i in range(len(matrix)):
        temp = matrix[i]
        temp = temp[1:-1]
        matrix[i]=temp
    return matrix[1:-1]

def is_pyramid_matrix(mat):
    MAX = 0
    for c in range(len(mat)-2):
        MAX = max(mat[0])
        MAX1 = max(mat[-1])
        if(MAX>MAX1):
            MAX=MAX
        else:
            MAX = MAX1
        for c in range(1,len(mat)-1):
            if (mat[c][0]>MAX):
                MAX = mat[c][0]
            if(mat[c][-1]>MAX):
                MAX = mat[c][-1]
        mat = one_layer_off(mat)
        for g in range(len(mat)):
            if(MAX>mat[0][g]):
                return False
            if(MAX>mat[-1][g]):
                return False        
        for v in range(len(mat)-2):
            if(MAX>mat[v][0]):
                return False
            if(MAX>mat[v][-1]):
                return False    
    return True


def main ():
    mat1 = [[7,8,9,4,-1],[1,13,17,22,0],[7,19,25,16,12],[5,20,21,19,9],[-2,0,8,6,6]]
    mat2 = [[7,8,4,-1],[1,13,22,0],[5,20,19,9],[-2,0,6,6]]
    mat3 = [[1,2,3,4],[1,2,3,4],[1,2,3,4],[1,2,3,4]]
    print(is_pyramid_matrix(mat1))
    print(is_pyramid_matrix(mat2))
    print(is_pyramid_matrix(mat3))  
    return

main()