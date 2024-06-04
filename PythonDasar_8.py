# ----------------------------------------------------Python Chapter 43-47-------------------------------------------------------


import datetime
import os
import string
import random
os.system('cls')


print(f'''
{149*'-'}''')
print('----------------------------------------------------------4[III] Latihan Dictionary (43)-----------------------------------------------------------')
print(149*'-')






library = {
    'NIU001'    : '1013545',
    'PASSG'     : 'Termuno',
    'USERCODE'  : 234,
    'DATE'      : datetime.datetime(2000,10,31)
}

dsub = {}

while True :
    
    print(149*'-')
    print(f'{'Data Subject II':^148}')
    print(149*'-')

    print(f'1. Latihan InputUser Dictionary')

    print(149*'-')


    
    csub = dict.fromkeys(dsub.keys())


    csub['NIU001'] = input(f'     Nomor Individu      = ')
    csub['PASSG'] = input(f'     Password            = ')
    csub['USERCODE'] = input(f'     Nomor Subjek        = ')

    years = int(input(f'     > Tahun Observasi   = '))
    month = int(input(f'     > Bulan Observasi   = '))
    date = int(input(f'     > Tanggal Observasi = '))

    csub['DATE'] = datetime.datetime(years, month, date)

    print(149*'-')

    

    KEY = ''.join((random.choice(string.ascii_uppercase) for w in range(7)))
    dsub.update({KEY : csub})

    print(f'{'KEY':<16} {'NIU001':<36} {'PASSG':<24} {'USERCODE':<18} {'DATE':^28}')
    print(149*'-')



    for csub in dsub :
       KEY           = csub
       NIU001        = dsub[KEY]['NIU001']
       PASSG         = dsub[KEY]['PASSG']
       USERCODE      = dsub[KEY]['USERCODE']
       DATE          = dsub[KEY]['DATE'].strftime('%x')

       print(f'{KEY:<16} {NIU001:<36} {PASSG:<24} {USERCODE:<18} {DATE:^28}')

    state = input('Lanjut isi data ? (Y/N) ')
    if state == 'N' :
        break
print(149*'-')





print(f'''




{149*'-'}''')
print('---------------------------------------------------4[IV-V] Introduksi dan Fungsi Argumen (44-45)----------------------------------------------------')
print(149*'-')

# 1. Fungsi sederhana menggunakan DEFINITION
print(f'I. Fungsi sederhana menggunakan DEFINITION')

print(149*'-')

def fungi() :
    usernick = input('1. Tuliskan Nama anda  = ')
    userage = int(input('2. Tuliskan Umur anda  = '))
    useract = input('3. Tuliskan Hobby anda = ')
    
    print(f'    {30*'-'}')
    print(f'    > Nama anda        = {usernick}')
    print(f'    > Umur anda        = {userage}')
    print(f'    > Hobby anda       = {useract}')



print(149*'-')

# 2. Database Nama pertama

userin2 = input(f'II. Nama anda          = ')
userin3 = input(f'    Umur anda          = ')
userin4 = float(input(f'    Berat badan anda   = '))

def nick(userin2, userin3, userin4) :
    print(f'    {32*'-'}')
    print(f'    > Nama anda        = {userin2}')
    print(f'    > Umur anda        = {userin3}')
    print(f'    > Berat badan anda = {userin4}')



userdatabase = nick(userin2, userin3, userin4)
print(userdatabase)

print(149*'-')

# 3. Database Nama kedua
userin2 = input(f'II. Nama anda          = ')
userin3 = input(f'    Umur anda          = ')
userin4 = float(input(f'    Berat badan anda   = '))

userdatabase = nick(userin2, userin3, userin4)
print(userdatabase)

print(149*'-')





print(f'''




{149*'-'}''')
print('----------------------------------------------------------4[VI] Fungsi dengan Return (46)-----------------------------------------------------------')
print(149*'-')

# Template Fungsi dengan Return
# def nama_fungsi(argument) :
#     (badan) formula fungsi

def rng(input_code) :
    output_code = input_code*14**3+282-23
    return output_code

print(f'1. Fungsi Return ID generator :')
userinx = int(input('   I. Masukan kode yang anda inginkan = '))


xent = rng(userinx)
print(f'   II. ID kode untuk NUMBERS {userinx}   = {xent}')
print(149*'-')



def datasiswa(inj,injj, ink,inkk, inl,inll) :
    siswa1 = print(f'   1. Nama siswa = {inj}, Kelas = {injj}')
    siswa2 = print(f'   2. Nama siswa = {ink}, Kelas = {inkk}')
    siswa3 = print(f'   3. Nama siswa = {inl}, Kelas = {inll}')
    return   siswa1,siswa2,siswa3

users11 = input(f'   III)1. Masukkan nama siswa  = ')
users12 = input(f'   III)2. Masukkan kelas siswa = ')
print(72*'-')
users21 = input(f'   III)1. Masukkan nama siswa  = ')
users22 = input(f'   III)2. Masukkan kelas siswa = ')
print(72*'-')
users31 = input(f'   III)1. Masukkan nama siswa  = ')
users32 = input(f'   III)2. Masukkan kelas siswa = ')
print(72*'-')

databasesiswa = datasiswa(users11,users12, users21,users22, users31,users32)
print(databasesiswa)
print(149*'-')





print(f'''




{149*'-'}''')
print('-----------------------------------------------------4[VII] Fungsi dengan Default Argument (47)------------------------------------------------------')
print(149*'-')

# Default Argument ditujukan untuk pengganti variabel input dalam FUNCTION yang tidak diisi / dikosongkan

def statusp(Nama, Status = 'Tidak diisi!') :
    print(f'     I. Nama anda   = {Nama}')
    print(f'    II. Status anda = {Status}')


insp  = input('1. Nama anda   = ')
outsp = input('2. Status anda = ')

print(72*'-')

outputsp = statusp(insp, outsp)
print(outsp)

print(72*'-')

def varie(num5 = 7, num6 = 14, num7 = 21, num8 = 28) :
    vary = num5 + num6 * num7 + num8 
    return vary

print(varie(num6 = 20, num8 = 250))
print(149*'-')
    