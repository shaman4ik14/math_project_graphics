"""
Program for working with graphics
(Give all additional and vital information)
"""
from sympy import *


def derivative_search(variable: str):
    local_variable = set()
    for elements in variable:
        if elements.isalpha():
            local_variable.add(elements)
    if len(local_variable) > 1 or len(local_variable) == 0:
        return False
    else:
        x = Symbol("x")
        limits = diff(variable, x)
        limits = str(limits)
        return limits

def search_root(variable:str):
    if 'x' in variable:
        current_split_info = variable.split()
        if '**2' in current_split_info[0]:
            try:
                a = float(current_split_info[0][0:current_split_info[0].index('x') - 1])
            except:
                a = 1
            c = 0
            b = 0
            if len(current_split_info) == 3:
                if 'x' in current_split_info[2]:
                    try:
                        if current_split_info[1] == '+':
                            b = float(current_split_info[2][0:current_split_info[2].index('x') - 1])
                        else:
                            b = -float(current_split_info[2][0:current_split_info[2].index('x') - 1])
                    except:
                        b = 1
                else:
                    try:
                        if current_split_info[1] == '+':
                            c = float(current_split_info[2][0:current_split_info[2].index('x') - 1])
                        else:
                            c = -float(current_split_info[2][0:current_split_info[2].index('x') - 1])
                    except:
                        c = 1
            else:
                try:
                    if current_split_info[1] == '+':
                        b = float(current_split_info[2][0:current_split_info[2].index('x') - 1])
                    else:
                        b = -float(current_split_info[2][0:current_split_info[2].index('x') - 1])
                except:
                    b = 1
                try:
                    if current_split_info[3] == '+':
                        c = float(current_split_info[4])
                    else:
                        c = -float(current_split_info[4])
                except:
                    c = 1
            # print(f'a iS {a}')
            # print(f'b iS {b}')
            # print(f'c iS {c}')
            discriminant = b ** 2 - 4 * a * c
            if discriminant < 0:
                return False
            elif discriminant == 0:
                x = -b / (2 * a)
                return [x]
            else:
                x1 = (-b + discriminant ** 0.5) / (2 * a)
                x2 = (-b - discriminant ** 0.5) / (2 * a)
                result = [x1, x2]
                return result
        elif '*x' in current_split_info[0] and 'x**' not in current_split_info[0]:
            if len(current_split_info) == 1:
                return [0]
            else:
                first = float(current_split_info[0][0:current_split_info[0].index('x') - 1])
                if current_split_info[1] == '-':
                    second = float(current_split_info[2])
                else:
                    second = -float(current_split_info[2])
                result = second/first
                return [result]
        else:
            current_roots = set()
            start_pos = -50
            end_pos = -start_pos
            while start_pos < end_pos:
                if abs(eval(variable, {'x': start_pos})) <= 0.1:
                    current_roots.add(round(start_pos, 2))
                start_pos += 0.005
            result = []
            current_elements = 100000000
            for elements in current_roots:
                if current_elements - elements > 0.35 or current_elements - elements < -0.35:
                    result.append(elements)
                    current_elements = elements
            return result
    else:
        return False

def search_intervals(variable, roots):
    result = []
    if roots:
        if len(roots) == 1:
            if eval(variable, {'x': roots[0] - 0.1}) > 0:
                res = f'зростає: (-∞;{roots[0]})'
                result.append(res)
            else:
                res = f'спадає: (-∞;{roots[0]})'
                result.append(res)
            if eval(variable, {'x': roots[0] + 0.1}) > 0:
                res = f'зростає: ({roots[0]}; +∞)'
                result.append(res)
            else:
                res = f'спадає: ({roots[0]}; +∞)'
                result.append(res)
        elif len(roots) == 2:
            roots = sorted(roots)
            #FIXME дописати для двох коренів які посортовані
            if eval(variable, {'x': roots[0] - 0.1}) > 0:
                res = f'зростає: (-∞;{roots[0]})'
                result.append(res)
            else:
                res = f'спадає: (-∞;{roots[0]})'
                result.append(res)

            if eval(variable, {'x': roots[0] + 0.1}) > 0:
                res = f'зростає: ({roots[0]};{roots[1]})'
                result.append(res)
            else:
                res = f'спадає: ({roots[0]};{roots[1]})'
                result.append(res)

            if eval(variable, {'x': roots[1] + 0.1}) > 0:
                res = f'зростає: ({roots[1]}; +∞)'
                result.append(res)
            else:
                res = f'спадає: ({roots[1]}; +∞)'
                result.append(res)
        return result
    else:
        return False

