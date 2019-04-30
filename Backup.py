# coding: utf-8

from matplotlib import pyplot as plt


#4b
f_R = open('C:/Users/akopo/source/repos/cos/cos/c0', 'r')
f_G = open('C:/Users/akopo/source/repos/cos/cos/c1', 'r')
f_B = open('C:/Users/akopo/source/repos/cos/cos/c2', 'r')

array_R = []
array_G = []
array_B = []

for line in f_R:
    array_R.append([float(x) for x in line.split()])
for line in f_G:
    array_G.append([float(x) for x in line.split()])
for line in f_B:
    array_B.append([float(x) for x in line.split()])


mult = 4


plt.figure()
plt.plot(range(0, len(array_R[0]) * mult, mult), array_R[0], label="y = -10")
plt.plot(range(0, len(array_R[1]) * mult, mult), array_R[1], label="y = -5")
plt.plot(range(0, len(array_R[2]) * mult, mult), array_R[2], label="y = 0")
plt.plot(range(0, len(array_R[3]) * mult, mult), array_R[3], label="y = 5")
plt.plot(range(0, len(array_R[4]) * mult, mult), array_R[4], label="y = 10")
plt.title("R")
plt.legend()


plt.figure()
plt.plot(range(0, len(array_G[0]) * mult, mult), array_G[0], label="y = -10")
plt.plot(range(0, len(array_G[1]) * mult, mult), array_G[1], label="y = -5")
plt.plot(range(0, len(array_G[2]) * mult, mult), array_G[2], label="y = 0")
plt.plot(range(0, len(array_G[3]) * mult, mult), array_G[3], label="y = 5")
plt.plot(range(0, len(array_G[4]) * mult, mult), array_G[4], label="y = 10")
plt.title("G")
plt.legend()


plt.figure()
plt.plot(range(0, len(array_B[0]) * mult, mult), array_B[0], label="y = -10")
plt.plot(range(0, len(array_B[1]) * mult, mult), array_B[1], label="y = -5")
plt.plot(range(0, len(array_B[2]) * mult, mult), array_B[2], label="y = 0")
plt.plot(range(0, len(array_B[3]) * mult, mult), array_B[3], label="y = 5")
plt.plot(range(0, len(array_B[4]) * mult, mult), array_B[4], label="y = 10")
plt.title("B")
plt.legend()



#12
f_hist12R = open('C:/Users/akopo/source/repos/cos/cos/histogramR', 'r')
f_hist12G = open('C:/Users/akopo/source/repos/cos/cos/histogramG', 'r')
f_hist12B = open('C:/Users/akopo/source/repos/cos/cos/histogramB', 'r')
f_hist12Y = open('C:/Users/akopo/source/repos/cos/cos/histogramY', 'r')
f_hist12Cb = open('C:/Users/akopo/source/repos/cos/cos/histogramCb', 'r')
f_hist12Cr = open('C:/Users/akopo/source/repos/cos/cos/histogramCr', 'r')

array_hist12R = []
array_hist12G = []
array_hist12B = []
array_hist12Y = []
array_hist12Cb = []
array_hist12Cr = []

for line in f_hist12R:
    array_hist12R.append([int(x) for x in line.split()])
for line in f_hist12G:
    array_hist12G.append([int(x) for x in line.split()])
for line in f_hist12B:
    array_hist12B.append([int(x) for x in line.split()])
for line in f_hist12Y:
    array_hist12Y.append([int(x) for x in line.split()])
for line in f_hist12Cb:
    array_hist12Cb.append([int(x) for x in line.split()])
for line in f_hist12Cr:
    array_hist12Cr.append([int(x) for x in line.split()])


plt.figure()
plt.bar(range(256), array_hist12R[0])
plt.title("Гистограмма R")

plt.figure()
plt.bar(range(256), array_hist12G[0])
plt.title("Гистограмма G")

plt.figure()
plt.bar(range(256), array_hist12B[0])
plt.title("Гистограмма B")

plt.figure()
plt.bar(range(256), array_hist12Y[0])
plt.title("Гистограмма Y")

plt.figure()
plt.bar(range(256), array_hist12Cb[0])
plt.title("Гистограмма Cb")

plt.figure()
plt.bar(range(256), array_hist12Cr[0])
plt.title("Гистограмма Cr")


