
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
    MaxI = 0
    Maxj = 0
    while k < int(n):
        MaxI = max(int(MyList[k][0]), MaxI)
        Maxj = max(int(MyList[k][1]), Maxj)
        k = k + 1
    return (MaxI, Maxj)

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
                        print(index[2]),
                else:
                    print(0),
            j += 1
        print('\n')
        i += 1
    return 0

#This function will add two matrices
def AddMatrix(ListA, ListB, ListAdd):
    MyTuple = ()
    dimensiuniA = MaxLenght( ListA, len(ListA) )
    dimensiuniB = MaxLenght( ListB, len(ListB) )
    if dimensiuniA != dimensiuniB:
        print('Nu sunt egale!')
        return 0
    for FirstIndex in range(dimensiuniA[0] + 1):
        for SecondIndex in range(dimensiuniA[1] + 1):
            FirstElement = SearchValue(ListA, FirstIndex, SecondIndex, len(ListA) )
            SecondElement = SearchValue(ListB, FirstIndex, SecondIndex, len(ListB) )
    
            Sum = FirstElement + SecondElement
            if Sum != 0:
                MyTuple = ( FirstIndex, SecondIndex, Sum )
                ListAdd.append( MyTuple )
    print('asta este lista: ', ListAdd)

  #This function will make substraction on two matrices  
def SubMatrix(ListA, ListB, ListSub):
    MyTuple = ()
    dimensiuniA = MaxLenght( ListA, len(ListA) )
    dimensiuniB = MaxLenght( ListB, len(ListB) )
    if dimensiuniA != dimensiuniB:
        print('Nu sunt egale!')
        return 0
    for FirstIndex in range(dimensiuniA[0] + 1):
        for SecondIndex in range(dimensiuniA[1] + 1):
            FirstElement = SearchValue(ListA, FirstIndex, SecondIndex, len(ListA) )
            SecondElement = SearchValue(ListB, FirstIndex, SecondIndex, len(ListB) )
    
            Diff = FirstElement - SecondElement
            if Diff != 0:
                MyTuple = ( FirstIndex, SecondIndex, Diff )
                ListAdd.append( MyTuple )
    print('asta este lista: ', ListSub)

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
                print (1),
            else:
                print(0),
            j += 1
        print('\n')
        i +=1

 #This function will create a null matrix and print it
def NullMatrix(n):
    i = 0
    while i < int(n):
        j = 0
        while j < int(n):
            print(0),
            j += 1
        print('\n')
        i +=1

#This functuin will search for a value useing the specified indices
def SearchValue(MyList, index_i, index_j, n):
    (maxi, maxj) = MaxLenght(A_matrix, n)
    if int(maxi) < int(index_i) or int(maxj) < int(index_j):
        print('The indices have exceeded the size of the matrix')
        return 0
    for index in MyList:
        if index_i == index[0]:
            if index_j == index[1]:
                return index[2]
    return 0

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

print('The numbers elements the second matrix will have: ')
m = input()
CreateMatrix(B_matrix, m)

#PrintMatrix(A_matrix, n)
#print('\n')

print('Enter the indices to look for:')
i = input('First index: ')
j = input('The second index: ')
print( SearchValue(A_matrix, i, j, n) )


max_i, max_j = MaxLenght(A_matrix, n)
print('The matrix dimesion is: ', max_i, 'x', max_j)
print('\n')

print('Aici se face adunarea: ')
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

