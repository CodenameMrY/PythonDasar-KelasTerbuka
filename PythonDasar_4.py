#----------------------------------------------------Python Chapter 22-27-------------------------------------------------------

print('Hello Worldo')
print(80*'-')
print('-----------------------------XXII.ELIF statement (22)----------------------------')
print(80*'-')

# 1. Implementasi ELIF Statement

print(f'''
Kami sedang mengumpulkan data para Adventurer,
Silahkan input rank anda diantara data berikut ini :
1. Destroyer  (I)
2. Conqueror  (II)
3. Gladiator  (III)
4. Champion   (IV)
5. Challenger (V)
6. Rookie     (VI)
7. Novice     (VII)
''')

rank = input('1. Input rank anda? ')

if rank == 'Destroyer' :
    print('-  Combat Power anda = 19,858-35,000')
    print('-  Experience anda worth = 20-32 years')
elif rank == 'Conqueror' :
    print('-  Combat Power anda = 12,535-14,520')
    print('-  Experience anda worth = 15-19 years')
elif rank == 'Gladiator' :
    print('-  Combat Power anda = 10,522-12,003')
    print('-  Experience anda worth = 10-14 years')
elif rank == 'Champion' :
    print('-  Combat Power anda = 8,910-9,422')
    print('-  Experience anda worth = 8-9 years')
elif rank == 'Challenger' :
    print('-  Combat Power anda = 5,782-6,959')
    print('-  Experience anda worth = 5-7 years')
elif rank == 'Rookie' :
    print('-  Combat Power anda = 2,102-2,801')
    print('-  Experience anda worth = 2-3 years')
elif rank == 'Novice' :
    print('-  Combat Power anda = 302-1,200')
    print('-  Experience anda worth = <2 years')
else :
    print('Maaf, tolong masukan data yang tepat dan ulangi kembali')

print(f'''
{80*'-'}''')





print(f'''




{80*'-'}''')
print('--------------------------XXIII.Kalkulator Sederhana (23)-------------------------')
print(80*'-')

num1 = float(input('1. Masukan Variabel pertama = '))
num2 = float(input('2. Masukan Variabel kedua = '))
op = input(f'''Pilih Function yang diinginkan
1. (+)
2. (-)
3. (*)
4. (/)    
Function yang anda gunakan : ''')


# OPERATOR
# 1. Operator (+)
if op == '+' :
    r = num1 + num2
    print(f'3. Hasil dari {num1} + {num2} =', int(r))
elif op == '-' :
    r = num1 - num2
    print(f'3. Hasil dari {num1} - {num2} =', int(r))
elif op == '*' :
    r = num1 * num2
    print(f'3. Hasil dari {num1} * {num2} =', int(r))
elif op == '/' :
    r = num1 / num2
    print(f'3. Hasil dari {num1} / {num2} =', int(r))
else :
    print('Silahkan ulangi, dan input sesuai instruksi')
print(80*'-')





print(f'''




{80*'-'}''')
print('--------------------------------XXIV.FOR Loop (24)------------------------------')
print(80*'-')

# 1. Mengggunakan List (Metode manual)
hp = [0,1,2,3,4,5,6.7,8,9,10,11,12]
for x in hp :
    print(f'Nilai X pada tiap looping adalah : {x}')
print(f'''{80*'-'}
''')

print(f'''
{80*'-'}''')
# 2. Menggunakan Range (Metode Auto menggunakan looping)
hp12 = range(3,12)
# pada 'range(3,12)' artinya dimulai dari angka 3, sebanyak 9 angka (12-3)
for y in hp12 :
    print(f'Nilai y pada tiap looping adalah : {y}')
print(80*'-')

print(f'''
{80*'-'}''')
# 3. Menggunakan Range (Looping STR)
title = 'The Raid'
for a in title :
    print(a)
print(80*'-')





print(f'''




{80*'-'}''')
print('--------------------------------XXV.WHILE Loop (25)------------------------------')
print(80*'-')

# 1. Menggunakan WHILE Loop
#    Akan terus looping hingga input = false

numl = 1
print(f'Bilangan saat ini : {numl}')
while numl < 20 :
    numl += 2
    print(f') Bilangan saat ini : {numl}')
    print('   >  Merupakan bilangan ganjil')
print(f'{32*'-'}Akhir dari program{32*'-'}')
print(82*'-')





print(f'''




{80*'-'}''')
print('---------------------XXVI-XVII.CONTINUE, PASS, dan BREAK (26-27)--------------------')
print(80*'-')

# 1. PASS berfungsi sebagai dummy yang tidak akan dieksekusi------------------------------
numex = 7
while numex <= 32 :
    numex += 3
    if numex == 19 :
        pass
    print(numex)

print(f'''{80*'-'}''')


# 2. CONTINUE------------------------------------------------------------------------------
numix = 243
print(f'Nilai NUMIX saat ini : {numix}')
while numix < 1250 :
    numix +=240
    print(f'Nilai NUMIX saat ini : {numix}')                 # AKSI 1

    if numix == 963 :
        print('] HEY, HEY! [')
        continue                                             # Akan skip AKSI dibawahnya
    print('NUMIX fixed')                                     # AKSI 2

print(f'{32*'-'}Akhir dari program{32*'-'}')


# 3. BREAK----------------------------------------------------------------------------------
numyx = 243
print(f'Nilai NUMYX saat ini : {numyx}')
while numyx < 1250 :
    numyx += 240
    print(f'Nilai NUMYX saat ini : {numyx}')                 # AKSI 1

    if numyx == 963 :
        print('] OI, OI! [')
        break                                                # Akan end LOOPING dan AKSI setelahnya
    print('NUMYX fixed')                                     # AKSI 2

print(f'{32*'-'}Akhir dari program{32*'-'}')
print(f'{32*'-'}Implementasi BREAK{32*'-'}')

# -------------------------------------------------------------------------------------------

examt = int(input('I. Sequence = '))

numdx = 0
while True :
    numdx += 1
    print(f'{numdx}')

    if numdx == examt :
        print(f'{32*'-'}Akhir dari program{32*'-'}')
        break

