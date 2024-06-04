# ----------------------------------------------------Python Chapter 53-57-------------------------------------------------------


print(f'''




{149*'-'}''')
print('---------------------------------------------------------5[III] Global dan Local Scope (53)----------------------------------------------------------')
print(149*'-')

# Global dalam python merupakan variabel dari sebuah objek yang dapat di callout dalam banyak cara
# nama = 'Budi'  ---> Budi merupakan variabel yang dapat di callout dengan berbagai metode seperti
# If, Else, Elif, For Loop, Fungsi, dan lainya
# sedangkan Local scope tidak dapat diakses langsung pada Fungsi

nama = 'Budi'

# Global dalam IF
if nama == 'Budi' :
    print(f'{73*'-'}{nama}{73*'-'}')

# Global dalam ELSE
if nama == 'Yan' :
    print('Namaku Yan')
else :
    print(f'{73*'-'}{nama}{73*'-'}')
print(149*'-')

# Global dalam Fungsi
def funz() :
    print(f'{73*'-'}{nama}{73*'-'}')
print(f'{73*'-'}{funz()}{73*'-'}')
print(149*'-')

# 1. manipulasi vaariabel local menjadi global
print(f'1. manipulasi vaariabel local menjadi global')

taskid = 'Yan von Einzbern'

def exc(alphav) :
    taskid = alphav #taskid tidak dapat dimodifikasi karena merupakan local variabel

print(f'   > Variabel seharusnya         = {taskid}')
exc('Yan van Ainsworth')
print(f'   > Variabel setelah modifikasi = {taskid}')
print(149*'-')



# Menggunakan sintaks global akan mengonversi local variabel menjadi global variabel
def exd(omegav) :
    global taskid
    taskid = omegav

print(f'   > Variabel seharusnya         = {taskid}')
exd('Yan van Ainsworth')
print(f'   > Variabel setelah modifikasi = {taskid}')
print(149*'-')

# Variabel Global dapat diakses dengan mudah
# Variabel Local perlu dikonversi terlebih dahulu





print(f'''




{149*'-'}''')
print('---------------------------------------------------------5[IV] Import Statement (54)----------------------------------------------------------')
print(149*'-')

# Import dapat digunakan untuk summon program eksternal dari file berbeda

# 1. Digunakan untuk summon seluruh sintaks yang ada pada file
import Example_54

print(149*'-')

# 2. Digunakan untuk summon objek yang ada pada file
print(Example_54.title)

# 3. Assign Fungsi 
class54 = Example_54.min(18, 7)
print(f'2. CLASS54 setelah Assign number = {class54}')

print(149*'-')





print(f'''




{149*'-'}''')
print('---------------------------------------------------------5[V] Module (55)----------------------------------------------------------')
print(149*'-')

import Example_55

assign55 = Example_55.pangkat(2, 4)
print(f'1. Jika bilangan 3 dipangkatkan dengan fungsi yang ada pada Module Example_55 maka, menjadi = {assign55(3)}')
print(149*'-')

from Example_55 import tambah, kali
assign50 = tambah(7,9)
print(f'2. Jika bilangan 5 ditambah dengan fungsi tambah pada Module Example_55 maka, menjadi       = {assign50(5)}')
print(149*'-')

assign55 = kali(3, 8)
print(f'3. Jika bilangan 8 dikali dengan fungsi kali pada Module Example_55 maka, menjadi           = {assign55(8)}')
print(149*'-')

# Dapat import semua source dalam file melalui sintaks :
# from data import *

# Dapat rename source yang ada pada file dengan penulisan :
# from Example_55 import kali as fx_k

# Maka fx_k akan menjadi dan bernilai sama dengan kali
# assign0 = fx_k(5, 12)





print(f'''




{149*'-'}''')
print('---------------------------------------------------------5[VI] Package Sederhana (56)----------------------------------------------------------')
print(149*'-')

import Math.matematika
from Physic.Physics import gaya

sniff = Math.matematika.sep(2,4,1,2,1)
print(f'1. Jika sniff ditranslasikan dengan sep maka menjadi                                   = {sniff}')
print(149*'-')

snuff = Math.matematika.sap(2, 4)
print(f'2. Jika snuff ditranslasikan dengan sap maka menjadi                                   = {snuff}')
print(149*'-')

snaff = gaya(30, 5)
print(f'3. Jika Massa benda 30kg dihadapkan objek dengan ruas 30m, maka terccipta gaya sebesar = {snaff} joule')
print(149*'-')





print(f'''




{138*'-'}''')
print('------------------------------------------------------5[VII] Init pada Package (57)-------------------------------------------------------')
print(138*'-')

import Package57 # import llingkaran, lbalok

print(138*'-')

lluas = Package57.llingkaran.klingkaran(3.14, 14, 14)
print(f'3. Jadi Luas lingkaran tersebut adalah = {lluas} cm')
print(138*'-')

bluas = Package57.lbalok.luas(13, 13, 13)
print(f'4. Jadi Luas balok tersebut adalah     = {bluas} cm')
print(138*'-')

