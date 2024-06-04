# ----------------------------------------------------Python Chapter 33-37-------------------------------------------------------


print(f'{65*'-'}Python CH.6 (33-37){65*'-'}')
print(149*'-')


print(f'''




{149*'-'}''')
print('--------------------------------------------------------------XXXIII. Nested List (33)---------------------------------------------------------------')
print(149*'-')

# 1. Nested LIST
print('1. Membuat Nested LIST (LIST dalam LIST)')
zerop        = [12,36,60,'X']
firstp       = [21,35,'Y',49]

cpoint       = [zerop,firstp]  
print(f'    I.  Kombinasi LIST ZEROP dan FIRSTP (CPOINT) = {cpoint}')

# IMPLEMENTASI Nested LIST
print('   II.  Implementasi NESTED LIST')

employee_a   = ['Zaki',22,'Pria']
employee_b   = ['Reina',21,'Wanita']
employee_c   = ['Kisaki',23,'Wanita']
employee_d   = ['Yan',23,'Pria']

employeed    = [employee_a,employee_b,employee_c,employee_d ]

for employee in employeed :
    print(f'       {26*'-'}')
    print(f'        Nama Karyawan   : {employee[0]}')
    print(f'        Umur Karyawan   : {employee[1]}')
    print(f'        Status Karyawan : {employee[2]}')
    print(f'       {26*'-'}')

print(149*'-')

print(f'''




{149*'-'}''')
print('------------------------------------------------------------XXXIV. COPY Nested List (34)-------------------------------------------------------------')
print(149*'-')


# 1. Mengambil DATA (Indexing) variabel tertentu dalam Nested LIST
print('1. Mengambil DATA (Indexing) variabel tertentu dalam Nested LIST')
va0          = [True,False]
va1          = ['Aka','Ao']
vax          = [va0,va1]

print(f'    I. Nested list dari VA0 dan VA1 = {vax}')
pick1        = vax[0][1]                    # Jika Benar dan berwarna Biru
pick2        = vax[1][0]                    # Jika Salah dan berwarna Merah

print(149*'-')

print(f'   II. Samudra tidak selalu luas    = {pick1}')
print(f'  III. Api umumnya berwarna         = {pick2}')

# Saat menggunakan .copy maka adress pada LIST copied akan berbeda dengan adress aslinya
# Namun adress pada tiap variabel yang di copy akan tetap sama
# Sehingga saat nilai variabel pada salah satu LIST dirubah, akan merubah nilai variabel LIST lainya

print(149*'-')

# 2. Metode DEEP COPY pada Nested LIST
print('2. Metode DEEPCOPY untuk Nested LIST')

from copy import deepcopy
hpnc = [122, 180, 300, 'Sturmtiger', 'Alpha SU 220']
hpnd = ['IS 9', 'Schwerer Gustav', 800, 1100]

hpdb = [hpnc,1001001,hpnd]
hpdd = hpdb.copy()
hpdc = deepcopy(hpdb)

print(f'       Adress dari data HPNC (ORI)      = {hex(id(hpdb))}')
print(f'       Adress dari data HPDC (DEEPCOPY) = {hex(id(hpdc))}')

print(149*'-')

# Mengetahui Adress variabel Nested LIST yang telah di DEEPCOPY

print(f'   IV. Adress dari variabel 3 Nested LIST HPNC (ORI)      = {hex(id(hpdb[0]))}')
print(f'    V. Adress dari variabel 3 Nested LIST HPDC (DEEPCOPY) = {hex(id(hpdc[0]))}')

print(149*'-')

# Jika Variabel 1 (HPNC) pada Nested LIST HPDB dirubah

hpdb[0][2] = 'White Panther II'
# Nested LIST [HPNC] variabel [2] dirubah menjadi 'White Panther II'
print(f'{37*'-'}Variabel 2 pada Nested LIST HPDB (HPNC) dirubah menjadi "White Panther II"{38*'-'}')
print(149*'-')

print(f'    VI. Data pada Nested LIST HPDB menjadi                      = \n{hpdb}')
print(149*'-')
print(f'   VII. Data pada Nested LIST HPDB setelah di COPY menjadi      = \n{hpdd}')
print(149*'-')
print(f'  VIII. Data pada Nested LIST HPDB setelah di DEEPCOPY menjadi  = \n{hpdc}')
print(149*'-')

# Variabel 2 dari HPNC pada Nested LIST HPDB tidak berubah jika DEEPCOPY


print(f'''




{149*'-'}''')
print('-------------------------------------------------------XXXV. Looping LIST dan ENUMERATE (35)--------------------------------------------------------')
print(149*'-')

