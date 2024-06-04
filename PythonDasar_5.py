# ----------------------------------------------------Python Chapter 28-32-------------------------------------------------------


bon = 'Bonjoure'
print(f'{bon} you all !')


print(f'''




{80*'-'}''')
print('--------------------------XXVIII. Latihan LOOPING (28)--------------------------')
print(80*'-')

# 1. Menggunakan FOR dan IN
print('1. Membuat segitiga sama kaki melalui metode LOOPING')

lenght = int(input('*  Masukkan panjang segitiga yang diharapkan : '))
numh = 1
for x in range(lenght) :
    print('.'*numh)
    numh += 2

print(f'''
{80*'-'} 
''')

# 2. Menggunakan WHILE dan BREAK
print('2. Membuat segitiga sama kaki melalui metode WHILE')
numa = 1
while True :
    print('+'*numa)
    numa += 2
    if numa > lenght :
        break

print(f'''
{80*'-'} 
''')

# 3. Hanya GANJIL saja menggunakan MODULUS
print('3. Membuat segitiga sama kaki dengan syarat GANJIL menggunakan MODULUS')
print(f'{31*'-'}Fungsi Gabungan Top{31*'-'}')
numb = 1
spasi = int(lenght/2)
while True :
    if (numb%2) :
        # Print jika GANJIL
        print(' '*spasi,'*'*numb)
        spasi -= 1
        numb += 2

    else :
        # Kembali ke atas jika GENAP
        numb += 2
        continue

    if numb > lenght :
        break
        # Akan Stop jika numb melebihi lenght
print(f'{31*'-'}Fungsi gabungan BOT{31*'-'}')
'''

# 4. Mencoba membuat KETUPAT
'''
shape = int(input('*  Masukkan panjang segitiga yang diharapkan : '))

for i in range(1, shape + 1) :
    print(' '*(shape-1) + '*' * (2*i - 1))

for i in range(shape - 1, 0, -1) :
    print(' '*(shape - i) + '*' * (2 * i - 1))

print(f'''




{80*'-'}''')
print('--------------------------------XXIX. List (29)--------------------------------')
print(80*'-')

# 1. LIST untuk data INT
print('1. List untuk DATA INT')
dint = [1, 3, 7, 9,12]
print(dint)
print(f'{52*'-'}')

# 2. LIST untuk data FLOAT
print('2. List untuk DATA FLOAT')
dfloat = [1.18, 3.55, 7.27, 9.41, 12.90]
print(dfloat)
print(f'{52*'-'}')

# 3. LIST untuk data STR
print('3. List untuk DATA STR')
dstr = ['Alpha', 'Beta', 'Teta', 'Sigma']
print(dstr)
print(f'{52*'-'}')

# 4. LIST untuk data BOOLEAN
print('4. List untuk DATA BOOL')
dbool = [True, False, False, True]
print(dbool)
print(f'{52*'-'}')

# 5. LIST untuk data CAMPURAN
print('5. List untuk DATA CAMPURAN')
dcom = [True, 'Gamma', 8.12, 93]
print(dcom)
print(f'{52*'-'}')

# 6. LIST dalam RANGE
print(f'6. List untuk DATA RANGE "range(2,12,2)" untuk membuat step sebanyak 2')
datar = range(2,12)
print(datar)
print(f'{35*'-'}')
datarl = list(datar)
print(datarl)
print(f'{52*'-'}')

# 7. List dengan metode FOR x in x (List Chomperesion)
print('7. List dengan metode FOR')
datalf = [x for x in range(3,12)]
print(datalf)
datalf1 = [x**2 for x in range(3,12)]
print(datalf1)
print(f'{52*'-'}')

# 8. List dengan metode FOR dan IF
print('8. List dengan metode FOR dan IF')
datafif = [y for y in range(1,15) if y != 7]
print(datafif)
print(f'{52*'-'}')

# 9. List dengan metode FOR dan IF (GENAP)
print('9. List dengan metode FOR dan IF (GENAP)')
datafifp = [y1 for y1 in range(1,15) if y1%2 == 0]
print(datafifp)
print(f'{52*'-'}')

# 10. List dengan metode FOR dan IF (GANJIL)
print('10. List dengan metode FOR dan IF (GANJIL)')
datafifl = [y2 for y2 in range(1,15) if y2%2 != 0]
print(datafifl)
print(f'{52*'-'}')


print(f'''




{80*'-'}''')
print('----------------------------XXX. Manipulasi List (30)----------------------------')
print(80*'-')

# 1. Pickup Data dalam LIST
print('1. Pickup Data dalam LIST')
# INDEX : 0/-3      1/-2     2/-1
cls =   ['Alpha', 'Sigma', 'Omega']
print(f'   Data dari LIST CLS = {cls}')

