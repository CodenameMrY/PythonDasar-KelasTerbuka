import os
os.system('cls') 
# ---------------------------------------------------------------------Python Chapter 63-66------------------------------------------------------------------------

print(f'''




{155*'-'}''')
print('-------------------------------------------------------------------6[III] __main__ (63)--------------------------------------------------------------------')
print(155*'-')

# __Main__ adalah top level code enviroment

print(f'1. Variabel __name__ pada PythonDasar_12.py = {__name__}')

# Import fungsi0 sebagai modul

import Fungsi0

print(155*'-')

# __Name__ == __main__    | akan terjadi jika modul dipanggil menjadi program utama melalui terminal
# Contoh : python  PythonDasar_12.py  -->   FxZ = FxZ                         | terjadi karena Fxzero diimport sebagai module
# Comtoh : python  Fxzero.py          -->   FxZ = __main__                    | terjadi karena Fxzero diimport sebagai program utama
# Akan langsung diprint saat dipanggil, seperti init                          | sering ddigunakan sebagai tajuk pada package program






print(f'''




{155*'-'}''')
print('---------------------------------------------------------------6[IV] Read External File (64)----------------------------------------------------------------')
print(155*'-')

# Read file di Python, method 1 (close otomatis)
try :
    with open('C:\\Users\\p\\Downloads\\Programming Language\\Python\\mbackup.txt') as fback :
        print(fback.read())
        print(155*'-')
        fbr = fback.readline()
        print(fbr, end='')
except FileNotFoundError :
    print('File is missing')
# fback.close()
print(155*'-')


# Read file di Python, method 2 (close manual)
fback = open('C:\\Users\\p\\Downloads\\Programming Language\\Python\\mbackup.txt', mode = 'r')
print(fback.read(), end='')
print(155*'-')

print(f'1. File mbackup readable  = {fback.readable()}')
print(155*'-')

print(f'2. File mbackup writeable = {fback.writable()}')
print(155*'-')

fback.close()





print(f'''




{155*'-'}''')
print('---------------------------------------------------------------6[V] Write External File (65)----------------------------------------------------------------')
print(155*'-')


# 1. Metode 1, menimpa file dengan sintaks baru (write)
with open('timeline_pb.txt', 'w', encoding='utf-8') as filetrace :
    filetrace.write('1. Tutorial Python Dasar akan menjadi bekal untuk explore berbagai library, framework yang ada di python hingga bahasa pemrograman lainya\n2. Tutorial Python Dasar dipelajari dari Kanal Youtube Kelas Terbuka dari sekitar 01-2024 hingga 05-2024\n3. Tutorial Python Dasar terdiri dari 71 episode')


# 2. Metode 2, menambah file dengan sintaks baru (append)
with open('objecti.txt', 'w', encoding='utf-8') as filetraces :
    filetraces.write('Tanggal Bulan Tahun')
with open('objecti.txt', 'a', encoding='utf-8') as filetraces :
    filetraces.write('\n1. 26th May, 2024')
with open('objecti.txt', 'a', encoding='utf-8') as filetraces :
    filetraces.write('\n2. Jakarta, 13:27')





print(f'''




{155*'-'}''')
print('--------------------------------------------------------6[VI] Exception Error (Try and Except) (66)---------------------------------------------------------')
print(155*'-')




while(True) :
    print(50*'-')
    numb = int(input(f'1. Masukan nilai pembagi        = '))
    try :
        state = 250/numb
        print(f'2. Hasil Akhir                  = {state}')
        aldone = input(f'3. Lanjutkan input angka? (Y/N) = ')
        if aldone == 'N' :
            break
    except : 
        print('X. Mohon masukan nilai berbeda dan coba lagi')
print(155*'-')

while(True) :
    try :
        with open('timeline_cost.txt') as filepath :
            print(filepath.read())
        break
    except :
        print(f'File tersebut tidak ditemukan, membuat file baru')
        with open('tiemeline_cost.txt', 'w', encoding='utf-8') as filepfinder :
            filepfinder.write('File Baru')
        break
print(155*'-')

