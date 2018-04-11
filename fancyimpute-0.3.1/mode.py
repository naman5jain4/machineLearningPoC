import sys
fh = open("data-3.txt", "r+")
f = open("mode-data-3.txt", "w+")

table = []

#appending data to a 2D array table
for line in fh:
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
	    f.write('%s '%(data)),
    f.writelines('\n')
f.close()
