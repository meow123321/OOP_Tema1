
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
def MaxLenght(MyList, n):
    k = 0
    while k + 1 < int(n):
        Maxi = max(MyList[k][0], MyList[k+1][0])
        Maxj = max(MyList[k][1], MyList[k+1][1])
        k = k + 1
    return Maxi, Maxj


# This function will print the full matrix
def PrintMatrix(MyList, Maxi, Maxj):
    k = 0
    print('Am intrat in functie')
    while k < len(MyList):
        val_temp = MyList[k][2]
        i = 1
        while i <= int(Maxi):
            j = 1
            while j <= int(Maxj):
                if MyList[k][0] == i and MyList[k][1] == j:
                    print(val_temp, end = ' ')
                else:
                    print(0, end = ' ')
                    print(MyList[k][0], i)
                    print(MyList[k][1], j)
  
                j = j + 1
            print('\n')
            i = i +1
        k += 1

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
    
def NullMatrix(n):
    i = 0
    while i < int(n):
        j = 0
        while j < int(n):
            print(0,  end =" ")
            j += 1
        print('\n')
        i +=1

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


max_i, max_j = MaxLenght(A_matrix, n)
print('The matrix dimesion is: ', max_i, 'x', max_j)
print('\n')

PrintMatrix(A_matrix, max_i, max_j)

print('Enter the dimension of the unit matrix')
u = input()
print('\n')
UnitMatrix(Unit_Matrix,u)

print('Null Matrix: ')
NullMatrix(u)


#print('The numbers elements the second matrix will have: ')
#m = input()
#CreateMatrix(B_matrix, m)


#nu merge

#AddMatrix(A_matrix, B_matrix, Add_matrix)
#SubMatrix(A_matrix, B_matrix, Sub_matrix)

#TransMatrix(A_matrix,Transp_matrix)