cls1 = cls[1]
clsm1 = cls[-1]
print(f'   I. Indeks ke-2 dari data CLS = {cls1}')
print(f'  II. Indeks terakhir dari data CLS = {clsm1}')

print(80*'-')

# 2. Mengetahui jumlah data pada LIST
print('2. Mengetahui jumlah data pada LIST')
clss = ['Zero', 'Teta', 'Beta', 'Mega', 'Simplex']
print(f'   Data dari LIST CLSS = {clss}')
cclss = len(clss)
print(f' III. Jumlah Data pada LIST CLSS = {cclss}')

print(80*'-')

# 3. Insert Data dalam LIST
print('3. Menambahkan data pada LIST sesuai number')
# Berdasarkan aturan sebelumnya
#     0/-6  1/-5   2/-4    3/-3     4/-2    5/-1
xs = ['12', '19', 'Blue', 'White', 'True', '18.2']
print(f'   Data XS sebelum ditambahkan = {xs}')
xs.insert(-4,'Army')
print(f'  IV. Data XS setelah ditambahkan pada (-4) = {xs}')

print(80*'-')

# 4. Insert Data pada akhir LIST 
print('4. Menambahkan data pada akhir LIST')
xs.append('Nova Sphere')
print(f'   V. Data XS setelah ditambahkan diakhir data = {xs}')

print(80*'-')

# 5. Insert Data pada LIST dengan LIST
print('5. Menggabungkan Data pada LIST dengan LIST')
ys = ['Blank', 'False', '259']
xs.extend(ys)
print(f'  V2. Data Koalisi LIST XS dengan YS = {xs}')

print(80*'-')

# 6. Exchange Data pada LIST 
print('6. Mengganti Data pada LIST')
print(f'    Data LIST XS sebelum di exchange = {xs}')
xs[-7] = 'Crown'
print(f'  VI. Data LIST XS setelah di exchange = {xs}')

print(80*'-')

# 7. Remove Data pada LIST 
print('7. Menghapus Data pada LIST')
xs.remove('18.2')
print(f'  VII. Data dari LIST XS setelah di Remove 1 Variabel = {xs}')

print(80*'-')

# 8. Remove Data yang ada pada akhir LIST 
print('8. Menghapus Data yang ada pada akhir LIST')
xs.pop()
print(f'  VIII. Data dari LIST XS setelah di Remove Variabel terakhir = {xs}')


print(f'''




{80*'-'}''')
print('----------------------------XXXI. Operasi List (31)----------------------------')
print(80*'-')

# 1. COUNT data pada LIST
print('1. Menghitung jumlah data yang ada pada LIST')
smg = ['UZI', 'VECTOR', 'VECTOR', 'UZI', 'RIOT', 'UMP9', 'VECTOR']
cvec = smg.count('VECTOR')
criot = smg.count('RIOT')
print(f'   I) Banyak var VECTOR pada SMG           = {cvec}')
print(f'  II) Banyak var RIOT pada SMG             = {cvec}')

print(80*'-')

# 2. INDEX data pada LIST
print('2. Mengetahui posisi data yang ada pada LIST')
smgs = ['UZI', 'VECTOR', 'RIOT', 'UMP9']
iuzi = smgs.index('UZI')
ivec = smgs.index('VECTOR')
print(f' III) Posisi var UZI pada SMGS             = {iuzi}')
print(f'  IV) Posisi var VECTOR pada SMGS          = {ivec}')

print(80*'-')

# 3. SORT data pada LIST
print('3. Mengurutkan posisi data yang ada pada LIST')
nums = [2, 54, 4, 6,18, 9, 11, 94 , 13, 15, 101, 16, 21]
print(f'   V) Diketahui LIST NUMS                  = {nums} ')
nums.sort()
print(f'  VI) Data NUMS setelah di sort            = {nums}')

print(80*'-')

# 4. REVERSE setelah SORT data pada LIST
print('4. Mengurutkan terbalik posisi data yang ada pada LIST')
nums.reverse()
print(f'  VII) Data NUMS setelah di sort terbalik  = {nums}')


print(f'''




{80*'-'}''')
print('----------------------------XXXII. Copy List (32)----------------------------')
print(80*'-')

# Menduplikat LIST tanpa hex id yang sama (copy dengan berbeda ID)
print(f'{20*'-'}I) Copy LIST dengan ID yang berbeda (I{20*'-'}')
'''
Ditujukan agar ketika A = B
dan variabel pada list A dirubah, maka tidak merubah pula komposisi variabel pada LIST B
'''

inx = ['Y', 'Z', 'X']
onx = inx
enx = inx.copy()

print(f' VIII) Nilai HEX ID List INX = {hex(id(inx))}')
print(f'   IX) Nilai HEX ID List ONX = {hex(id(onx))}')
print(f'    X) Nilai HEX ID List ENX = {hex(id(enx))}')

print(80*'-')