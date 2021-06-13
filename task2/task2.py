import json
import sys


def load_data(file_name):
    with open(file_name, 'r') as file:
        content = file.read()
        try:
            data = json.loads(content)
        except json.decoder.JSONDecodeError:
            b = content.replace('sphere', '"sphere"').replace('center', '"center"').replace('radius', '"radius"').replace('line', '"line"').replace('{[', '[[').replace(']}', ']]')
            data = json.loads(b)
        sphere = data['sphere']
        line = data['line']
        return sphere, line


def solution(x1, x2, t):
    x = (x2 - x1) * t + x1
    return round(x, 2)


def compute_collision(sphere, line):
    xc, yc, zc = sphere["center"]
    r = sphere["radius"]
    x1, y1, z1 = line[0]
    x2, y2, z2 = line[1]
    m = x2 - x1
    n = y2 - y1
    p = z2 - z1
    c = (x1 - xc) ** 2 + (y1 - yc) ** 2 + (z1 - zc) ** 2 - r ** 2
    a = m ** 2 + n ** 2 + p ** 2
    b = 2 * m * (x1 - xc) + 2 * n * (y1 - yc) + 2 * p * (z1 - zc)
    discr = b ** 2 - 4*a*c
    if discr < 0:
        return 'Коллизий не обнаружено'

    elif discr == 0:
        t0 = -b / (2*a)
        point = [solution(x1, x2, t0), solution(y1, y2, t0), solution(z1, z2, t0)]
        return point

    elif discr > 0:
        t1 = (-b + discr ** 0.5)/(2*a)
        t2 = (-b - discr ** 0.5)/(2*a)
        point1 = [solution(x1, x2, t1), solution(y1, y2, t1), solution(z1, z2, t1)]
        point2 = [solution(x1, x2, t2), solution(y1, y2, t2), solution(z1, z2, t2)]
        return point1, point2


def print_result(result):
    if type(result) == str:
        print(result)
    elif type(result) == tuple:
        print(result[0])
        print(result[1])
    elif type(result) == list:
        print(result)


def main():
    try:
        file_name = sys.argv[1]
        sphere, line = load_data(file_name)
        result = compute_collision(sphere, line)
        print_result(result)

    except IndexError:
        print('invalid arguments') #если не передали имя файла
    except FileNotFoundError:
        print('file not found')


if __name__ == "__main__":
    main()
