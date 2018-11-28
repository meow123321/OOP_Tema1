
# This function will ask only for the non_null values
def CreateMatrix(MyList, n):
    index = 0
    print('Enter the elements: ')
    while index < int(n):
        i = input('The first index: ')
        j = input('The second index: ')
        val = input('The value of the element: ')
        MyTuple = (i, j, val)
        MyList.append(MyTuple)
        index = index + 1
        print('\n')
    print(MyList)
    print('\n')
  


#This function will find the matrix dimension
def MaxLenght(MyList, Maxi, Maxj, n):
    k = 0
    while k + 1 < int(n):
        Maxi = max(MyList[k][0], MyList[k+1][0])
        Maxj = max(MyList[k][1], MyList[k+1][1])
        k = k + 1
    return Maxi, Maxj


# This function will print the full matrix
def PrintMatrix(MyList, Maxi, Maxj):
    p = 0
    q = 0
    while p < int(Maxi):
        while q < int(Maxj):
            if MyList[p][0] == p + 1 and MyList[p][1] == q + 1:
                val_temp = MyList[p][2]
                print(val_temp,', ')
            else:
                print(0,', ')
            q = q + 1
        print('\n')
        p = p +1
#This function will add two matrices
def AddMatrix(ListA, ListB, ListAdd):
   MyTuple = ()
   indexA = 0
   indexB = 0
   indexAdd = 0
   while indexA < len(ListA):
        while indexB < len(ListB):
            while indexAdd < len(ListAdd):
                if ListA[indexA][0] == ListB[indexB][0] and ListA[indexA][1] == ListB[indexB][1] :
                    Add_val = ListA[indexA][2] + ListA[indexB][2]
                    i = ListA[indexA][0]
                    j = ListA[indexB][1]
                    MyTuple = (i, j, Add_val)
                    ListAdd.append(MyTuple)
                else:
                    Add_val = ListA[indexA][2]
                    i = ListA[indexA][0]
                    j = ListA[indexA][1]
                    MyTuple = (i, j, Add_val)
                    ListAdd.append(MyTuple)
                if ListAdd[indexAdd][0] != ListB[indexB][0] and ListAdd[indexAdd][1] != ListB[indexB][1]:
                    Add_val = ListB[indexB][2]
                    i = ListB[indexB][0]
                    j = ListB[indexB][1]
                    MyTuple = (i, j, Add_val)
                    ListAdd.append(MyTuple)
                indexAdd = indexAdd + 1
            indexB = indexB + 1
        indexA = indexA + 1 
        print(ListAdd)

  #This function will make substraction on two matrices  
def SubMatrix(ListA, ListB, ListSub):
   MyTuple = ()
   indexA = 0
   indexB = 0
   indexSub = 0
   while indexA < len(ListA):
        while indexB < len(ListB):
            while indexSub < len(ListSub):
                if ListA[indexA][0] == ListB[indexB][0] and ListA[indexA][1] == ListB[indexB][1] :
                    Add_val = ListA[indexA][2] + ListA[indexB][2]
                    i = ListA[indexA][0]
                    j = ListA[indexB][1]
                    MyTuple = (i, j, Add_val)
                    ListSub.append(MyTuple)
                else:
                    Add_val = ListA[indexA][2]
                    i = ListA[indexA][0]
                    j = ListA[indexA][1]
                    MyTuple = (i, j, Add_val)
                    ListSub.append(MyTuple)
                if ListSub[indexSub][0] != ListB[indexB][0] and ListSub[indexSub][1] != ListB[indexB][1]:
                    Add_val = ListB[indexB][2]
                    i = ListB[indexB][0]
                    j = ListB[indexB][1]
                    MyTuple = (i, j, Add_val)
                    ListSub.append(MyTuple)
                indexSub = indexSub + 1
            indexB = indexB + 1
        indexA = indexA + 1 
        print(ListSub)

#this function will print the transposed matrix as a list
def TransMatrix(MyList, TransList):
    MyTuple = ()
    index = 0
    while index < len(MyList):
        i = MyList[index][1]
        j = MyList[index][0]
        val_trans = MyList[index][2]
        MyTuple = (i, j, val_trans)
        TransList.append(MyTuple)
        index = index + 1
    print(TransList)
    


A_matrix = []
B_matrix = []
Add_matrix = []
Sub_matrix = []
Transp_matrix = []
max_i = 0
max_j = 0

print('The numbers elements the first matrix will have: ')
n = input()
CreateMatrix(A_matrix, n)

print('The numbers elements the second matrix will have: ')
m = input()
CreateMatrix(B_matrix, m)

max_i, max_j = MaxLenght(A_matrix, max_i, max_j, n)
print('The matrix dimesion is: ', max_i, 'x', max_j)
print('\n')

#nu merge
#PrintMatrix(A_matrix, max_i, max_j)
#AddMatrix(A_matrix, B_matrix, Add_matrix)
#SubMatrix(A_matrix, B_matrix, Sub_matrix)

TransMatrix(A_matrix,Transp_matrix)