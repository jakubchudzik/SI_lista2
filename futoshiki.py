import time

import numpy as np
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
def futo(_matrix,field,coords):
    if f_is_ok_row(_matrix, field, coords) and f_is_ok_col(_matrix, field, coords) and f_is_ok_with_sanctions(_matrix,coords):
        return True
    return False

def solver(_matrix,field,function,coords=None):
    if coords == None:
        coords = find_free_place(_matrix)
    for i in field:
        _matrix[coords[1]][coords[0]] = i
        if function(_matrix,field,coords):
            free = find_free_place(_matrix)
            if free == False:
                print(_matrix)
            else:
                solver(_matrix,field,futo,find_free_place(_matrix))
    _matrix[coords[1]][coords[0]] = ''



def main():
    t1 = time.time()
    _matrix = f_make_grid("data/futoshiki_4x4")
    #print(_matrix)
    solver(_matrix,f_make_field(_matrix),futo)
    # print(f_is_ok_with_sanctions(_matrix,(0,4)))
main()