# ----------------------------------------------------Python Chapter 48-52-------------------------------------------------------


import os
os.system('cls')

print(f'''




{149*'-'}''')
print('------------------------------------------------------------4[VIII] Latihan Fungsi (48)-------------------------------------------------------------')
print(149*'-')


# Program menghitung luas dan keliling persegi panjang


print(f'\n{60*'-'}I. Menghitung Luas dan Keliling{60*'-'}')
print(149*'-')

panjangp    = int(input('1. Masukkan panjang bangun ruang = '))
lebarp      = int(input('2. Masukkan panjang bangun ruang = '))
tinggip     = int(input('3. Masukkan tinggi bangun ruang  = '))

vollumep    = panjangp*lebarp*tinggip
kelilingp   = 4*(panjangp+lebarp+tinggip)

print(149*'-')

print(f'4. Vollume Balok berdasarkan nilai yang diinput yaitu  = {vollumep} cm')
print(f'5. Keliling Balok berdasarkan nilai yang diinput yaitu = {kelilingp} cm')
print(149*'-')
'''
'''
def cover() :
    # os.system('cls')
    print(f'\n{60*'-'}I. Menghitung Luas dan Keliling{60*'-'}')
    print(149*'-')

def broom() :
    panjangp    = int(input('1. Masukkan panjang bangun ruang = '))
    lebarp      = int(input('2. Masukkan panjang bangun ruang = '))
    tinggip     = int(input('3. Masukkan tinggi bangun ruang  = '))

    vollumep    = panjangp*lebarp*tinggip
    kelilingp   = 4*(panjangp+lebarp+tinggip)


while True :
    cover()
    broom()

    spread = input('Lanjutkan menginput? (y/n) = ')
    if spread == 'n' :
        break
print(f'{60*'-'}Akhir dari Program{60*'-'}')





print(f'''




{149*'-'}''')
print('---------------------------------------------------------------4[IX] Type Hints (49)----------------------------------------------------------------')
print(149*'-')

# Penggunaan Type Hints


def fxample(BB, TB : float) -> float :
    print(f'1. Berat badan anda           = {BB}')
    print(f'2. Tinggi badan anda          = {TB}')
    bmi = BB // TB**2
    print(f'3. Jadi, Body Mass Index anda = {bmi}')

inbb = int(input('>. Masukkan BB anda = '))
intb = float(input('>. Masukkan TB anda = '))

print(149*'-')

outbt = fxample(inbb, intb)
print(outbt)

print(149*'-')





print(f'''




{149*'-'}''')
print('---------------------------------------------------------------5[0] args dalam Fungsi (50)----------------------------------------------------------------')
print(149*'-')

def fxamp(*args) :
    name    = args[0]
    age     = args[1]
    cl      = args[2]
    print(f'{name}, an employeer {age} years old, with {cl} cm tall')

fxamp('Budi',27,180)

# UNtuk menggunakan args hanya perlu menyematkan '*' pada argument

def plusx(*numbers) :
    contain = 0
    for number in numbers :
        contain += number
    return contain

plus1 = plusx(8,10,12,14,16,18,20)
print(f'Nilai plus1 = {plus1}')

print(149*'-')

plus2 = plusx(128,277,321)
print(f'Nilai plus2 = {plus2}')

print(149*'-')





print(f'''




{149*'-'}''')
print('---------------------------------------------------------------5[I] kwargs dalam Fungsi (51)----------------------------------------------------------------')
print(149*'-')

def fxux(Merek, Seri, Tahun) :
    print(f'Merek motor {Merek}, Seri motor {Seri}, dan Tahun produksi {Tahun}')

fxux('Yamaha', 'Verza', 2024)

print(149*'-')

# Kwargs mengambil data berupa Dictionary

def fxix(**kwargs) :
    Merek = kwargs['Merek']
    Seri  = kwargs['Seri']
    Tahun = kwargs['Tahun']
    print(f'Merk motor {Merek}, Seri motor {Seri}, dan Tahun produksi {Tahun}')

fxix(Merek='Yamaha', Seri='XSR', Tahun='2024')

