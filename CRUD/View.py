# from operator import index
from importlib.resources import contents
from . import Operasi

#   Gunakan tkinter untuk UI lebih baik

def delete_console() :
    read_console()
    while(True):
        no_lagu = int(input('Hint = Silahkan pilih No. lagu yang akan di Delete : '))
        data_lagu = Operasi.read(index=no_lagu)

        if data_lagu :
            data_break = str(data_lagu).split(',')
            pk         = data_break[0]
            ssing      = data_break[1]
            stitle     = data_break[2]
            srate      = data_break[3][:-1]

   
            print(180*'-')
            print(f'Hint = Silahkan pilih data yang ingin anda Delete :')
            print(f'1. Penyanyi Lagu    = {ssing:.30}')
            print(f'2. Judul Lagu       = {stitle:.30}')
            print(f'3. Rating Lagu      = {srate:2}')
            casedone = input('Delete variabel? (Y/N) = ')
            if casedone == 'Y' or casedone == 'y' :
                Operasi.delete(no_lagu)
                break
        else :
            print('Alert = No. tidak valid, silahkan ulangi')
    print('Data berhasil dihapus')

        
        

def update_console() :
    read_console()
    print('\n')
    while(True):
        no_lagu = int(input('Hint = Silahkan pilih No. lagu yang akan di Update : '))
        data_lagu = Operasi.read(index=no_lagu)

        if data_lagu :
            break
        else :
            print('Alert = No. tidak valid, silahkan ulangi')


        casedone = input('Selesai mengupdate? (Y/N) = ')
        if casedone == 'Y' or casedone == 'y' :
            break

    data_break = str(data_lagu).split(',')
    pk         = data_break[0]
    ssing      = data_break[1]
    stitle     = data_break[2]
    srate      = data_break[3][:-1]
    
    while(True) :
        print(180*'-')
        print(f'Hint = Silahkan pilih data yang ingin anda ubah :')
        print(f'1. Penyanyi Lagu    = {ssing:.30}')
        print(f'2. Judul Lagu       = {stitle:.30}')
        print(f'3. Rating Lagu      = {srate:2}')

        user_option = input('Pilih jenis data [1,2,3] = ')
        print(180*'-')
        match user_option :
            case '1' : ssing  = input('1. Penyanyi Lagu = ')
            case '2' : stitle = input('2. Judul Lagu    = ')
            case '3' : srate  = input('3. Rating Lagu   = ')
            case  _  : print('Indeks yang anda masukan salah')
        
        print('Data Baru anda :')
        print(f'1. Penyanyi Lagu    = {ssing:.30}')
        print(f'2. Judul Lagu       = {stitle:.30}')
        print(f'3. Rating Lagu      = {srate:2}')

        casedone = input('Selesai mengupdate? (Y/N) = ')
        if casedone == 'Y' or casedone == 'y' :
            break

    Operasi.update(no_lagu,pk,ssing,stitle,srate)

    
    
    
    
def create_console() :
    print('\n\n'+'-'*180)
    print('Hint = Silahkan tambahkan data Lagu :')
    penyanyi = input(f'1. Masukan nama penyanyi = ')
    judul    = input(f'2. Masukan judul lagu    = ')
    rating   = int(input(f'3. Masukan rating lagu   = '))

    Operasi.create(penyanyi, judul, rating ) # type: ignore
    print('\nData baru telah ditambahkan!')
    read_console()




def read_console() :
    data_file   = Operasi.read()

    index       = 'UID'
    ssing       = 'PENYANYI'
    stitle      = 'JUDUL'
    srate       = 'RATING'

    # Header
    print('\n' + 180*'-')


    print(f'{index.center(8):} | {ssing.center(65)} | {stitle.center(85)} | {srate.center(8)}')
    print(180*'-')

    # Data
    for index, data in enumerate(data_file) :  # type: ignore
        if isinstance(data, str) :
            data_break = data.split(',')
            pk = data_break[0]
            ssing = data_break[1]
            stitle = data_break[2]
            srate = data_break[3]

            print(f'{index+1:^8} | {ssing.center(65)} | {stitle.center(85)} | {srate.center(8)}') # type: ignore
            # print(f'{index:^8} | {ssing:^65} | {stitle:^85} | {srate:<8}')
            
            
        else :
            print('Alert = Terjadi kesalahan, variabel data bukan merupakan string')
        

    # Footer
    print( + 180*'-')

