f1 = open("data-1.txt", "r+")
f2 = open("data-2.txt", "r+")
f3 = open("data-3.txt", "r+")

fh1 = open("mode-data-1.txt", "w+")
fh2 = open("mode-data-2.txt", "w+")
fh3 = open("mode-data-3.txt", "w+")

table = []

#appending data to a 2D array table
for line in f1:
    line = line.rstrip('\n').split()
    table.append(line) 
del table[-1]

#find mode of attribute
def mode(table, i):
    map={}
    for r, row in enumerate(table):
        if table[r][i]=='NaN':
            continue
        if map.has_key(table[r][i]):
            map[table[r][i]]+=1
            continue
        map[table[r][i]]=1
    max=0
    temp=0
    for key in map:
        if map[key]>max:
            max=map[key]
            temp=key
    for r, row in enumerate(table):
        if table[r][i]=='NaN':
            table[r][i]=temp
 
#filling "NaN" with attribute average value
for row in table:
    i = 0
    for col in row:
	if col == 'NaN':
	    mode(table, i)
	    break
	i+=1
	
#writting svm to a file
for row in table:
    for data in row:
	    fh1.write('%s '%(data)),
    fh1.writelines('\n')
fh1.close()
del table[:]


#appending data to a 2D array table
for line in f2:
    line = line.rstrip('\n').split()
    table.append(line) 
del table[-1]

 
#filling "NaN" with attribute average value
for row in table:
    i = 0
    for col in row:
	if col == 'NaN':
	    mode(table, i)
	    break
	i+=1
	
#writting svm to a file
for row in table:
    for data in row:
	    fh2.write('%s '%(data)),
    fh2.writelines('\n')
fh2.close()
del table[:]

#appending data to a 2D array table
for line in f3:
    line = line.rstrip('\n').split()
    table.append(line) 
del table[-1]

 
#filling "NaN" with attribute average value
for row in table:
    i = 0
    for col in row:
	if col == 'NaN':
	    mode(table, i)
	    break
	i+=1
	
#writting svm to a file
for row in table:
    for data in row:
	    fh3.write('%s '%(data)),
    fh3.writelines('\n')
fh3.close()
del table[:]

