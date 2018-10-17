import math
def tower_builder(n_floors):
    space = 1
    for i in range(n_floors-1):
        space+=2
    space = math.floor(space/2)
    asteriscs = 1
    res = []
    for i in range(n_floors):
        res_row = ''
        res_row = res_row + (' ' * space)
        res_row = res_row + ('*'* asteriscs)
        res_row = res_row + (' ' * space)
        space -=1
        asteriscs +=2
        res.append(res_row)
    return res
