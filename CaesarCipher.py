# DEKRIPSI MENGGUNAKAN Substitusi Caesar CIPHER
# JULIO ANDYAN JORDAN ARYANTO (24060117130078)
from array import *
from nltk import *

#CATATAN :
# Dekripsi dilakukan dengan menggunakan subtitusi caesar cipher dengan 3 huruf ke kanan


#MULAI
# inisialisasi
# Fungsi dekripsi Subtitusi Caesar Cipher   
def SDekripsi(Kar):
    if Kar == 'D' :
        return 'A'
    elif Kar =='E':
        return 'B'
    elif Kar =='F':
        return 'C'
    elif Kar =='G':
        return 'D'
    elif Kar =='H':
        return 'E'
    elif Kar =='I':
        return 'F'
    elif Kar =='J':
        return 'G'
    elif Kar =='K':
        return 'H'
    elif Kar =='L':
        return 'I'
    elif Kar =='M':
        return 'J'
    elif Kar =='N':
        return 'K'
    elif Kar =='O':
        return 'L'
    elif Kar =='P':
        return 'M'
    elif Kar =='Q':
        return 'N'
    elif Kar =='R':
        return 'O'
    elif Kar =='S':
        return 'P'
    elif Kar =='T':
        return 'Q'
    elif Kar =='U':
        return 'R'
    elif Kar =='V':
        return 'S'
    elif Kar =='W':
        return 'T'
    elif Kar =='X':
        return 'U'
    elif Kar =='Y':
        return 'V'
    elif Kar =='Z':
        return 'W'
    elif Kar =='A':
        return 'X'
    elif Kar =='B':
        return 'Y'
    elif Kar =='C':
        return 'Z'
    else :
        return ''

#List untuk Hasil Dekripsi
Pteks = []

#realisasi
teks = input("masukan cipher teks : ")
#mengubah semua inputan teks menjadi kapital
Cteks = teks.upper()
#menghilangkan spasi di Cteks
Ateks = []
for j in range(len(Cteks)):
    if Cteks[j] != ' ' :
        Ateks.append(Cteks[j])
print(Ateks)


#mulai proses dekripsi
for i in range(len(Ateks)):
    Pteks.append(SDekripsi(Ateks[i]))
print ("Plainteks yang didapatkan dari dekripsi Caesar Cipher adalah ="+" ".join(Pteks))

