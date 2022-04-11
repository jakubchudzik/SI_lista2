import copy

import numpy as np

def b_make_grid(file_name,field):
    with open(file_name, 'r') as file:
        binary = file.readlines()

    lista = []
    dziedziny = []

    for i in range(len(binary)):
        binary[i] = binary[i].strip()
        pom = []
        pomDziedziny=[]
        for j in binary[i]:
            if j == "x":
                pom.append('')
                pomDziedziny.append(copy.deepcopy(field))
            else:
                pom.append(j)
                pomDziedziny.append([])
        lista.append(pom)
        dziedziny.append(pomDziedziny)
    _matrix = np.array(lista)
    # _matrix_field= np.array(dziedziny)
    # print(_matrix)
    # for i in dziedziny:
    #     print(i)
    return  _matrix, dziedziny


def find_free_place(_matrix):
    for i in range(len(_matrix)):
        for j in range(len(_matrix[i])):
            if _matrix[i][j] == '':
                return (j, i)
    return False

#coord(col,row)
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
    list_of_not_matched=[]
    for i in field:
        counter = 0
        for j in range(len(_matrix)):
            if i == _matrix[row][j]:
                counter+=1
        if counter+1>limit_numbers:
            list_of_not_matched.append(i)
    return list_of_not_matched


def b_isOkColNumbers(_matrix, limit_numbers, field,coords):
    col = coords[0]
    pom = _matrix.T
    list_of_not_matched=[]
    for i in field:
        counter = 0
        for j in range(len(_matrix)):
            if i == pom[col][j]:
                counter+=1
        if counter+1>limit_numbers:
            list_of_not_matched.append(i)
    return list_of_not_matched

def act_field(_matrix,field,coords):
    for i in range(len(_matrix)):
        pair = (i,coords[0])
        if pair[0] == coords[0] and pair[1] == coords[1]:
            continue
        list_not_matched=b_isOkRowNumbers(_matrix,len(_matrix)//2,['0','1'],pair)
        if len(list_not_matched)>0:
            for k in list_not_matched:
                if k in field[coords[1]][i]:
                    field[coords[1]][i].remove(k)
        pair = (coords[1],i)
        list_not_matched=b_isOkColNumbers(_matrix,len(_matrix)//2,['0','1'],pair)
        if len(list_not_matched)>0:
            for k in list_not_matched:
                if k in field[i][pair[0]]:
                    field[i][pair[0]].remove(k)


def binary(_matrix,field,coords):
    if b_is_less_than_3_char(_matrix, coords, field) and b_is_different(_matrix, coords):
        return True
    return False

def solver(_matrix,field,function,coords=None):
    if coords == None:
        coords = find_free_place(_matrix)
    last_field = copy.deepcopy(field)
    if len(field[coords[1]][coords[0]])==0:
        return
    for i in field[coords[1]][coords[0]]:
        _matrix[coords[1]][coords[0]] = i
        field[coords[1]][coords[0]].remove(i)
        kord= (coords[1],coords[0])
        act_field(_matrix,field,kord)
        if function(_matrix,['0','1'],coords):
            free = find_free_place(_matrix)
            if free == False:
                print(_matrix)
            else:
                solver(_matrix,field,function,free)
        # field[coords[1]][coords[0]].append(i)
        # field[coords[1]][coords[0]].sort()
    field = last_field
    _matrix[coords[1]][coords[0]]=''

def main():
    field1 = ['0', '1']
    print('Binary 6x6')
    p = b_make_grid("data/text_6x6",field1)
    _matrix = p[0]
    dziedziny = p[1]
    solver(_matrix,dziedziny,binary)
    # for i in dziedziny:
    #     print(i)
    # #najpierw wiersz, potem kolumna
    # act_field(_matrix,dziedziny,(0,2))
    # print(_matrix)
    # for i in dziedziny:
    #     print(i)

main()