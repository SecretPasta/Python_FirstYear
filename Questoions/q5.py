

def is_pyramid_matrix(mat):
    max1 = []
    min1 = []
    if(len(mat)%2==1):
       for r in range(len(mat)//2+1):
           temp = []
           
    
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