f_hist15R1 = open('C:/Users/akopo/source/repos/cos/cos/DR1', 'r')
f_hist15R2 = open('C:/Users/akopo/source/repos/cos/cos/DR2', 'r')
f_hist15R3 = open('C:/Users/akopo/source/repos/cos/cos/DR3', 'r')
f_hist15R4 = open('C:/Users/akopo/source/repos/cos/cos/DR4', 'r')
f_hist15G1 = open('C:/Users/akopo/source/repos/cos/cos/DG1', 'r')
f_hist15G2 = open('C:/Users/akopo/source/repos/cos/cos/DG2', 'r')
f_hist15G3 = open('C:/Users/akopo/source/repos/cos/cos/DG3', 'r')
f_hist15G4 = open('C:/Users/akopo/source/repos/cos/cos/DG4', 'r')
f_hist15B1 = open('C:/Users/akopo/source/repos/cos/cos/DB1', 'r')
f_hist15B2 = open('C:/Users/akopo/source/repos/cos/cos/DB2', 'r')
f_hist15B3 = open('C:/Users/akopo/source/repos/cos/cos/DB3', 'r')
f_hist15B4 = open('C:/Users/akopo/source/repos/cos/cos/DB4', 'r')
f_hist15Y1 = open('C:/Users/akopo/source/repos/cos/cos/DY1', 'r')
f_hist15Y2 = open('C:/Users/akopo/source/repos/cos/cos/DY2', 'r')
f_hist15Y3 = open('C:/Users/akopo/source/repos/cos/cos/DY3', 'r')
f_hist15Y4 = open('C:/Users/akopo/source/repos/cos/cos/DY4', 'r')
f_hist15Cb1 = open('C:/Users/akopo/source/repos/cos/cos/DCb1', 'r')
f_hist15Cb2 = open('C:/Users/akopo/source/repos/cos/cos/DCb2', 'r')
f_hist15Cb3 = open('C:/Users/akopo/source/repos/cos/cos/DCb3', 'r')
f_hist15Cb4 = open('C:/Users/akopo/source/repos/cos/cos/DCb4', 'r')
f_hist15Cr1 = open('C:/Users/akopo/source/repos/cos/cos/DCR1', 'r')
f_hist15Cr2 = open('C:/Users/akopo/source/repos/cos/cos/DCR2', 'r')
f_hist15Cr3 = open('C:/Users/akopo/source/repos/cos/cos/DCr3', 'r')
f_hist15Cr4 = open('C:/Users/akopo/source/repos/cos/cos/DCr4', 'r')


array_hist15R1 = []
array_hist15R2 = []
array_hist15R3 = []
array_hist15R4 = []
array_hist15G1 = []
array_hist15G2 = []
array_hist15G3 = []
array_hist15G4 = []
array_hist15B1 = []
array_hist15B2 = []
array_hist15B3 = []
array_hist15B4 = []
array_hist15Y1 = []
array_hist15Y2 = []
array_hist15Y3 = []
array_hist15Y4 = []
array_hist15Cb1 = []
array_hist15Cb2 = []
array_hist15Cb3 = []
array_hist15Cb4 = []
array_hist15Cr1 = []
array_hist15Cr2 = []
array_hist15Cr3 = []
array_hist15Cr4 = []


for line in f_hist15R1:
    array_hist15R1.append([int(x) for x in line.split()])
for line in f_hist15R2:
    array_hist15R2.append([int(x) for x in line.split()])
for line in f_hist15R3:
    array_hist15R3.append([int(x) for x in line.split()])
for line in f_hist15R4:
    array_hist15R4.append([int(x) for x in line.split()])

for line in f_hist15G1:
    array_hist15G1.append([int(x) for x in line.split()])
for line in f_hist15G2:
    array_hist15G2.append([int(x) for x in line.split()])
for line in f_hist15G3:
    array_hist15G3.append([int(x) for x in line.split()])
for line in f_hist15G4:
    array_hist15G4.append([int(x) for x in line.split()])

for line in f_hist15B1:
    array_hist15B1.append([int(x) for x in line.split()])
for line in f_hist15B2:
    array_hist15B2.append([int(x) for x in line.split()])
