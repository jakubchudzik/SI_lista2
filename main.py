import numpy as np

def isOkRowNumbers(_matrix,limit_numbers,field):
    for i in field:
        for j in _matrix:
            temp_count=0
            for k in j:
                if i==k:
                    temp_count+=1
            if temp_count>limit_numbers:
                return False
    return True
def isOkColNumbers(_matrix,limit_numbers,field):
    for i in field:
        for j in range(len(_matrix)):
            temp_count=0
            for k in range(len(_matrix)):
                if i == _matrix[k][j]:
                    temp_count+=1
            if temp_count>limit_numbers:
                return False
    return True
def areDifRows(_matrix):
    for i in range(len(_matrix)):
        for j in range(i+1,len(_matrix)):
            if np.array_equal(_matrix[i],_matrix[j]):
                return False


def main():
    with open("data\\binary_6x6",'r') as file:
        binary = file.readlines()

    lista = []

    field1=['0','1']

    for i in range(len(binary)):
        binary[i]=binary[i].strip()
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
            if _matrix[i][j]=='':
                coords = (i,j)

    limit_numbers = len(_matrix)//2
    print(_matrix)
    print()
    print(_matrix.T)

if __name__ == '__main__':
    main()