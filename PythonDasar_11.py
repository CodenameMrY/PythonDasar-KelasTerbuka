import os
os.system('cls')
# ----------------------------------------------------Python Chapter 58-62-------------------------------------------------------

print(f'''




{144*'-'}''')
print('------------------------------------------------------5[VIII] Global dan Local Scope (58)-------------------------------------------------------')
print(144*'-')

import datetime

print(f'1. Standard Library DATETIME')

trn = datetime.datetime.now()
print(f'   1) Waktu saat ini = {trn}')

tiy = trn.year
print(f'   2) Tahun saat ini = {tiy}')

tim = trn.month
print(f'   3) Bulan saat ini = {tim}')

tid = trn.strftime('%A')
print(f'   4) Hari saat ini  = {tid}')
print(144*'-')

print(f'2. Standard Library COLLECTIONS')

from collections import Counter

ListNum = ['d', 'a','w', 's', 'w', 'w', 's']

cln = 0
for n in ListNum :
    if n == 'w':  
          cln += 1

print(f'   1) Jumlah "w" pada LIstNum menggunakan metode for, if    = {cln}')

print(f'   2) Jumlah tiap variabel pada ListNum menggunakan Counter = {Counter(ListNum)}')

pack1 = Counter(ListNum)

print(f'   3) Jumlah "s" pada ListNum menggunakan Counter           = {pack1['s']}')
print(144*'-')


print(f'3. Standard Library Input Output (IO)')

import io

# rulesdc = io.open("rules_text.txt","r")  # HANYA JIKA MAIN PROGRAM DAN MODUL BERADA DALAM SATU FOLDER
# print(rulesdc.read())
print(144*'-')





print(f'''




{144*'-'}''')
print('--------------------------------------------5[IX] tkinter dan Graphical Usser Interface (GUI) (59)---------------------------------------------')
print(144*'-')




print(f'1. Implementasi dari window tkinter')

# Import

import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo

# Init

window = tk.Tk()
window.configure(bg='sky blue')
window.geometry('1200x720')

window.resizable(False, False) # Window tidak dapat di resize pada sumbu x maupun y

window.title('List-Rating Music')

# 1. Membuat frame inputUser
input_frame = ttk.Frame(window)  # Agar frame dapat ditampilkan pada window maka perlu melakukan positioning terlebih dahulu


# 1.1 Positioning : Grid, Pack, Place
input_frame.pack(padx=10, pady=10, fill='x', expand=True)


# 1.2 Komponen Judul Lagu
titlel = ttk.Label(input_frame, text='Judul Lagu')
titlel.pack(padx=10, pady=2, fill='x', expand=True)


# 1.3 Label window title 'Judul Lagu'  |   Variabel dan Fungsi
JUDUL_LAGU = tk.StringVar()

titlelw = ttk.Entry(input_frame, textvariable=JUDUL_LAGU)
titlelw.pack(padx=10, pady=2, fill='x', expand=True)


# ----------------------------------------------------------------


# 1.4 Komponen Penyanyi
singerl = ttk.Label(input_frame, text='Penyanyi Lagu')
singerl.pack(padx=10, pady=2, fill='x', expand=True)


# 1.5 Label window title 'Penyanyi'
PENYANYI = tk.StringVar()

singerlw = ttk.Entry(input_frame, textvariable=PENYANYI)
singerlw.pack(padx=10, pady=2, fill='x', expand=True)

# ----------------------------------------------------------------

# 1.6 Komponen Rating Lagu
ratel = ttk.Label(input_frame, text='Rating Lagu')   # BISA DI FORMAT f'
ratel.pack(padx=10, pady=2, fill='x', expand=True)


# 1.7 Label window title 'Rating Lagu'
RATING_LAGU = tk.StringVar()

ratelw = ttk.Entry(input_frame, textvariable=RATING_LAGU)
ratelw.pack(padx=10, pady=2, fill='x', expand=True)

