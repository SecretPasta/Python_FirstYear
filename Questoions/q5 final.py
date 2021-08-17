def one_layer_off(matrix):
    for i in range(len(matrix)):
        temp = matrix[i]
        temp = temp[1:-1]
        matrix[i]=temp
    return matrix

def is_pyramid_matrix(mat):
    MAX = []
    MIN = []
    temp = []    
    for r in range(len(mat)-2):
        temp.extend(mat[r])
        temp.extend(mat[-1-r])
        for c in range(r+1,len(mat)-1-r):
            temp.append(mat[c][0])
            temp.append(mat[c][-1])    
        MAX.append(max(temp))
        MIN.append(min(temp))
        temp = []
        mat = one_layer_off(mat)
    print(MAX,MIN)
    for s in range(len(MAX)-1):
        if not (MAX[s]<=MIN[s+1]):
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