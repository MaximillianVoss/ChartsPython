# coding: utf-8

from matplotlib import pyplot as plt


def GetMatrix(filename):
    matrix = []
    try:
        file = open(filename)
        for line in file:
            matrix.append([float(x) for x in line.split()])
    except FileNotFoundError:
        print("file {0} not found!".format(filename))
    return matrix


def GetChart(matrix, title):
    mult = 4
    step = 5
    start = -10
    plt.figure()
    if len(matrix) > 3:
        for i in range(0, 5):
            plt.plot(range(0, len(matrix[i]) * mult, mult), matrix[i], label="y={0}".format(start))
            start += step
    plt.title(title)
    plt.legend()


def GetBar(matrix, title):
    plt.figure()
    plt.bar(range(len(matrix[0])), matrix[0])
    plt.title(title)


titles = ["Red", "Green", "Blue"]
for i in range(0, len(titles)):
    GetChart(GetMatrix("{0}.txt".format(titles[i])), titles[i])

titles = ["Y", "Cb", "Cr", "DAB", "DACb", "DACr", "DAG", "DAR", "DAY", "HB", "HCb", "HCr", "HG", "HR", "HY"]
for i in range(0, len(titles)):
    GetBar(GetMatrix("{0}.txt".format(titles[i])), titles[i])
plt.show()
