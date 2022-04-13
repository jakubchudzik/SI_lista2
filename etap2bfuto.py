import copy
licznik =0

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
                if i %2 ==1:
                    pom.append('-')
        if i%2==1:
            pom=pom[:-1]
        lista.append(pom)
    return  lista

def make_field_grid(_matrix,field):
    lista = []
    for i in _matrix:
        pom=[]
        for j in i:
            if j == '':
                pom.append(copy.deepcopy(field))
            else:
                pom.append(j)
        lista.append(pom)
    return lista
def act_field_grid_constraints(_matrix,field_grid,field):
    #act rows
    for i in range(len(_matrix)):
        for k in field:
            if _matrix[i].count(k)>0:
                for j in range(len(_matrix[i])):
                    if _matrix[i][j]=='':
                        if k in field_grid[i][j]:
                            field_grid[i][j].remove(k)
    #act cols
    for j in range(len(_matrix)):
        for k in field:
            isk =False
            for i in range(len(_matrix)):
                if k == _matrix[i][j]:
                    isk=True
                    break
            if isk:
                for i in range(len(_matrix)):
                    if _matrix[i][j]=='':
                        if k in field_grid[i][j]:
                            field_grid[i][j].remove(k)
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
def act_field_grid_constraints_numbers(_matrix,field_grid,field):
    for i in range(len(_matrix)):
        for j in range(len(_matrix)):
            if _matrix[i][j] in field:
                if j+2<len(_matrix):
                    if _matrix[i][j+1] != '-':
                        temp = copy.deepcopy(field_grid[i][j+2])
                        for k in temp:
                            if not f_is_ok(_matrix[i][j],k,_matrix[i][j+1]):
                                field_grid[i][j+2].remove(k)
                if j-2 >=0:
                    if _matrix[i][j-1] != '-':
                        temp = copy.deepcopy(field_grid[i][j-2])
                        for k in temp:
                            if not f_is_ok(k,_matrix[i][j],_matrix[i][j-1]):
                                field_grid[i][j-2].remove(k)
                if i+2<len(_matrix):
                    if _matrix[i+1][j] != '-':
                        temp = copy.deepcopy(field_grid[i+2][j])
                        for k in temp:
                            if not f_is_ok(_matrix[i][j],k,_matrix[i+1][j]):
                                field_grid[i+2][j].remove(k)
                if i-2 >=0:
                    if _matrix[i-1][j] != '-':
                        temp =copy.deepcopy(field_grid[i-2][j])
                        for k in temp:
                            if not f_is_ok(k,_matrix[i][j],_matrix[i-1][j]):
                                field_grid[i-2][j].remove(k)


def print_list(lista):
    for i in lista:
        print(i)

def find_free_place(_matrix):
    for i in range(len(_matrix)):
        for j in range(len(_matrix[i])):
            if _matrix[i][j] == '':
                return (i, j)
    return False

def act_field_grid_all(_matrix,field_grid,field):
    act_field_grid_constraints(_matrix,field_grid,field)
    act_field_grid_constraints_numbers(_matrix,field_grid,field)

def isEmptyField(_matrix,field_grid):#
    for i in range(len(_matrix)):
        for j in range(len(_matrix)):
            a=_matrix[i][j]
            b= field_grid[i][j]
            if a=='' and len(b)==0:
                return True
    return False
def nothing(a=None,b=None):
    return True

def find_free_place_smalest_field(_matrix,field_grid):
    mini = None
    result = None
    for i in range(len(_matrix)):
        for j in range(len(_matrix[i])):
            if _matrix[i][j] == '':
                if mini==None or mini > len(field_grid[i][j]):
                    mini = len(field_grid[i][j])
                    result = (i,j)
                    if mini ==1:
                        return result
    if mini ==None:
        return False
    return result
def solver(_matrix,field_grid,field,find_function,constraint_function):
    global licznik
    licznik+=1
    free_place = find_function(_matrix,field_grid)
    if free_place == False:
        print_list(_matrix)
        return
    temp_field = copy.deepcopy(field_grid[free_place[0]][free_place[1]])
    for k in field_grid[free_place[0]][free_place[1]]:
        _matrix[free_place[0]][free_place[1]]=k
        copy_field_grid = copy.deepcopy(field_grid)
        if constraint_function(free_place,_matrix):
            field_grid[free_place[0]][free_place[1]]=[]
            act_field_grid_all(_matrix,field_grid,field)
            if not isEmptyField(_matrix,field_grid):
                solver(_matrix,field_grid,field,find_function,constraint_function)
        field_grid = copy_field_grid
    _matrix[free_place[0]][free_place[1]]=''
    field_grid[free_place[0]][free_place[1]] = temp_field
def test():
    field = ['1','2','3','4','5']
    p = f_make_grid("data/futoshiki_5x5")
    g = make_field_grid(p,field)
    act_field_grid_constraints(p,g,field)
    act_field_grid_constraints_numbers(p,g,field)
    solver(p,g,field,find_free_place_smalest_field,nothing)
    global licznik
    print(licznik)
test()