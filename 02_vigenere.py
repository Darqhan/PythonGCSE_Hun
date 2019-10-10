def inputString(minChar, maxChar):
    ### min-max érték közt bekér egy szöveget, space nélkülm majd normalizálja
    sentence =""
    while ((len(sentence)==minChar)or(len(sentence)>maxChar)):
        sentence = input("kérlek írj egy "+ str(minChar)+"-"+str(maxChar)+" karakter szöveget:")
        sentence=sentence.replace(" ","")
        #a lenti sor veszi ki az összes nem alfabetikus elemet
        sentence=''.join(x for x in sentence if x.isalpha())
    sentence = normalizeString(sentence)
    return sentence

def normalizeString(x):
    ### eltünteti az áéíöüóőúűé karakterek ékezetés és angol latin-1 lesz
    import unicodedata
    normalized = unicodedata.normalize('NFKD', x).encode('latin-1','ignore').decode("latin-1")
    normalized=normalized.upper()
    return normalized

def Mantissa(sentence, keyword):
    #ezzel készítem el a kódsort, amennyi a lefordítani való mondat, annyiszor illesztem be a kódszót
    multipleMe = int(len(sentence)/len(keyword))
    addFurtherMoreMe = len(sentence)%len(keyword)
    LeftOver = keyword [0:addFurtherMoreMe]
    return (multipleMe*keyword + LeftOver)

def convertFileIntoArray():
    #ez nyitja a file-t és írja ki listába a sorokat
    file = open ("vtabla.dat")
    table=[]
    for items in file:
        table.append(items.rstrip())
    return table
def writeIntoFile(filename, xstring):
    file = open(filename, "a")
    file.write(xstring)
    file.close
    
#Első feladat: bekérünk 1-255 karakter hosszú szöveget. 
#Második feladat: szöveg átalakítása:
    ## magyar ékezet helyett sima karakter
    ## csak angol abc szerepelhet
    ## csupa nagybetűs szöveg
#hihibás a feladat : simán írhatok be számot, illetve más unicode-dal nem foglalkozik
#harmadik feladat: írja ki a szöveget
openSentence = inputString(0,255)
print("ezt a szöveget kódold, oszlop: ",openSentence)
#Most kulcsszót kérünk be 1-5 karakter, nagybetűs
    
keyWord = inputString(0,5)
#print(keyWord)
#Ötödik feladat: Kódolás első lépése. Annyiszor ismételjük a kódszót, amennyi az üzenet hossza.
#Példa: kódszó = abcde mondat = Acreelesett 5 vs 11 karakter: fűzés = abcdeabcdea

#ismét rossz a feladat: nem kéri a space eltüntetését a nyílt szövegből

keyWordMantissa = Mantissa(openSentence, keyWord)
print("ez a kulcsszó átalakítva, sor: ", keyWordMantissa)

#beolvasni a táblázatot, szöveg első karakter = első sor, mantissa első karakter = első oszlop
# a metszésponton lévő karakter lesz a mienk
# kapott kódolt szöveget kiírni a képernyőre, és a fájlba kodolt.dat

vigenere_code=convertFileIntoArray()

startLetters = ""
for i in range(len(vigenere_code)):
    startLetters+=vigenere_code[i][0]

result = ""
for i in range(len(openSentence)): 
    #kulcsszöveg (mantissa)> első sorban keresse meg hogy melyik értéken van 
    First = vigenere_code[0].find(openSentence[i]) 
    #openSentence első karaktere első oszlopban
    Second = startLetters.find(keyWordMantissa[i])
    result+=(vigenere_code[Second][First])
print ("én eredményem:    ", result)
print ("ez kellene legyen:","ETTDRIUOSTHJEATAINDCDIEINE")
#!HIBA: felkiáltójelet nem szedi ki a program
#!HIBA: ha a kulcsszó hosszabb, mint  aszöveg, akkor rosszul fut le
writeIntoFile("kodolt.dat", result)
