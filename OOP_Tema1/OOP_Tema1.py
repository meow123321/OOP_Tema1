
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

def MaxLenght(MyList,Maxi, Maxj, n):
    k = 0
    while k + 1 < int(n):
        Maxi = max(MyList[k][0], MyList[k+1][0])
        Maxj = max(MyList[k][1], MyList[k+1][1])
        k = k + 1
    print('The matrix dimesion is: ', Maxi, 'x', Maxj)
    print('\n')

# This function will print the full matrix
def PrintMatrix(MyList, Maxi, Maxj):
    p = 0
    q = 0
    print('Am intrat in functie')
    while p < Maxi:
        while q < Maxj:
            if MyList[j][1] == index_i and MyList[q][2] == k:
                print(val,', ')
            else:
                print(0,', ')
            q = q + 1
        print('\n')
        
        p = p +1

def AddMatrix(ListA, ListB, ListAdd, Maxi, Maxj):
   indexA = 0
   indexB = 0
   while indexA < len(ListA):
       while indexB < len(ListB):
        if ListA[indexA][0] == ListB[indexB][0] and ListA[indexA][1] == ListB[indexB][1] :
            Add_value = ListA[indexA][2] + ListA[indexB][2]
            i = ListA[indexA][0]
            j = ListA[indexB][1]
            MyTuple = (i, j, Add_value)
            ListAdd.append(MyTuple)
        else:
            Add_value = ListA[indexA][2]
            i = ListA[indexA][0]
            j = ListA[indexA][1]
            MyTuple = (i, j, Add_value)
            ListAdd.append(MyTuple)

    while indexB < len(ListB):
        while indexAdd < len(ListAdd):
            if ListAdd[indexAdd][0] != ListB[indexB][0] and ListAdd[indexAdd][1] != ListB[indexB][1] :
                Add_value = ListB[indexB][2]
                i = ListB[indexB][0]
                j = ListB[indexB][1]
                MyTuple = (i, j, Add_value)
                ListAdd.append(MyTuple)
    print(ListAdd)
    print('\n')
    
def SubMatrix(ListA, ListB, ListSub, Maxi, Maxj):
   indexA = 0
   indexB = 0
   while indexA < len(ListA):
       while indexB < len(ListB):
        if ListA[indexA][0] == ListB[indexB][0] and ListA[indexA][1] == ListB[indexB][1] :
            Add_value = ListA[indexA][2] - ListA[indexB][2]
            i = ListA[indexA][0]
            j = ListA[indexB_matrix][1]
            MyTuple = (i, j, Add_value)
            ListSub.append(MyTuple)
        else:
            Add_value = ListA[indexA][2]
            i = ListA[indexA][0]
            j = ListA[indexA][1]
            MyTuple = (i, j, Add_value)
            ListSub.append(MyTuple)
        if ListSub[indexA][0] != ListB[indexB][0] and ListSub[indexA][1] != ListB[indexB][1] :
            Add_value = -ListB[indexB][2]
            i = ListB[indexB][0]
            j = ListB[indexB][1]
            MyTuple = (i, j, Add_value)
            ListSub.append(MyTuple)
        print(ListSub)
        print('\n')
    


A_matrix = []
B_matrix = []
Add_matrix = []
Sub_matrix = []
Transp_matrix = []
max_i = 0
max_j = 0

MyTuple = ()
print('The numbers elements the first matrix will have: ')
n = input()
CreateMatrix(A_matrix, n)
print('The numbers elements the second matrix will have: ')
m = input()
CreateMatrix(B_matrix, m)
MaxLenght(A_matrix, max_i, max_j, n)
PrintMatrix(A_matrix, max_i, max_j)
AddMatrix(A_matrix, B_matrix, Add_matrix, max_i, max_j)