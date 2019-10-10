print ("\n1.feladat: Beolvasni a meccs.txt")

file = open ("meccs.txt","r")
data = []
for lines in file:
    working_var = lines.split()
    data.append(working_var)        
"""
print ('\n2.feladat: Bekérni egy forduló számot, és kiadni a meccseket')
print ("\nformátum: csoport-csoport: x-x(x-x)")
input_data="a"
while (input_data not in "1234567891011121314151617181920"):
    input_data = input("add meg a forduló számát:")
for i in range(1,len(data)):
    if (data[i][0] == input_data):
        print (data[i][5],"-",data[i][6],": ", data[i][1],"-",data[i][2],"(",data[i][3],"-",data[i][4],")")

print("\n3. feladat: Mely csapatok fordítottak a félidő után?")
"""
"""
data[i][3-4]:félidő, data[i][1-2]:eredmény
első félidőben vesztésre állt
második félidőben győzött
"""
"""
for i in range(1,len(data)):
    if ((int(data[i][3])>int(data[i][4]))and(int(data[i][1])<int(data[i][2]))):
        print ("A vesztesből lett győztes csapat:",data[i][0],".fordulóban:",data[i][6])
    elif (int(data[i][3])<int(data[i][4]))and(int(data[i][1])>int(data[i][2])):
        print ("A vesztesből lett győztes csapat:",data[i][0],".fordulóban:",data[i][5])
print ("\n4.feladat: Kérj be egy csapatnevet(Lelkesek)")
print ("Írasd ki, hogy a csapat mennyi gólt lőtt, és mennyit kapott")
"""
"""
team_to_check=""
while (len(team_to_check)<1):
    team_to_check = input("adj meg egy csapatnevet (pl.:Lelkesek):")
"""
"""
szerzett, kapott = 0,0
team_to_check = "Lelkesek"
for i in range(1,len(data)):
    if (data[i][5]==team_to_check): 
            szerzett+= int(data[i][1])
            kapott += int(data[i][2])
            print(data[i])
    elif(data[i][6]==team_to_check):
        szerzett +=int(data[i][2])
        kapott += int(data[i][1])
        print (data[i])
""" 
print ("\nMelyik csapat maradt otthon veretlen, , vagy melyik fordulóban kapott ki először")
hazai_csapat = [data[1][5]]
for i in (range(1,len(data))):
    if (data[i][5] not in hazai_csapat):
        hazai_csapat.append(data[i][5])
talalat = []
megvertek = []
for i in range(len(hazai_csapat)):
    for j in range(1,len(data)):
        if ((hazai_csapat[i] == data[j][5])and(int(data[j][1])<int(data[j][2]))):
                bang = ("vesztes:"+ data[j][0]+".fordulóban "+data[j][5])
                talalat.append (bang)
                bong = data[j][5]
                megvertek.append(bong)
                print(bang)
                break
for i in range(len(hazai_csapat)):
    if (hazai_csapat[i] not in megvertek):
        print ("A csapat otthon veretlen maaradt: ",hazai_csapat[i])
print ("\n7.feladat: Statisztika")
print ("mennyi hasonló eredmény született: 0-0:12, 1-0:11, stb")
counter = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
for i in range(1,len(data)):
    if ((data[i][1]=="0") and (data[i][2]=="0")):
        counter[0]+=1
    elif ((data[i][1]=="0") and (data[i][2]=="1"))or((data[i][1]=="1") and (data[i][2]=="0")):
        counter[1]+=1
    elif (data[i][1]=="1") and (data[i][2]=="1"):
        counter[2]+=1
    elif ((data[i][1]=="2") and (data[i][2]=="1"))or((data[i][1]=="1") and (data[i][2]=="2")):
        counter[3]+=1
    elif ((data[i][1]=="0") and (data[i][2]=="2"))or((data[i][1]=="2") and (data[i][2]=="0")):
        counter[4]+=1
    elif ((data[i][1]=="2") and (data[i][2]=="2")):
        counter[5]+=1
    elif ((data[i][1]=="0") and (data[i][2]=="3"))or((data[i][1]=="3") and (data[i][2]=="0")):
        counter[6]+=1
    elif ((data[i][1]=="1") and (data[i][2]=="3"))or((data[i][1]=="3") and (data[i][2]=="1")):
        counter[7]+=1
    elif ((data[i][1]=="2") and (data[i][2]=="3"))or((data[i][1]=="3") and (data[i][2]=="2")):
        counter[8]+=1
    elif ((data[i][1]=="3") and (data[i][2]=="3")):
        counter[9]+=1
    elif ((data[i][1]=="0") and (data[i][2]=="4"))or((data[i][1]=="4") and (data[i][2]=="0")):
        counter[10]+=1
    elif ((data[i][1]=="1") and (data[i][2]=="4"))or((data[i][1]=="4") and (data[i][2]=="1")):
        counter[11]+=1
    elif ((data[i][1]=="2") and (data[i][2]=="4"))or((data[i][1]=="4") and (data[i][2]=="2")):
        counter[12]+=1
    elif ((data[i][1]=="3") and (data[i][2]=="4"))or((data[i][1]=="4") and (data[i][2]=="3")):
        counter[13]+=1
    elif ((data[i][1]=="4") and (data[i][2]=="4")):
        counter[14]+=1
print ("0:0=", counter[0],"\n1:0=", counter[1],"\n1:1=",counter[2])
print ("2:0=",counter[4],"\n2:1=",counter[3],"\n2:2=",counter[5])
print ("3:0=",counter[6],"\n3:1=",counter[7],"\n3:2=",counter[8],"\n3:3=",counter[9])
print ("4:0=",counter[10],"\n4:1=",counter[11],"\n4:2=",counter[12],"\n4:3=",counter[13],"\n4:4=",counter[14])



