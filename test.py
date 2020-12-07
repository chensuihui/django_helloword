a = [(4,3), (1, 0)]
b = [(2, 0), (3, 1)]


def completion(line1: list, line2: list):
    for i in range(0, len(line1)):
        is_equal = False
        for j in range(0, len(line2)):
            if line1[i][0] == line2[j][0]:
                is_equal = True
        if not is_equal:
            line2.append((line1[i][0], 0))
    for i in range(0, len(line2)):
        is_equal = False
        for j in range(0, len(line1)):
            if line1[j][0] == line2[i][0]:
                is_equal = True
        if not is_equal:
            line1.append((line2[i][0], 0))
    return (line1, line2)


def order_fun(line: list):
    x = []
    result_line = []
    for i in range(0, len(line)):
        x.append(line[i][0])
    for i in range(1, 13):
        if i in x:
            result_line.append(line[x.index(i)])
    return result_line

print(order_fun(a))
