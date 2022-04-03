import numpy as np
def is_different(_matrix, coords):
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

def is_less_than_3_char(_matrix, coords, field):
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

def isOkRowNumbers(_matrix, limit_numbers, field,coords):
    row = coords[1]
    for i in field:
        counter = 0
        for j in range(len(_matrix)):
            if i == _matrix[row][j]:
                counter+=1
        if counter>limit_numbers:
            return False
    return True


def isOkColNumbers(_matrix, limit_numbers, field,coords):
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


def make_grid(file_name):
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
def find_free_place(_matrix):
    coords = None
    for i in range(len(_matrix)):
        for j in range(len(_matrix[i])):
            if _matrix[i][j] == '':
                return (i, j)
    return False


def rec_met(_matrix, coords,field):
    global p
    p+=1
    limit_numbers = len(_matrix) // 2
    for i in field:
        _matrix[coords[0]][coords[1]] = i
        if is_less_than_3_char(_matrix, (coords[1], coords[0]), field) and is_different(_matrix, (coords[1], coords[0])) and isOkRowNumbers(_matrix, limit_numbers, field, (coords[1], coords[0])) and isOkColNumbers(_matrix, limit_numbers, field, (coords[1], coords[0])):
            free = find_free_place(_matrix)
            if free == False:
                print(_matrix)
            else:
                rec_met(_matrix,free,field)
    _matrix[coords[0]][coords[1]]=''



def main():

    field1 = ['0', '1']

    print('Binary 6x6')
    _matrix = make_grid("data/binary_6x6")
    rec_met(_matrix,find_free_place(_matrix),field1)
    print('------------------------')
    print('Binary 8x8')
    _matrix = make_grid("data/binary_8x8")
    rec_met(_matrix, find_free_place(_matrix), field1)
    print('------------------------')
    print('Binary 10x10')
    _matrix = make_grid("data/binary_10x10")
    rec_met(_matrix, find_free_place(_matrix), field1)

main()

