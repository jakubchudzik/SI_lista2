import numpy as np

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
            if i % 2 ==1:
                pom.append('')
        if i%2==1:
            pom.pop()
        lista.append(np.array(pom))
    _matrix = np.array(lista)
    return  _matrix


def rec_futo(_matrix,field,coords):
    pass

def make_field(_matrix):
    field = []
    for i in range(len(_matrix)//2+1):
        field.append(f'{i+1}')
    return field

def find_free_place(_matrix):
    coords = None
    for i in range(0,len(_matrix),2):
        for j in range(0,len(_matrix[i]),2):
            if _matrix[i][j] == '':
                return (i, j)
    return False


def main():
    _matrix = make_grid("data/futoshiki_4x4")
    #rec_futo(_matrix,make_field(_matrix),)
    print(find_free_place(_matrix))
main()