# 1. Looping LIST menggunakan FOR LOOP
print('1. Looping LIST menggunakan FOR LOOP')
print(36*'-')

idcode = [23441,53774,78112,11562,10788]
for x in idcode :
    print(f'    Nomor ID = {x}')

print(149*'-')

umury  = [23,31,21,23,24]
for y in umury :
    print(f'    Umur     = {y}')


print(149*'-')


# 2. Looping LIST menggunakan FOR LOOP dan RANGE
print('2. Looping LIST menggunakan FOR LOOP dan RANGE')
print(46*'-')

hpnum = [22,33,44,55,66,77,88]
lword = len(hpnum)

for i in range(lword) :
    print(f'    Numbers  = {hpnum[i]}')


print(149*'-')


# 3. Looping LIST menggunakan WHILE
print('3. Looping LIST menggunakan WHILE')
print(33*'-')

numbero = [72,88,10,122,130,152,188,220]
lspeech = len(numbero)

i = 0

while i < lspeech :
    print(f'    Kaliber Meriam = {numbero[i]}mm ')
    i += 1


print(149*'-')


# 4. Looping menggunakan LIST COMPREHENSION 
print('4. Looping menggunakan LIST COMPREHENSION ')
print(41*'-')

hpdua = [0,'Two',True,'Third',25.5]
[print(f'    Variabel list HPDUA = {i}') for i in hpdua] 


print(149*'-')


# 5. Looping LIST menggunakan ENUMERATE
print('5. Looping LIST menggunakan ENUMERATE ')
print(37*'-')

raghunt = [12.11,22.55,35.5]
for index, z in enumerate(raghunt) :
    print(f'   Indeks data = {index}, Variabel = {z}')

    




print(f'''




{149*'-'}''')
print('-------------------------------------------------------XXXVI. Latihan LIST (36)--------------------------------------------------------')
print(149*'-')


# 1. Membuat daftar BUKU
print('1. Membuat Daftar BUKU')

booklist = []
while True :
    print(f'   {40*'-'}')
    print('   Input Data Buku!')
    title  = input('   Judul Buku    : ')
    writer = input('   Penulis       : ')
    print(f'   {40*'-'}')

    books  = [f'\t\t\t\t{title}\t\t\t\t|\t\t\t\t{writer}']
    
    booklist.append(books)

    print('   No.\t\t|\t\t\t\t   Judul   \t\t\t\t|\t\t\t\tPenulis')
    for index, book in enumerate(booklist) :
        print(f'   {147*'-'}')
        print(f'   {index+1}\t\t|{book[0]}\t\t')
    





booklist = []
while True :
    print(f'   {40*'-'}')
    print('   \nInput Data Buku!')
    title  = input('    I.   Judul Buku    : ')
    writer = input('    II.  Penulis       : ')
    rate   = input('    III. Rating        : ')
    print(f'   {40*'-'}')

    books  = [f'\t\t\t{title}\t\t\t|\t\t\t{writer}\t\t\t|\t\t{rate}\t\t|']
    
    booklist.append(books)

    print(f'   \nNo.\t\t|\t\t\tJudul\t\t\t\t|\t\t\t\tPenulis\t\t\t\t|\t\tRating\t\t|')
    for index, book in enumerate(booklist) :
        print(f'   {164*'-'}')
        print(f'   {index+1}\t\t|{book[0]}\t\t')


    print(f'''
    {145*'-'}''')
    keeps = input('    Lanjutkan Daftar LIST? (Yes/No) : ')
    if keeps == 'No' :
        break

print(f'''
    {145*'-'}''')
print(f'{70*'-'} Akhir dari Program {70*'-'}')






print(f'''




{149*'-'}''')
print('-------------------------------------------------------XXXVII. Tuples dan Set (37)--------------------------------------------------------')
print(149*'-')

# 1. List Normal pada Umumnya 
print('1. List Normal pada Umumnya ')
xlist = [12, 'Yan', True]
print(f'    {xlist}')

print(149*'-')

# 2. List Tuples (menggunakan kurung umum)
print('2. List Tuples (menggunakan kurung umum)')
ylist = (12, 'Yan', True)
print(f'    {ylist}')

print(149*'-')

# DATA TUPLES TIDAK SUPPORT ASSIGNMENT VARIABEL (Assignment hanya berlaku pada tipe Data Umum)
# DATA TUPLES digunakan agar Variabel list tidak dapat dirubah

# 3. List Sets digunakan untuk 
print('3. List Sets (tidak ada indeks')
zlist = {12, 'Yan', True}
print(f'    {zlist}')

# Data Sets seringkali digunakan dalam statistika