# 1.8 Komponen Button/Tombol
def buttond() :
     msg = f'1. Judul lagu = {JUDUL_LAGU.get()}  \n2. Penyanyi    = {PENYANYI.get()}  \n3. Rating        = {RATING_LAGU.get()}  \nTekan ok untuk lanjut'
     {showinfo(title='Data Musik', message=msg)} # type: ignore
            


buttons = ttk.Button(input_frame, text='Submit', command=buttond) # PART PENTING!
buttons.pack(padx=10, pady=5, fill='x', expand=True)
               
# 2. Main Loop Window
window.mainloop()





print(f'''




{144*'-'}''')
print('-----------------------------------------------------------6[0] Introduksi PIP (60)-------------------------------------------------------------')
print(144*'-')

# pypi.org website fundamental bagi Python

# Open Command Prompt / Terminal, ketik PIP enter 
# ketik : PIP --version                         | untuk mengetahui versi program Python
# ketik : pip list                              | untuk mengetahui program yang telah diinstal
# ketik : python -m pip install --upgrade pip   | untuk melakukan upgrade versi pada pip
# ketik : pip install {package}                 | untuk menginstal package python
# ketik : pip install {package}==1.22.1         | untuk menginstal package python dengan versi diinginkan
# ketik : pip uninstall {package}               | untuk uninstal package pada pip




print(f'''




{144*'-'}''')
print('-----------------------------------------------------------6[I] Package Numpy (61)-------------------------------------------------------------')
print(144*'-')

import  numpy as np

alphai = [1, 3, 5, 7, 10]
betai  = np.array([2, 4, 6, 8, 12])

print(f'1. Variabel List a (metode umum)          = {alphai}')                   # List ini tidak bisa asssignment method
print(144*'-')

print(f'2. Variabel List b (metode array vector) = {betai**2}')                 # List ini bisa assignment method
print(144*'-')

matriksx = np.array([(3, 7, 2),(2,8,4)])
print(f'3. Variabel List c (metode array vector) = \n{matriksx}')
print(144*'-')

matriksy = np.zeros((3,1))
print(f'4. Variabel List zeros                   = \n{matriksy}')
print(144*'-')

matriksz = np.ones((4,2))
print(f'5. Variabel List ones                    = \n{matriksz}')
print(144*'-')

# matrixu = matriksz - matriksy - matriksx**4
# print(f'Hasil akhir dari matrix                  = \n{matrixu}')
# print(144*'-')





print(f'''




{144*'-'}''')
print('-----------------------------------------------------------6[I] Package Numpy (61)-------------------------------------------------------------')
print(144*'-')

import pygame

# Struktur dasar Operasional Game
# 1. Init                             (World, Main Character)
# 2. User Input, Database Input       (Pilih mode, menu)
# 3. Update Asset                     (Update command, run game)
# 4. Render to Display                (Window) [Program terberat]

print(f'1. Langkah Dasar pembuatan Game')
# 1. Fase Init
print(f'   1) Fase Init')
pygame.init()                         # Program ini wajib dilooping agar tidak close

#    KEY1. Window (Surface Object Operation)
windowp = 720
windowl = 500
window = pygame.display.set_mode((windowp,windowl))

#    1.1.1 Object
#          Position Object
x = 400
y = 250

#          Size Object
lenghto = 32
heighto = 8

#          Movement Speed
speedo = 3

GameRun = True
while GameRun :
     pygame.time.delay(10)
     for event in pygame.event.get() :
          if event.type == pygame.QUIT :
               GameRun = False

     # Ambil semua keyboard press
     path = pygame.key.get_pressed()

     if path[pygame.K_LEFT] and x > 0 :
          x -= speedo

     if path[pygame.K_RIGHT] and x < windowp-lenghto :
          x += speedo

     if path[pygame.K_DOWN] and y < windowl-heighto :
          y += speedo

     if path[pygame.K_UP] and y > 0 :
          y -= speedo

     # KEY3. Update Asset
     window.fill((250,250,250))
     pygame.draw.rect(window,(250,0,0), (x,y, lenghto, heighto))

     # KEY4. Display
     pygame.display.update()

pygame.quit()