def search_convexity(variable, roots):
    result = []
    if roots:
        if len(roots) == 1:
            if eval(variable, {'x': roots[0] - 0.1}) > 0:
                res = f'вгнута: (-∞;{roots[0]})'
                result.append(res)
            else:
                res = f'опукла: (-∞;{roots[0]})'
                result.append(res)
            if eval(variable, {'x': roots[0] + 0.1}) > 0:
                res = f'вгнута: ({roots[0]}; +∞)'
                result.append(res)
            else:
                res = f'опукла: ({roots[0]}; +∞)'
                result.append(res)
        elif len(roots) == 2:
            roots = sorted(roots)
            #FIXME дописати для двох коренів які посортовані
            if eval(variable, {'x': roots[0] - 0.1}) > 0:
                res = f'вгнута: (-∞;{roots[0]})'
                result.append(res)
            else:
                res = f'опукла: (-∞;{roots[0]})'
                result.append(res)

            if eval(variable, {'x': roots[0] + 0.1}) > 0:
                res = f'вгнута: ({roots[0]};{roots[1]})'
                result.append(res)
            else:
                res = f'опукла: ({roots[0]};{roots[1]})'
                result.append(res)

            if eval(variable, {'x': roots[1] + 0.1}) > 0:
                res = f'вгнута: ({roots[1]}; +∞)'
                result.append(res)
            else:
                res = f'опукла: ({roots[1]}; +∞)'
                result.append(res)
        return result
    else:
        return False

def search_extremums(variable, pos):
    extremus = dict()
    for elements in range(1, len(pos)):
        if pos[elements][0] != pos[elements-1][0]:
            res_info = float(pos[elements].split('(')[1].split(';')[0])
            if pos[elements][0] == 'с':
                if [(res_info, eval(variable,{'x' : res_info}))] in extremus.values():
                    extremus['максимум'] += [(res_info, eval(variable,{'x' : res_info}))]
                else:
                    extremus['максимум'] = [(res_info, eval(variable, {'x': res_info}))]
            else:
                if [(res_info, eval(variable, {'x': res_info}))] in extremus.values():
                    extremus['мінімум'] += [(res_info, eval(variable, {'x': res_info}))]
                else:
                    extremus['мінімум'] = [(res_info, eval(variable, {'x': res_info}))]
    return extremus

def inflection_points(variable, pos):
    pos_of_inflection = set()
    for elements in range(1, len(pos)):
        if pos[elements][0] != pos[elements - 1][0]:
            res_info = float(pos[elements].split('(')[1].split(';')[0])
            local_inflection = (res_info, eval(variable, {'x' : res_info}))
            pos_of_inflection.add(local_inflection)
    return pos_of_inflection


def main():
    info = input()
    first_derivative = derivative_search(info)
    second_derivative = derivative_search(first_derivative)
    critical_points_1 = search_root(first_derivative)
    critical_points_2 = search_root(second_derivative)
    intervals_1 = search_intervals(first_derivative, critical_points_1)
    intervals_2 = search_convexity(second_derivative, critical_points_2)
    if type(intervals_1) != bool:
        extremums = search_extremums(info, intervals_1)
    else:
        extremums = False
    pos_inflection = False
    if type(intervals_2) != bool:
        pos_inflection = inflection_points(info, intervals_2)


    print(f"точки перетину з віссю OY: (0, {eval(info, {'x': 0})})")
    if type(search_root(info)) != bool:
        print(f'точки перетину з віссю OX: ',end="")
        for elements in range(len(search_root(info))-1):
            print((search_root(info)[elements], 0), end="; ")
        print((search_root(info)[-1], 0))
    else:
        print(f'перетину з віссю OX не існує')

    print(f'перша похідна: {first_derivative}')
    print(f'друга похідна: {second_derivative}')

    if type(critical_points_1) != bool:
        if len(critical_points_1) > 0:
            print(f'критичні точки першої похідної: ', end='')
            print(*critical_points_1, sep='; ')
        else:
            print(f'критичних точок першої похідної не існує')
    else:
        print(f'критичних точок першої похідної не існує')
    if type(critical_points_2) != bool:
        if len(critical_points_2) > 0:
            print(f'критичні точки другої похідної: ', end='')
            print(*critical_points_2, sep='; ')
        else:
            print(f'критичних точок другої похідної не існує')
    else:
        print(f'критичних точок другої похідної не існує')

    if type(intervals_1) != bool:
        print(*intervals_1, sep='; ')
    else:
        print(f'функція монотонна')
    if type(intervals_2) != bool:
        print(*intervals_2, sep='; ')
    else:
        print(f'інтервалів опуклості не існує')
    if type(extremums) != bool:
        print(f'екстремуми функції: ', end='')
        for elements in extremums.items():
            print(f'{elements[0]}: ', end='')
            print(*elements[1], sep='; ')
    else:
        print(f'функція не має екстремумів')
    if type(pos_inflection) != bool:
        print(f'точки перегину: ', end='')
        print(*pos_inflection, sep='; ')
    else:
        print(f'точок перегину не існує')

main()