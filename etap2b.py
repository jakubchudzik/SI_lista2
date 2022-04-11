import copy

import numpy as np
licznik =0
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
    return  lista
def b_make_field_grid(_matrix,field):
    lista = []
    for i in range(len(_matrix)):
        pom = []
        for j in range(len(_matrix)):
            if _matrix[i][j]!='':
                pom.append([])
            else:
                pom.append(copy.deepcopy(field))
        lista.append(pom)
    return lista

def act_field_grid_half_in_rows_and_cols(_matrix,field_grid,field):
    for i in range(len(_matrix)):
        for k in field:
            counter = _matrix[i].count(k)
            if counter>=len(_matrix)//2:
                for j in range(len(_matrix)):
                    if k in field_grid[i][j]:
                       field_grid[i][j].remove(k)
    for j in range(len(_matrix)):
        for k in field:
            counter = 0
            for i in range(len(_matrix)):
                if _matrix[i][j]==k:
                    counter+=1
            if counter>=len(_matrix)//2:
                for i in range(len(_matrix)):
                    if k in field_grid[i][j]:
                        field_grid[i][j].remove(k)

def act_field_grid_3_in_rows(_matrix,field_grid,field):
    for i in range(len(_matrix)):
        for k in field:
            l = 0
            p = 0
            counter=0
            for j in range(len(_matrix)):
                if _matrix[i][j]==k:
                    counter+=1
                    if counter==1:
                        l=j
                    p=j
                else:
                    if counter ==2:
                        if l-1>=0:
                            if k in field_grid[i][l-1]:
                                field_grid[i][l-1].remove(k)
                        if p+1<len(_matrix):
                            if k in field_grid[i][p+1]:
                                field_grid[i][p+1].remove(k)
                    counter=0

            for j in range(len(_matrix)-2):
                if _matrix[i][j]==_matrix[i][j+2]==k:
                    if _matrix[i][j] in field_grid[i][j+1]:
                        field_grid[i][j+1].remove(_matrix[i][j])
def act_field_grid_3_in_cols(_matrix,field_grid,field):
    for j in range(len(_matrix)):
        for k in field:
            l = 0
            p = 0
            counter=0
            for i in range(len(_matrix)):
                if _matrix[i][j]==k:
                    counter+=1
                    if counter==1:
                        l=i
                    p=i
                else:
                    if counter ==2:
                        if l-1>=0:
                            if k in field_grid[l-1][j]:
                                field_grid[l-1][j].remove(k)
                        if p+1<len(_matrix):
                            if k in field_grid[p+1][j]:
                                field_grid[p+1][j].remove(k)
                    counter=0
            for i in range(len(_matrix)-2):
                if _matrix[i][j]==_matrix[i+2][j]==k:
                    if _matrix[i][j] in field_grid[i+1][j]:
                        field_grid[i+1][j].remove(_matrix[i][j])

def isDifferentRow(rowNumber,_matrix):
    if '' in _matrix[rowNumber]:
        return True
    for i in range(len(_matrix)):
        if i!=rowNumber:
            if '' not in _matrix[i]:
                counter = 0
                for j in range(len(_matrix)):
                    if _matrix[i][j]==_matrix[rowNumber][j]:
                        counter+=1
                if counter == len(_matrix):
                    return False
    return True
def isDifferentCol(colNumber,_matrix):
    for i in range(len(_matrix)):
        if _matrix[i][colNumber]=='':
            return True
    for j in range(len(_matrix)):
        if j!=colNumber:
            hasEmpty=False
            for i in range(len(_matrix)):
                if _matrix[i][j] == '':
                    hasEmpty=True
                    break
            if not hasEmpty:
                counter = 0
                for i in range(len(_matrix)):
                    if _matrix[i][colNumber] == _matrix[i][j]:
                        counter +=1
                if counter == len(_matrix):
                    return False
    return True
def find_free_place(_matrix):
    for i in range(len(_matrix)):
        for j in range(len(_matrix[i])):
            if _matrix[i][j] == '':
                return (i, j)
    return False

def print_list(lista):
    for i in lista:
        print(i)

def isEmptyField(_matrix,field_grid):
    for i in range(len(_matrix)):
        for j in range(len(_matrix)):
            a=_matrix[i][j]
            b= field_grid[i][j]
            if a=='' and len(b)==0:
                return True
    return False
def act_field_grid_all(_matrix,field_grid,field):
    act_field_grid_half_in_rows_and_cols(_matrix,field_grid,field)
    act_field_grid_3_in_rows(_matrix,field_grid,field)
    act_field_grid_3_in_cols(_matrix,field_grid,field)

def solver(_matrix,field_grid,field):
    global licznik
    licznik+=1
    free_place = find_free_place(_matrix)
    if free_place == False:
        print_list(_matrix)

        return
    temp_field = copy.deepcopy(field_grid[free_place[0]][free_place[1]])
    for k in field_grid[free_place[0]][free_place[1]]:
        _matrix[free_place[0]][free_place[1]]=k
        copy_field_grid = copy.deepcopy(field_grid)
        if isDifferentRow(free_place[0],_matrix) and isDifferentCol(free_place[1],_matrix):
            field_grid[free_place[0]][free_place[1]]=[]
            act_field_grid_all(_matrix,field_grid,field)
            if not isEmptyField(_matrix,field_grid):
                solver(_matrix,field_grid,field)
        field_grid = copy_field_grid


    _matrix[free_place[0]][free_place[1]]=''
    field_grid[free_place[0]][free_place[1]] = temp_field


def test():
    field1 = ['0', '1']
    print('Binary 10x10')
    p = b_make_grid("data/binary_10x10")
    f = b_make_field_grid(p,field1)
    act_field_grid_half_in_rows_and_cols(p,f,field1)
    act_field_grid_3_in_rows(p,f,field1)
    act_field_grid_3_in_cols(p,f,field1)
    solver(p,f,field1)
    global licznik
    print(licznik)
test()