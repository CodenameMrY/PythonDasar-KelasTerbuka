from operator import index
from . import Database
import os

from CRUD.Util import random_string

# from . Util import random_string, random_string2, random_string3

def delete(no_lagu) :
    try :
        with(open(Database.DB_NAME, 'r')) as file :
            counter = 0
            while(True) :
                content = file.readline()
                if len(content) == 0 :
                    break
                elif counter == no_lagu -1 :
                    pass
                else :
                    with open("data_temp.txt", 'a', encoding="utf-8") as temp_file :
                        temp_file.write(content)
                counter += 1
    except :
        print("Database Error!")
    
    os.rename("data_temp.txt", Database.DB_NAME)




def update(no_lagu,pk,ssing,stitle,srate) :
    data = Database.TEMPLATE.copy()

    data['pk'] = pk
    data['pl'] = ssing
    data['jl'] = stitle
    data['rl'] = srate

    data_str = f'{data['pk']}, {data["pl"]}, {data["jl"]}, {data["rl"]}\n'
    data_length = len(data_str)

    try :
        with(open(Database.DB_NAME, 'a+', encoding='utf-8')) as file :
            file.seek(data_length*(no_lagu-1))
            file.write(data_str)
    except :
        print('Terjadi error dalam update')


def create(penyanyi, judul, rating) :
    data = Database.TEMPLATE.copy()

    data['pk'] = random_string(8)
    data['pl'] = penyanyi + Database.TEMPLATE['pl'][len(penyanyi) :]
    data['jl'] = judul + Database.TEMPLATE['jl'][len(judul) :]
    data['rl'] = rating

    data_str = f'{data['pk']}, {data["pl"]}, {data["jl"]}, {data["rl"]}\n'

    try :
        with open(Database.DB_NAME,'a', encoding='utf-8') as files :
            files.write(data_str)
    except :
        print('Alert = Creating Data Failed')

    


def create_dl() :
    penyanyi = input(f'1. Nama Penyanyi = ')
    judul    = input(f'2. Judul Lagu    = ')
    rating   = input(f'3. Rating Lagu   = ')

    data = Database.TEMPLATE.copy()

    data['pk'] = random_string(8)
    data['pl'] = penyanyi + Database.TEMPLATE['pl'][len(penyanyi) :]
    data['jl'] = judul + Database.TEMPLATE['jl'][len(judul) :]
    data['rl'] = rating # + Database.TEMPLATE['rating'][len(rating) :]
    
    data_str = f'{data['pk']}, {data["pl"]}, {data["jl"]}, {data["rl"]}\n'
    # print(data_str)

    try :
        with open(Database.DB_NAME,'w', encoding='utf-8') as files :
            files.write(data_str)
    except :
        print('Alert = An Occcured Error')

def read(**kwargs) :
    try :
        with open(Database.DB_NAME, 'r') as file :
            content = file.readlines()
            jumlah_lagu = len(content)
            if 'index' in kwargs :
                index_lagu = kwargs['index']-1
                if index_lagu < 0 or index_lagu > jumlah_lagu :
                    return False
                else :
                    data_seplit = content[kwargs['index']-1]
                    return data_seplit
                    # print(f'Indeks terbaca = {content[kwargs['index']-1]}')
            else :
                return content
    except :
        print('Alert = Membaca Database Gagal!')
        return False


    # data['jl'] = random_string2(7)
    # data['rl'] = random_string3(2)
    
    



