f1 = open("missing-data-1.txt", "r+")
f2 = open("missing-data-2.txt", "r+")
f3 = open("missing-data-3.txt", "r+")
fh1 = open("data-1.txt", "w+")
fh2 = open("data-2.txt", "w+")
fh3 = open("data-3.txt", "w+")

table = []

for line in f1:
    line = line.rstrip('\n').split()
    table.append(line)
del table[-1]

i=0
for row in table:
    j=0
    for data in row:
        if float(data)==1.00000000000000e+99:
            table[i][j]='NaN'
        j+=1
    i+=1

for row in table:
    for data in row:
        fh1.write('%s ' %data)
    fh1.writelines('\n')
fh1.close()
del table[:]


table = []

for line in f2:
    line = line.rstrip('\n').split()
    table.append(line)
del table[-1]

i=0
for row in table:
    j=0
    for data in row:
        if float(data)==1.00000000000000e+99:
            table[i][j]='NaN'
        j+=1
    i+=1

for row in table:
    for data in row:
        fh2.write('%s ' %data)
    fh2.writelines('\n')
fh2.close()
del table[:]


table = []

for line in f3:
    line = line.rstrip('\n').split()
    table.append(line)
del table[-1]

i=0
for row in table:
    j=0
    for data in row:
        if float(data)==1.00000000000000e+99:
            table[i][j]='NaN'
        j+=1
    i+=1

for row in table:
    for data in row:
        fh3.write('%s ' %data)
    fh3.writelines('\n')
fh3.close()
del table[:]
