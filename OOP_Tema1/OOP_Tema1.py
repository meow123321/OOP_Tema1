
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

#This function will find the matrix dimension
def MaxLenght(MyList, n):
    k = 0
    while k + 1 < int(n):
        Maxi = max(MyList[k][0], MyList[k+1][0])
        Maxj = max(MyList[k][1], MyList[k+1][1])
        k = k + 1
    return Maxi, Maxj

# This function will print the full matrix
def PrintMatrix(MyList, n):
    Maxi, Maxj = MaxLenght(A_matrix, n)
    i = 0
    while i < int(Maxi):
        j = 0
        while j < int(Maxj):
            for index in MyList:
                if i == index[0]:
                    if j == index[1]:
                        print(index[2], end = ' ')
                else:
                    print(0, end = ' ')
            j += 1
        print('\n')
        i += 1
    return 0

#This function will add two matrices
def AddMatrix(ListA, ListB, ListAdd):
   indexA = 0
   indexB = 0
   while indexA < len(ListA):
        indexB = 0
        while indexB < len(ListB):
            if ListA[indexA][0] == ListB[indexB][0] and ListA[indexA][1] == ListB[indexB][1] :
                Add_val = int(ListA[indexA][2]) + int(ListB[indexB][2])
                i = ListA[indexA][0]
                j = ListA[indexA][1]
                MyTuple = (i, j, Add_val)
                ListAdd.append(MyTuple)
                print('if: ', MyTuple, '\n')
                ListB.remove(ListB[indexB])
                print(ListB)
            else:
                Add_val = ListA[indexA][2]
                i = ListA[indexA][0]
                j = ListA[indexA][1]
                MyTuple = (i, j, Add_val)
                if MyTuple not in ListAdd:
                    ListAdd.append(MyTuple)
                    print('sunt in else', MyTuple)
            indexB += 1
        indexA += 1
        indexB = 0
        while indexB < len(ListB):
            Add_val = ListB[indexB][2]
            i = ListB[indexB][0]
            j= ListB[indexB][1]
            MyTuple = (i, j, Add_val)
            ListAdd.append(MyTuple)
            print('ifB: ', MyTuple, '\n')
            indexB += 1
        i = 0
        while i < len(ListAdd):
            j = 0
            while j < len(ListAdd):
                if ListAdd[i][0] == ListAdd[j][0] and ListAdd[i][1] == ListAdd[j][1]:
                    if i < j:
                        ListAdd.remove(ListAdd[i])
                    else:
                        ListAdd.remove(ListAdd[j])
        print('asta este lista: ', ListAdd)

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

#This function will print the transposed matrix as a list
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

#This function careate the unit matrix and print it
def UnitMatrix(MyList, n):
    i = 0
    while i < int(n):
        j = 0
        while j < int(n):
            if i == j :
                MyTuple = (i, j, 1)
                MyList.append(MyTuple)
                print (1,  end =" ")
            else:
                print(0,  end =" ")
            j += 1
        print('\n')
        i +=1

 #This function will create a null matrix and print it
def NullMatrix(n):
    i = 0
    while i < int(n):
        j = 0
        while j < int(n):
            print(0,  end =" ")
            j += 1
        print('\n')
        i +=1

#This functuin will search for a value useing the specified indices
def SearchValue(MyList, index_i, index_j, n):
    maxi, maxj = MaxLenght(A_matrix, n)
    if int(maxi) < int(index_i) or int(maxj) < int(index_j):
        print('The indices have exceeded the size of the matrix')
        return 0
    for index in MyList:
        if index_i == index[0]:
            if index_j == index[1]:
                print('We found the element', end = ' ')
                print(index[2], '\n')
                return index[2]
                

A_matrix = []
B_matrix = []
Add_matrix = []
Sub_matrix = []
Transp_matrix = []
Unit_Matrix = []
max_i = 0
max_j = 0

print('The numbers elements the first matrix will have: ')
n = input()
CreateMatrix(A_matrix, n)
print(A_matrix)

PrintMatrix(A_matrix, n)
print('\n')

print('Enter the indices to look for:')
i = input('First index: ')
j = input('The second index: ')
SearchValue(A_matrix, i, j, n)


max_i, max_j = MaxLenght(A_matrix, n)
print('The matrix dimesion is: ', max_i, 'x', max_j)
print('\n')

print('The numbers elements the second matrix will have: ')
m = input()
CreateMatrix(B_matrix, m)


AddMatrix(A_matrix, B_matrix, Add_matrix)

print('Enter the dimension of the unit matrix')
u = input()
print('\n')
UnitMatrix(Unit_Matrix,u)

print('Null Matrix: ')
NullMatrix(u)

print('The transpused matrix')
TransMatrix(A_matrix,Transp_matrix)


#nu merge
#SubMatrix(A_matrix, B_matrix, Sub_matrix)

