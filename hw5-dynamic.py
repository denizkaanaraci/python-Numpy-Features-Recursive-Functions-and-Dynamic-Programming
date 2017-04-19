import sys
import numpy


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


def min_edit_distance_dynamic(matrix, word1, word2, len1, len2, outputfile):
    for i in range(0, len1 + 1):
        matrix[i][0] = i * 2

    for i in range(0, len2 + 1):
        matrix[0][i] = i * 2

    for i in range(1, len1 + 1):
        for j in range(1, len2 + 1):
            delta = 1 if word1[i - 1] != word2[j - 1] else 0
            matrix[i][j] = min(matrix[i - 1][j] + 2, matrix[i][j - 1] + 2, matrix[i - 1][j - 1] + delta)

    print_alignment(matrix, word1, word2, outputfile)


def file_open(inputfile, outputfile):
    f = open(inputfile, "r")
    toread = f.read()
    last = toread.splitlines()
    if len(last) == 2:
        target = last[0]
        source = last[1]
    else:
        target = last[0]
        source = []

    matrix = numpy.zeros((len(target) + 1, len(source) + 1), dtype=int)
    min_edit_distance_dynamic(matrix, target[::-1], source[::-1], len(target), len(source), outputfile)


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
