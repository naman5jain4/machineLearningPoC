from fancyimpute import IterativeSVD
f1 = open("data-1.txt", "r+")
f2 = open("data-2.txt", "r+")
f3 = open("data-3.txt", "r+")
fh1 = open("svd-data-1.txt", "w+")
fh2 = open("svd-data-2.txt", "w+")
fh3 = open("svd-data-3.txt", "w+")

table = []
for line in f1:
    line = line.rstrip('\n').split()
    table.append(line)

filled = IterativeSVD().complete(table)

for row in filled:
    for data in row:
        fh1.write('%s ' %data)
    fh1.writelines('\n')
fh1.close()
del table[:]

table = []
for line in f2:
    line = line.rstrip('\n').split()
    table.append(line)

filled2 = IterativeSVD().complete(table)

for row in filled2:
    for data in row:
        fh2.write('%s ' %data)
    fh2.writelines('\n')
fh2.close()
del table[:]

table = []
for line in f3:
    line = line.rstrip('\n').split()
    table.append(line)

filled3 = IterativeSVD().complete(table)

for row in filled3:
    for data in row:
        fh3.write('%s ' %data)
    fh3.writelines('\n')
fh3.close()
del table[:]

