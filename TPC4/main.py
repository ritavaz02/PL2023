import sys
import re
import json

# sys.argv[1] is the path to the csv file     
n=0
myDict = {}
columns = []
agreg = ""

# gets the first line as argument and creates the dicitonary
def index(line):
    count = 0
    index = re.split(r',(?=[A-Z])', line)
    for item in index:
        if line.strip() != '':
            # match {minNumber,maxNumber}
            nm = re.search('(.+)\{(\d+),(\d+)\}',item)
            # match {maxNumber}
            m = re.search('(.+)\{(\d+)\}',item)
            # match ::(sum|media)
            agr = re.search('::(.+)',item)
            if nm:
                col = nm.group(1)
                minC = nm.group(2)
                columns.append(int(nm.group(3)))
            elif m:
                col = m.group(1)
                columns.append(int(m.group(2)))
            else:
                col = item
                columns.append(1)
            if agr:
                agreg = agr.group(1)
                name = col + '_' + re.split(r',',agreg)[0]
            else: name = col
            
            # update the dictionary
            new = {name: []}
            myDict.update(new)
            count+=1

# for each line, fill the dictionary with the values
def parseLines(line):
    items = re.split(r',', line)
    count = 0
    i = 0
    for name in myDict.keys():
        if(re.search(r'sum', name)):
            j=0
            sumC = 0
            while(j<columns[count]):
                if items[i].strip() != '':
                    sumC += int(items[i])
                i+=1
                j+=1
            myDict[name].append(sumC)
        elif(re.search(r'media', name)):
            j=0
            sumC = 0
            m = 0
            while(j<columns[count]):
                if items[i].strip() != '':
                    sumC += int(items[i])
                    m += 1
                i+=1
                j+=1
            myDict[name].append(sumC/m)
        else:
            if(columns[count]==1):
                if items[i].strip() != '':
                    myDict[name].append(items[i])
                i+=1
            else:
                j=0
                new = []
                while(j<columns[count]):
                    if items[i].strip() != '':
                        new.append(int(items[i]))
                    i+=1
                    j+=1
                myDict[name].append(new)
        count+=1

# open file csv
with open(sys.argv[1],'r') as f:
    # read first line to know the types
    for line in f:
        line = line.rstrip('\n')
        if n == 0:
            index(line)
        else:
            parseLines(line)
        n += 1
    

    # creates the sctruture json
    i = 0
    final = []
    while i < n-1:
        final.append({})
        for name in myDict:
            final[i][name] = myDict[name][i]
        i+=1

    name = sys.argv[1].split('.')[0]

    # write in the json file
    with open(name + '.json', 'w') as f:
        f.write(json.dumps(final, indent=4, ensure_ascii=False))