for line in f_hist15B3:
    array_hist15B3.append([int(x) for x in line.split()])
for line in f_hist15B4:
    array_hist15B4.append([int(x) for x in line.split()])

for line in f_hist15Y1:
    array_hist15Y1.append([int(x) for x in line.split()])
for line in f_hist15Y2:
    array_hist15Y2.append([int(x) for x in line.split()])
for line in f_hist15Y3:
    array_hist15Y3.append([int(x) for x in line.split()])
for line in f_hist15Y4:
    array_hist15Y4.append([int(x) for x in line.split()])

for line in f_hist15Cb1:
    array_hist15Cb1.append([int(x) for x in line.split()])
for line in f_hist15Cb2:
    array_hist15Cb2.append([int(x) for x in line.split()])
for line in f_hist15Cb3:
    array_hist15Cb3.append([int(x) for x in line.split()])
for line in f_hist15Cb4:
    array_hist15Cb4.append([int(x) for x in line.split()])

for line in f_hist15Cr1:
    array_hist15Cr1.append([int(x) for x in line.split()])
for line in f_hist15Cr2:
    array_hist15Cr2.append([int(x) for x in line.split()])
for line in f_hist15Cr3:
    array_hist15Cr3.append([int(x) for x in line.split()])
for line in f_hist15Cr4:
    array_hist15Cr4.append([int(x) for x in line.split()])

plt.figure()
plt.bar(range(256), array_hist15R1[0])
plt.title("Гистограмма DR rule 1")

plt.figure()
plt.bar(range(256), array_hist15R2[0])
plt.title("Гистограмма DR rule 2")

plt.figure()
plt.bar(range(256), array_hist15R3[0])
plt.title("Гистограмма DR rule 3")

plt.figure()
plt.bar(range(256), array_hist15R4[0])
plt.title("Гистограмма DR rule 4")


plt.figure()
plt.bar(range(256), array_hist15G1[0])
plt.title("Гистограмма DG rule 1")

plt.figure()
plt.bar(range(256), array_hist15G2[0])
plt.title("Гистограмма DG rule 2")

plt.figure()
plt.bar(range(256), array_hist15G3[0])
plt.title("Гистограмма DG rule 3")

plt.figure()
plt.bar(range(256), array_hist15G4[0])
plt.title("Гистограмма DG rule 4")


plt.figure()
plt.bar(range(256), array_hist15B1[0])
plt.title("Гистограмма DB rule 1")

plt.figure()
plt.bar(range(256), array_hist15B2[0])
plt.title("Гистограмма DB rule 2")

plt.figure()
plt.bar(range(256), array_hist15B3[0])
plt.title("Гистограмма DB rule 3")

plt.figure()
plt.bar(range(256), array_hist15B4[0])
plt.title("Гистограмма DB rule 4")


plt.figure()
plt.bar(range(256), array_hist15Y1[0])
plt.title("Гистограмма DY rule 1")

plt.figure()
plt.bar(range(256), array_hist15Y2[0])
plt.title("Гистограмма DY rule 2")

plt.figure()
plt.bar(range(256), array_hist15Y3[0])
plt.title("Гистограмма DY rule 3")

plt.figure()
plt.bar(range(256), array_hist15Y4[0])
plt.title("Гистограмма DY rule 4")


plt.figure()
plt.bar(range(256), array_hist15Cb1[0])
plt.title("Гистограмма DCb rule 1")

plt.figure()
plt.bar(range(256), array_hist15Cb2[0])
plt.title("Гистограмма DCb rule 2")

plt.figure()
plt.bar(range(256), array_hist15Cb3[0])
plt.title("Гистограмма DCb rule 3")

plt.figure()
plt.bar(range(256), array_hist15Cb4[0])
plt.title("Гистограмма DCb rule 4")


plt.figure()
plt.bar(range(256), array_hist15Cr1[0])
plt.title("Гистограмма DCr rule 1")

plt.figure()
plt.bar(range(256), array_hist15Cr2[0])
plt.title("Гистограмма DCr rule 2")

plt.figure()
plt.bar(range(256), array_hist15Cr3[0])
plt.title("Гистограмма DCr rule 3")

plt.figure()
plt.bar(range(256), array_hist15Cr4[0])
plt.title("Гистограмма DCr rule 4")



plt.show()

