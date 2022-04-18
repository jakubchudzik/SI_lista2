import random
import time

import numpy as np
licznik =0
nawroty = 0
ti = time.time()
def b_is_different(_matrix, coords):
    pom = _matrix.T
    if '' in _matrix[coords[1]]:
        return True
    for i in range(len(_matrix)):
        if i!=coords[1]:
            if np.array_equal(_matrix[i],_matrix[coords[1]]):
                return False
    if '' in pom[coords[0]]:
        return True
    for i in range(len(_matrix)):
        if i!=coords[0]:
            if np.array_equal(pom[i],pom[coords[0]]):
                return False
    return True

def b_is_less_than_3_char(_matrix, coords, field):
    col = coords[0]
    row = coords[1]
    maxi_col = 0
    maxi_row = 0
    for i in field:
        count_of_elements_col = 0
        count_of_elements_row = 0
        for j in range(len(_matrix)):
            if _matrix[j][col] == i:
                count_of_elements_col += 1
            else:
                if maxi_col < count_of_elements_col:
                    maxi_col = count_of_elements_col
                count_of_elements_col = 0
            if _matrix[row][j] == i:
                count_of_elements_row += 1
            else:
                if maxi_row < count_of_elements_row:
                    maxi_row = count_of_elements_row
                count_of_elements_row = 0
        if maxi_row > 2 or maxi_col > 2 or count_of_elements_row > 2 or count_of_elements_col > 2:
            return False
    return True
#(col,row)

def b_isOkRowNumbers(_matrix, limit_numbers, field,coords):
    row = coords[1]
    for i in field:
        counter = 0
        for j in range(len(_matrix)):
            if i == _matrix[row][j]:
                counter+=1
        if counter>limit_numbers:
            return False
    return True


def b_isOkColNumbers(_matrix, limit_numbers, field,coords):
    col = coords[0]
    pom = _matrix.T
    for i in field:
        counter = 0
        for j in range(len(_matrix)):
            if i == pom[col][j]:
                counter+=1
        if counter>limit_numbers:
            return False
    return True


def b_make_grid(file_name):
    with open(file_name, 'r') as file:
        binary = file.readlines()

    lista = []

    for i in range(len(binary)):
        binary[i] = binary[i].strip()
        pom = []
        for j in binary[i]:
            if j == "x":
                pom.append('')
            else:
                pom.append(j)
        lista.append(pom)
    _matrix = np.array(lista)
    return  _matrix

def f_make_grid(file_name):
    with open(file_name, 'r') as file:
        binary = file.readlines()

    lista = []

    for i in range(len(binary)):
        binary[i] = binary[i].strip()
        pom = []
        for j in binary[i]:
            if j == "x":
                pom.append('')
            else:
                pom.append(j)
            if i % 2 ==1:
                pom.append('-')
        if i%2==1:
            pom.pop()
        lista.append(np.array(pom))
    _matrix = np.array(lista)
    return  _matrix

def f_make_field(_matrix):
    field = []
    for i in range(len(_matrix)//2+1):
        field.append(f'{i+1}')
    return field

# def find_free_place(_matrix):
#     for i in range(len(_matrix),2):
#         for j in range(len(_matrix[i]),2):
#             if _matrix[i][j] == '':
#                 return (j,i)
#     return False

def f_is_ok_row(_matrix,field,coords):
    liczniki={}
    for i in range(0,len(_matrix),2):
        if _matrix[coords[1]][i] in field:
            if _matrix[coords[1]][i] not in liczniki:
                liczniki[_matrix[coords[1]][i]] = 1
            else:
                return False
    return True

def f_is_ok_col(_matrix,field,coords):
    liczniki = {}
    for i in range(0,len(_matrix),2):
        if _matrix[i][coords[0]] in field:
            if _matrix[i][coords[0]] not in liczniki:
                liczniki[_matrix[i][coords[0]]] = 1
            else:
                return False
    return True

def f_is_ok(a,b,character):
    if a=='' or b == '':
        return True
    if character == ">":
        if int(a)>int(b):
            return True
        else:
            return False
    if character == "<":
        if int(a)<int(b):
            return True
        else:
            return False
    return True
def f_is_ok_with_sanctions(_matrix,coords):
    row = coords[1]
    col = coords[0]
    pom = []
    for i in range(len(_matrix)):
        pom.append(_matrix[row][i])
    k=0
    for i in range(len(pom)//2):
       if not f_is_ok(pom[k],pom[k+2],pom[k+1]):
           return False
       k+=2
    pom=[]
    for i in range(len(_matrix)):
        pom.append(_matrix[i][col])
    k = 0
    for i in range(len(pom) // 2):
        if not f_is_ok(pom[k], pom[k + 2], pom[k + 1]):
            return False
        k += 2
    return True

def find_free_place(_matrix):
    for i in range(len(_matrix)):
        for j in range(len(_matrix[i])):
            if _matrix[i][j] == '':
                return (j, i)
    return False
def binary(_matrix,field,coords):
    if b_is_less_than_3_char(_matrix, coords, field) and b_is_different(_matrix, coords) and b_isOkRowNumbers(_matrix, len(_matrix) // 2, field,coords) and b_isOkColNumbers(_matrix, len(_matrix) // 2,field, coords):
        return True
    return False
def futo(_matrix,field,coords):
    if f_is_ok_row(_matrix, field, coords) and f_is_ok_col(_matrix, field, coords) and f_is_ok_with_sanctions(_matrix,coords):
        return True
    return False

def solver(_matrix,field,function,coords=None):
    global licznik
    global nawroty
    n_field=['1','0']
    licznik+=1
    if coords == None:
        coords = find_free_place(_matrix)
    n_field=field
    if random.randint(0,1) ==1:
        n_field=field[::-1]
    for i in n_field:
        _matrix[coords[1]][coords[0]] = i
        if function(_matrix,field,coords):
            free = find_free_place(_matrix)
            if free == False:
                print(_matrix)
                print(licznik)
                print("czas dla pierwszego: "+str(time.time()-ti))

            else:
                solver(_matrix,field,function,free)
        elif i == n_field[-1]:
            nawroty+=1

    _matrix[coords[1]][coords[0]]=''

def main():
    global licznik
    global nawroty
    field1 = ['0', '1']
    print('Binary 6x6')
    _matrix = b_make_grid("data/binary_6x6")
    solver(_matrix,field1,binary)
    print(licznik)
    licznik = 0
    print('------------------------')
    print('Binary 8x8')
    _matrix = b_make_grid("data/binary_8x8")
    solver(_matrix,field1,binary)
    print(licznik)
    print(nawroty)
    print("czas dla wszystkich: "+str(time.time()-ti))

    licznik=0
    print('------------------------')
    print('Binary 10x10')
    _matrix = b_make_grid("data/binary_10x10")
    solver(_matrix,field1,binary)
    print(licznik)
    licznik=0
    print('------------------------')
    _matrix = f_make_grid("data/futoshiki_4x4")
    solver(_matrix,f_make_field(_matrix),futo)
    print(licznik)
    print(nawroty)
    print("czas dla wszystkich: "+str(time.time()-ti))
    print('------------------------')
    _matrix = f_make_grid("data/futoshiki_5x5")
    solver(_matrix,f_make_field(_matrix),futo)
    print(licznik)
    print(nawroty)
    print("czas dla wszystkich: "+str(time.time()-ti))
    _matrix = f_make_grid("data/futoshiki_6x6")
    solver(_matrix, f_make_field(_matrix), futo)
    print(licznik)
    print(time.time()-ti)
    print(nawroty)
main()