print(149*'-')

def math(*args,**kwargs) :
    output = 0
    if kwargs['option'] == 'tambah' :
        for angka in args :
            output += angka

    elif kwargs['option'] == 'kali' :
        output = 1
        for angka in args :
            output *= angka
        else :
            print('Tidak ada command')
    return output

hasil = math(1,3,5, option='tambah')
print(f'1. Hasil dari penjumlahan = {hasil}')

print(149*'-')

hasil = math(1,3,5, option='kali')
print(f'2. Hasil dari perkalian   = {hasil}')

print(149*'-')





print(f'''




{149*'-'}''')
print('------------------------------------------------------5[II] Anonymous dan Lambda Function (52)-------------------------------------------------------')
print(149*'-')

# 1. Ordinary Function
print(f'1. Ordinary Function')

def fx_dopple(number) :
    return number**4
print(f'   > Diketahui fx_dopple = num**4')
print(f'   > Nilai 8 jika dipangkatkan dengan fungsi dopple  = {fx_dopple(8)}')
print(149*'-')



# 2. Lambda Function
print(f'2. Ordinary Function')

dopples = lambda numbers : numbers**4
print(f'   > Diketahui dopples    = num**4')
print(f'   > Nilai 16 jika dipangkatkan dengan lambda dopples = {dopples(16)}')
print(149*'-')


lpp = lambda p, l : p*l
print(f'   > Diketahui lambda lpp = p*l')
print(f'   > Jika Nilai p=12 dan l=7, maka lambda lpp menjadi = {lpp(12, 7)}')

print(149*'-')



# 3. Sorting List menggunakan Function
listcity = ['New York', 'Washington DC', 'Detroit']

def countlen(city) :
    return len(city)
listcity.sort(key=countlen)
print(f'3. List yang disortir menggunakan regular funtion, diurutkan berdasarkan alfabet = {listcity}')

print(149*'-')

# 4. Sorting List menggunakan Function
listcountry = ['United States', 'Indonesian', 'Sweden']

listcountry.sort(key=lambda country:len(country))
print(f'4. List yang disortir menggunakan lambda funtion, diurutkan berdasarkan alfabet = {listcountry}')
print(149*'-')



# 5. Filter data Angka menggunakan lambda function
print(f'5. Sorting data angka menggunakan fungsi lambda')

thenumbers = [12,22,32,42,52,62,72,82]
sortednum = list(filter(lambda x:x <50, thenumbers))
print(f'   > Diketahui list thenumbers                 = {thenumbers}')
print(f'   > List thenumbers setelah disortir <50 maka = {sortednum}')
print(149*'-')



numbero = [1,2,4,5,7,8,11,13,14,25,26,28,33,37,39]

# 6. Filter data Angka menggunakan lambda menjadi genap
print(f'6. Filter data Angka menggunakan lambda menjadi genap')
sortedgnum = list(filter(lambda x:(x%2==0), numbero))
print(f'   > Diketahui list numbero                      = {numbero}')
print(f'   > List numbero setelah disortir num%2==0 maka = {sortedgnum}')
print(149*'-')



# 7. Filter data Angka menggunakan lambda menjadi ganjil
print(f'7. Filter data Angka menggunakan lambda menjadi ganjil')
sortedjnum = list(filter(lambda x:(x%2!=0), numbero))
print(f'   > Diketahui list numbero                      = {numbero}')
print(f'   > List numbero setelah disortir num%2!=0 maka = {sortedjnum}')
print(149*'-')



# 8. Function Anonymous Lambda currying
print(f'8. Function Anonymous Lambda currying')

def fx_pangkat(x) :
    return lambda num:num**x

# Penulisan Opsi 1
fxp3 = fx_pangkat(3)
print(f'    > Jika nilai 5 dipangkatkan dengan fx_pangkat, maka hasilnya = {fxp3(5)}')

# Penulisan Opsi 2
print(f'    > Jika nilai 7 dipangkatkan dengan 3, maka hasilnya          = {fx_pangkat(3)(7)}')
print(149*'-')
