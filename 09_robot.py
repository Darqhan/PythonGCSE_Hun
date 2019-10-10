print ("\n1.feladat: olvassuk be az adatokat.")
file = open("program.txt","r")
data=[]
for lines in file:
    data.append(lines.strip("\n"))
data = data[1:]
print("\n4.feladat. Egyszerűsítés: working_data tartalmazza")

def count_in_array(proba):
    '''
    Az első funkció a harmadik feladathoz
    először minden betűt megszámol, és [2,"E"] formában listáz,
    de ez csak string-sorozatonként teszi
    példa: 
    count_in_array("AABCD")
    [[2, 'A'], [1, 'B'], [1, 'C'], [1, 'D']]
    '''
    actual = proba[0]
    counter = 0
    data_new = []
    for item in proba:
        if(actual==item):
            counter+=1
        else:
            data_new.append([counter, actual])
            counter=1
            actual = item
    data_new.append([counter, actual])
    return data_new

def all (data):
    '''
    A count_in_array funkciót hívja meg, hogy [2,"E"] formában kapjuk meg
    az "EEE"-t
    Illetve, hogy a EGÉSZ listát elemenként szétszedhessük
    példa:
    all(["AAB","BCC"])
    [[[2, 'A'], [1, 'B']], [[1, 'B'], [2, 'C']]]
    '''
    data_newest = []
    for i in range(len(data)):
        data_newest.append(count_in_array(data[i]))
    return data_newest 

def array_to_string(data):
    '''
    Az all funkció eredményét tudom itt [[2,"E"],[4,"C"],[1,"N"]] formátumból
    >>> "2E4CN" formába áttenni (lista ezis), az 1-t nem írja
    példa:
    array_to_string([[[2, 'A'], [1, 'B']], [[1, 'B'], [2, 'C']]])
    ['2AB', 'B2C']
    '''
    fresh_data=[]
    fresh=""
    for i in range(len(data)):
        for j in range(len(data[i])):
            if (data[i][j][0]>1): 
                fresh += str(data[i][j][0])+data[i][j][1]
            else:
               fresh += data[i][j][1]  
        fresh_data.append(fresh)
        fresh=""
    return fresh_data

working_data = array_to_string(all(data))
newfile = open("ujprog.txt","a")
for items in working_data:
    newfile.write(items+"\n")
newfile.close()
