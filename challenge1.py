
def addMatrix(matrixx,matrixxx):
    sumArray=[]

    for i in range(len(matrixx)):
        sumArray.append([]) #adds a list after looping through each sub list.
        for j in range(len(matrixxx[i-1])):
           print((matrixx[i][j]+matrixxx[i][j]))        #adds and adds the sum.
           sumArray[i].append((matrixx[i][j]+matrixxx[i][j]))

    return sumArray

mat1=[[1,2],[1,2]]
mat2=[[2,3],[4,5]]

print(addMatrix(mat1,mat2))

