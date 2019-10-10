print ("\n1.feladat: Beolvasni az sms.txt-t data változóba, soronként")
file = open("sms.txt","r")
data = []
for lines in file:
    data.append(lines.rstrip())
print ("\n2.feladat: Írd ki a legutolsó üzenet szövegét: ")
print (data[-1])
print("\n3.feladat: Kiíratni a leghosszabb és legrövidebb üzenetet")
sms_count = int(len(data)/2)
sms_msg=[]
sms_length=[]
for i in range(1,sms_count+1):
    sms_msg.append(data[i*2])
    sms_length.append(len(data[i*2]))

sms_min_index = sms_length.index(min(sms_length))
sms_max_index = sms_length.index(max(sms_length))
print ("\nA leghosszabb üzenet:")
print(data[sms_max_index*2+1])
print(data[(sms_max_index+1)*2])
print ("\nA legrövidebb üzenet:")
print(data[sms_min_index*2+1])
print(data[(sms_min_index+1)*2])
"""
print ("\n4.feladat: Statisztika. Üzenet hossza szerint 1-20,21-40, 41-60,61-80, 81-100, mellé kerüljön az üzenet hossza.")
counter = [0,0,0,0,0]
for i in range(len(sms_msg)):
    if((len(sms_msg[i])>0)and(len(sms_msg[i])<21)):
        counter[0]+=1
    elif((len(sms_msg[i])>21)and(len(sms_msg[i])<41)):
        counter[1]+=1
    elif((len(sms_msg[i])>41)and(len(sms_msg[i])<61)):
        counter[2]+=1
    elif((len(sms_msg[i])>61)and(len(sms_msg[i])<81)):
        counter[3]+=1
    elif((len(sms_msg[i])>81)and(len(sms_msg[i])<101)):
        counter[4]+=1
print ("\n1-20:",counter[0],"\n20-40:",counter[1],"\n41-60:",counter[2],"\n61-80:",counter[3],"\n81-100:",counter[4])
print("\n5.feladat: elég zavaros, minden óra 0. percében olvas, majd töröl, 1-24 óra közt")
print ("órakor olvasott üzenetek száma:","nem olvasott:")
data = data[1:]
where_is = [0,0,0,0]
for i in range(0,len(data),2):
    if (data[i][0:2].rstrip()=="9"):
        where_is[0]+=1
    elif (data[i][0:2].rstrip()=="10"):
        where_is[1]+=1
    elif(data[i][0:2].rstrip()=="11"):
        where_is[2]+=1
    elif(data[i][0:2].rstrip()=="12"):
        where_is[3]+=1
print("\n10-kor elolvasott:",where_is[0],"\n11kor elolvasott:",where_is[1], "\n12kor elolvasott:",where_is[2],"\n13kor elolvasott:",where_is[3])
print ("\n6.feladat:Ernő barátnője")
print("Mennyi idő telik el két üzenet közt?")
eltelt = []
for i in range(0,len(data),2):
    if(data[i][-9:]=='123456789'):
        eltelt.append(data[i][0:5].rstrip())
for i in range(len(eltelt)):
    eltelt[i]=eltelt[i].split()
kulonbseg = []
for j in range(1,len(eltelt)):
    ora=int(eltelt[j][0])-int(eltelt[j-1][0])
    perc=int(eltelt[j][1])-int(eltelt[j-1][1])
    eredmeny = [ora,perc]
    kulonbseg.append(eredmeny)
print ("Legtöbb eltelt idő két sms közt:",max(kulonbseg)[0], "óra",max(kulonbseg)[1],"perc")
print("\n7.feladat:Olvass be egy bejövő üzenetet")
import datetime
actual_sms = datetime.datetime.now()
hour_and_minute = str(actual_sms.hour)+" "+str(actual_sms.minute)
new_message = hour_and_minute
number=""
while (len(number)<9):
    number = input("add meg a számot, 9 szjegy: ")
new_message = new_message+" "+ str(number)
sms_new = input("kérem az üzenetet:")
new_message = new_message+" "+str(sms_new)
print(new_message)
"""
print ("\n8.feladat: smski.txt-be kiírni, telefonszám szerint növekvő sorrendben, alatt idő-üzenet")
data = data[1:]
hossz = int(len(data)/2)
to_work = []
for i in range(0,hossz,2):
    x = data[i].split(" ")
    x.append(data[i+1])
    to_work.append(x)
def getkey(item):
    return item[2]
result=sorted(to_work, key=getkey)
new_file = open("smski.txt","a")

for i in range(len(result)):
    new_file.write(result[i][2])
    second_line = "\n"+str(result[i][0])+":"+result[i][1]+" "+str(result[i][3])+"\n"
    new_file.write(second_line)
new_file.close()
