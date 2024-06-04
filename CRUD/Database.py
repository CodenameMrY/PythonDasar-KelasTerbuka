# from signal import pause

from . import Operasi

DB_NAME  = 'database.txt'
TEMPLATE = {
    'pk'    : 50*' ',
    'pl'    : 50*' ',
    'jl'    : 40*' ',
    'rt'    : 'NN'
}

def init_console() :
    try :
        with open(DB_NAME, 'r') as files :
            print('Hint = Database Avaible, init done!')
    except :
        print('Alert = Database tidak ditemukan, creating new file :')
        Operasi.create_dl()
        # with open(DB_NAME, 'w', encoding='utf-8') as files :
        #     penyanyi = input(f'1. Nama Penyanyi = ')
        #     judul    = input(f'2. Judul Lagu    = ')
        #     rating   = input(f'3. Rating Lagu   = ')
        #     data_str = f'{penyanyi}, {judul}, {rating}'
        #     files.write(data_str)


