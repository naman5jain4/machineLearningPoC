f1 = open("data-1.txt", "r+")
f2 = open("data-2.txt", "r+")
f3 = open("data-3.txt", "r+")

fm1 = open("mean-data-1.txt", "w+")
fm2 = open("mean-data-2.txt", "w+")
fm3 = open("mean-data-3.txt", "w+")

table = []

#appending data to a 2D array table
for line in f1:
    line = line.rstrip('\n').split()
    table.append(line) 
del table[-1]

#average the attribute
def ave(table, i):
    r = 0
    sum = 0
    for row in table:
        if table[r][i] == 'NaN':
            r+=1
            continue 
        sum+= float(table[r][i])
        r+=1
    r = 0
    average = sum/len(table)
    for row in table:
        if table[r][i] =='NaN':
            table[r][i] = average
        r+=1

#filling "NaN" with attribute average value
for row in table:
    i = 0
    for col in row:
	if col == 'NaN':
	    ave(table, i)
	    break
	i+=1
	
#writting svm to a file
for row in table:
    for data in row:
	    fm1.write('%s '%(data)),
    fm1.writelines('\n')
fm1.close()
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
	    ave(table, i)
	    break
	i+=1
	
#writting svm to a file
for row in table:
    for data in row:
	    fm2.write('%s '%(data)),
    fm2.writelines('\n')
fm2.close()
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
	    ave(table, i)
	    break
	i+=1
	
#writting svm to a file
for row in table:
    for data in row:
	    fm3.write('%s '%(data)),
    fm3.writelines('\n')
fm3.close()
del table[:]
