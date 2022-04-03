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


def isOkRowNumbers(_matrix, limit_numbers, field):
    for i in field:
        for j in _matrix:
            temp_count = 0
            for k in j:
                if i == k:
                    temp_count += 1
            if temp_count > limit_numbers:
                return False
    return True


def isOkColNumbers(_matrix, limit_numbers, field):
    for i in field:
        for j in range(len(_matrix)):
            temp_count = 0
            for k in range(len(_matrix)):
                if i == _matrix[k][j]:
                    temp_count += 1
            if temp_count > limit_numbers:
                return False
    return True


def areDifRows(_matrix):
    for i in range(len(_matrix)):
        for j in range(i + 1, len(_matrix)):
            if np.array_equal(_matrix[i], _matrix[j]):
                return False


def main():
    with open("data/text_6x6", 'r') as file:
        binary = file.readlines()

    lista = []

    field1 = ['0', '1']

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

    stack = []
    coords = None
    for i in range(len(_matrix)):
        for j in range(len(_matrix[i])):
            if _matrix[i][j] == '':
                coords = (i, j)

    limit_numbers = len(_matrix) // 2
    print(_matrix)
    print(is_different(_matrix, (0, 0)))


main()

