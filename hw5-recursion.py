import numpy
import sys


def print_alignment(matrix, w1, w2, outputfile):
    outputWrite = open(outputfile, "w")
    outputWrite.write(''.join("Edit Distance = ".__str__()) + ''.join(matrix[len(w1)][len(w2)].__str__()) + '\n')
    i1 = len(w1) - 1
    i2 = len(w2) - 1
    while True:
        if i1 == -1 or i2 == -1:
            break

        cost = 0
        a = matrix[i1][i2]
        if w1[i1] != w2[i2]:
            a += 1
            cost = 1

        b = matrix[i1][i2 + 1] + 2
        c = matrix[i1 + 1][i2] + 2

        m = min(a, b, c)

        if m == a:
            outputWrite.write(
                ''.join(w1[i1].__str__()) + " " + ''.join(w2[i2].__str__()) + " " + ''.join(cost.__str__()) + '\n')

            i1 -= 1
            i2 -= 1
        elif m == b:
            outputWrite.write(
                ''.join(w1[i1].__str__()) + " " + ''.join("-".__str__()) + " " + ''.join("2".__str__()) + '\n')

            i1 -= 1
        elif m == c:
            outputWrite.write(
                ''.join("-".__str__()) + " " + ''.join(w2[i2].__str__()) + " " + ''.join("2".__str__()) + '\n')

            i2 -= 1

    while i1 >= 0:
        outputWrite.write(
            ''.join(w1[i1].__str__()) + " " + ''.join("-".__str__()) + " " + ''.join("2".__str__()) + '\n')

        i1 -= 1

    while i2 >= 0:
        outputWrite.write(
            ''.join("-".__str__()) + " " + ''.join(w2[i2].__str__()) + " " + ''.join("2".__str__()) + '\n')

        i2 -= 1

    outputWrite.close()


def min_edit_distance_recursive(s1, s2, n, m, matrix, outputfile):
    if n == 0 and m == 0:
        return 0

    if n == 0:
        matrix[n][m] = 2 * m
        return m * 2

    if m == 0:
        matrix[n][m] = 2 * n
        return n * 2

    delta = 1 if s1[n - 1] != s2[m - 1] else 0
    a = min_edit_distance_recursive(s1, s2, n - 1, m - 1, matrix, outputfile) + delta
    b = min_edit_distance_recursive(s1, s2, n - 1, m, matrix, outputfile) + 2
    c = min_edit_distance_recursive(s1, s2, n, m - 1, matrix, outputfile) + 2

    matrix[n][m] = min(a, b, c)

    return matrix[n][m]


def file_open(inputfile, outputfile):
    f = open(inputfile, "r")
    toread = f.read()
    last = toread.splitlines()
    f.close()
    if len(last) == 2:
        target = last[0]
        source = last[1]
    else:
        target = last[0]
        source = []

    matrix = numpy.zeros((len(target) + 1, len(source) + 1), dtype=int)
    min_edit_distance_recursive(target[::-1], source[::-1], len(target), len(source), matrix, outputfile)
    print_alignment(matrix, target[::-1], source[::-1], outputfile)


def starter():
    if __name__ == '__main__':
        k = 2
        inputfile = 2
        outputfile = 2

        if k > 1:
            inputfile = sys.argv[1]
            outputfile = sys.argv[2]
        file_open(inputfile, outputfile)
        pass


starter()
