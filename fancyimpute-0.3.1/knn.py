fh = open("data-3.txt", "r+")
f = open("knn-data-3.txt", "w+")

table = []
for line in fh:
    line = line.rstrip('\n').split()
    table.append(line)

from fancyimpute import KNN
filled = KNN(k=3).complete(table)

for row in filled:
    for data in row:
        f.write('%s '%data)
    f.writelines('\n')
f.close()
