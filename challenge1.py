
#python challenege number 1 of many...

def addMatrix(*matrixx):
    listOfLists=[];
    empty=[];
    sumArray=[]
    arrayLength=len(matrixx)

    for matrix in matrixx:
        listOfLists.append(matrixx)

    token=0;
    counter = 0
    for i in arrayLength:
        for j in range(len(listOfLists[i-1])):
            sumArray[i]+=sumArray[i]

    return sumArray



mat1=[[1,2],[1,2]]
mat2=[[2,3],[4,5]]

print(addMatrix(mat1,mat2))



'''
    for i in range(len(listOfLists)):
        sumArray.append([])         #adds a list after looping through each sub list.
        #sumArray.append(listOfLists[i])
        for j in range(len(listOfLists[i-1])):
            sumArray[i].append(listOfLists[i][j])
  '''
          # print((matrixx[i][j]+matrixxx[i][j]))        #adds and adds the sum.
          # sumArray[i].append((matrixx[i][j]+matrixxx[i][j]))

