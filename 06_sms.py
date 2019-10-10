'''
print("\n1.feladat: 1 betű bekérése, kód kiírása")
keyboard_read = ""

while (len(keyboard_read)!= 1):
    keyboard_read = input ('adj egy betűt:')

keyboard_read = keyboard_read.lower()
equivalent = ["abc","def","ghi","jkl","mno","pqrs","tuv","wxyz"]
for i in range(len(equivalent)):
    if (keyboard_read in equivalent[i]):
        this_is_it = i+2
print (this_is_it)
'''
'''
print("\n2.feladat: szó bekérése, számsor hozzáadása")
word_in = input ('adj egy szöveget:')

equivalent = ["2abc","3def","4ghi","5jkl","6mno","7pqrs","8tuv","9wxyz"]
my_result=""

for i in range(len(word_in)):
    for j in range(len(equivalent)):
        if (word_in[i] in equivalent[j]):
            my_result += str(j+2)
print (my_result)
'''
'''
print ("\n3.feladat: beolvasni a szavak txt-t")
my_array = []
file = open ("szavak.txt","r")
for lines in file:
    x=lines.replace("\n","")
    my_array.append(x)
file.close()
print("\n4.feladat: megtalálni a leghosszabb szót")
longest = ""
for i in range(len(my_array)):
    if (len(longest) < len(my_array[i])):
        longest = my_array[i]
print ("A leghosszabb szó a: ",longest,", hossza: " ,len(longest))

print ("\n5.feladat: Rövid szavak, vagyis 5 karakter alattiak")
shorts = 0
for i in range(len(my_array)):
    if (len(my_array[i])<6):
        shorts+=1
print ("Rövid szóból: ", shorts, " van.")
'''
print ("\n6.feladat: kodok.txt-ből átírni a szöveget a szavak.txt-be, kód szerint")
file = open ("szavak.txt","r")
target_file = open("kodok.txt","a")
my_array=[]
for lines in file:
    w=lines.replace("\n","")
    my_array.append(w)
target_array = []
equivalent = ["2abc","3def","4ghi","5jkl","6mno","7pqrs","8tuv","9wxyz"]
for i in range(len(my_array)):
    target_array.append("")
    for j in range(len(my_array[i])):
        for k in range(len(equivalent)):
            if (my_array[i][j] in equivalent[k]):
                target_array[i]+=(str(k+2))
'''
for i in range(len(target_array)):
    x = target_array[i]+"\n"
    target_file.write(x) 
target_file.close()
'''
print("\n7.feladat: Bekérni egy számsort, melyik szó tartozik hozzá")
your_code = input("adj egy számsort")
save_code=[]
for i in range(len(target_array)):
    if (your_code in target_array [i]):
        print(target_array[i])
        save_code.append(i)
for i in range(len(save_code)):
    place = save_code[i]
    print (my_array[place])
print ("\n8.feladat: kód:szó, amelyiknél 1kód:sok szó")
kod_sok=[]
for i in range(len(target_array)):
    if (target_array.count(target_array[i])>1):
        kodok = [target_array[i],my_array[i]]
        kod_sok.append(kodok)
print(kod_sok)
print("\n9.feladat: Melyik kodhoz tartozik a legtöbb a szó? Kiíratni az összes szót")
my_count = []
for i in range(len(target_array)):
    my_count.append(target_array.count(target_array [i]))
my_indx=my_count.index(max(my_count))
print (my_count[my_indx]," darab")

where = []
for i in range(len(target_array)):
    if (target_array[my_indx]==target_array[i]):
        where.append(i)
for i in range(len(where)):
    print (my_array[where[i]], target_array[where[i]])
