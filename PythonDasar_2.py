print('-----------------------VIII.Operasi Logika Boolean-----------------------')

# Function yang tersedia
# 1. NOT ~
# 2. OR |
# 3. AND &
# 4. XOR ^

# Input Variabel
an = False
bn = not an
cn = True
dn = False

# Fungsi NOT
# Output dipastikan antonim dari variabel
print('Jika an=false, dan bn "not" an. Maka bn = ', bn)

# Fungsi OR
# Jika salah satu atau lebih True, maka akan True
print('Jika an=false, dan dn=false. Maka an or dn = ', an | dn)

# Fungsi AND
# Jika salah satu False, maka akan False
print('Jika an=false, dan cn=true. Maka an and cn = ', an & cn)

# Fungsi XOR
# Jika 1 True maka akan True
# Jika True lebih dari 1 maka akan False
print('Jika an=false, dan bn= "not" an. Maka an xor bn = ', an ^ bn)





print('---------------------------IX.Operasi Logika 2---------------------------')

"""inputUser= int(input('Nilai Bilangan yang <12, dan >7 = '))
ilsm = inputUser<=8
ikdm = inputUser>=11
print('I.', inputUser, '< 18,', 'Jawab = ', inputUser <18)
print('II.', inputUser, '> 6,', 'Jawab = ', inputUser >6)
print('III.', inputUser, '<= 8,', 'Jawab = ', ilsm)
print('IV.', inputUser, '>= 11,', 'Jawab = ', ikdm)

print('P1. inputUser <=8')
print('P2. inputUser >=11')

# OR
print('Nilai yang anda masukan memenuhi salah satu dari pernyataan 1 atau 2,', ilsm or ikdm)
# AND
print('Nilai yang anda masukan memenuhi pernyataan 1 dan 2,', ilsm and ikdm)"""





print('------------------------X.Operasi / Operator Biner------------------------')

"""
Format Biner yaitu 8 digit/+
xxxxxxxxxx
9876543210
"""
trt = 82
txt = 3088
tnt = trt and txt
tct = 0b0101010010010
tkt = 0b1001110

# Dalam Biner,
# | diartikan OR
# & diartikan AND
# ^ diartikan XOR
# ~ diartikan NOT

# Konversi Angka ke Biner
print('Angka', trt, 'jika dikonversi ke bilangan biner, menjadi = ', format(trt,"08b"))
print('Angka', txt, 'jika dikonversi ke bilangan biner, menjadi = ', format(txt,"08b"))
print('Angka', tnt, 'jika dikonversi ke bilangan biner, menjadi = ', format(tnt,"08b"))
print('Jika tct =', tct, 'dan tkt =', tkt, 'maka tct^tkt =', tct^tkt)
print('Jika tct =', tct, 'dan tkt =', tkt, 'maka tct^tkt =', format(tct^tkt,"08b"))

print('--------------------------------------------------------------------------------')

ctrl = 1859
ctmn = 274835
ctrs = ctrl is not ctmn
print('Jika CTRL or CTMN, maka =', format(ctrl | ctmn, "08b"))
print('Jika CTRL and CTMN, maka =', ctrl & ctmn)
print('Jika CTRL xor CTMN, maka =', format(ctrl ^ ctmn, "08b"))
print('Jika CTRL not CTMN, maka =', format(ctrl is not ctmn, "08b"))

# SHIFTING BINER
opr = 345580
osr = opr >> 3
orr = opr << 2
print('Diketahui Nilai OPR=345580, jika dikonversi menjadi biner =', format(opr,"08b"))
print('Biner OPR,', format(opr,"08b"), 'jika dishifting ke kanan sebanyak 3, maka =', format(osr,"08b"))
print('Biner OPR,', format(opr,"08b"), 'jika dishifting ke kiri sebanyak 2, maka =', format(orr,"08b"))





print('------------------------XI.Operasi / Operator Assignment------------------------')

# Macam Operator Assignment
# 1.) += digunakan untuk PLUS
# 2.) -= digunakan untuk MINUS
# 3.) *= digunakan untuk PERKALIAN
# 4.) /= digunakan untuk PEMBAGIAN
# 5.) **= digunakan untuk PEMANGKATAN
# 6.) %= digunakan untuk MODULUS
# 7.) //= digunakan untuk PEMBAGIAN dibulatkan ke BAWAH

# 8.) &= digunakan untuk AND
# 9.) ^= digunakan untuk XOR
# 10.) |= digunakan untuk OR
# 11.) <<= digunakan untuk LEFT SHIFTING
# 12.) >>= digunakan untuk RIGHT SHIFTING

a12 = 1080
a13 = 1080
a14 = 1080
a15 = 1080
a16 = 1080
a17 = 1080
a18 = 1080
a19 = 1080
a20 = 1080


print('Diketahui Variabel a12=', a12)
a12 += 140

# 1. Assignment PLUS
print('Jika a12 +=140 maka, a12 menjadi =', a12,'p')
a13 -= 452
# 2. Assignment MINUS
print('Jika a13 -=452 maka, a13 menjadi =', a13,'p')
a14 *= 18
# 3. Assignment PERKALIAN
print('Jika a14 *=18 maka, a14 menjadi =', a14,'k')
a15 /= 3
# 4. Assignment PEMBAGIAN
print('Jika a15 /=3 maka, a15 menjadi =', a15,'p')
# 5. Assignment PEMANGKATAN
a16 **= 3
print('Jika a16 **=3 maka, a16 menjadi =', a16,'p')
a17 %= 13
# 6. Assignment MODULUS
print('Jika a17 %=13 maka, a17 menjadi =', a17,'p')
# 7. Assignment PEMBAGIAN dibulatkan ke BAWAH
a18 //= 12.9
print('Jika a18 //=18 maka, a18 menjadi =', a18,'p')





print('------------------------XII.Operasi Assignment Bitwise------------------------')
i = False
l = True
k = not False
m = not True
i1 = False

print('Diketahui data variabel : i=False, l=True, k=not False. Maka =')
# 8. Assignment AND
# Jika salah satu False, maka akan False
i1 &= m
print('Jika i1 and m, maka =', l)

# 9. Assignment XOR
# Jika 1 True maka akan True
# Jika True lebih dari 1 maka akan False
l ^= k
print('Jika l Xor k, maka =', l)

# 10. Assignment OR
# Jika salah satu atau lebih True, maka akan True
i |= l
print('Jika i or l, maka =', i)

ubw = 902
print('Nilai UBW = 902, jika dikonversi ke biner :', format(ubw,"08b"))
# 11. Assignment LEFT SHIFTING
ubw <<= 3
print('Biner UBW = 902, jika left shifting sebanyak 3, maka menjadi :', format(ubw,"08b"))
ibf = 18001
print('Nilai IBF = 18001, jika dikonversi ke biner :', format(ibf,"08b"))
ibf >>= 4
print('Biner IBF = 18001, jika right shifting sebanyak 4, maka menjadi :', format(ibf,"08b"))




print('-----------------------------XIII.Orientasi String-----------------------------')

# '' dan ""
# Jika print menggunakan '' maka untuk menampilkan petik, gunakan ""

# \
# Digunakan untuk menggonversi elemen setelah \ menjadi string
print('Attempt code 98uhdf7dfk')

# \\
# Digunakan untuk print \ saja
print('juri.ac\\result')

# \t
# Digunakan untuk print TAB 
print('Variabel yang dienskripsi senilai \t18829 pounds')

# \b 
# Digunakan untuk print BACKSPACE
print('Subjek protipe I, dengan kode \b08CGUF7JF')

# \n
# Digunakan untuk print NEWLINE
print('Instruksi dibawah : \nALPHA-BETA-OMEGA')

# \r
# Digunakan untuk print RETURN
print('Rian \rD Masiv')

# \r\n
# Digunakan print RETURN dan NEWLINE
print('Subjek prototipe II, dengan kode \r\n08Vk7dkj500dn')

iss = 98870032873
csi = 988.14
# r'
# Digunakan untuk mengonversi elemen setelahnya menjadi raw string
print("Subjek protptipe III, dengan kode =", iss, "dan raw code =", csi)





print('------------------------------XIV.Manipulasi String------------------------------')
na = 'Budi'
nt = 'Suherman'
nr = 'Sitompul'

# 1. Concatenate (Menggabungkan vaariabel str)
print('Diketahui : \rNama Awal=Budi, Nama Tengah=Suherman, Nama Akhir=Sitompul')
nama_awal = 'Budi'
nama_tengah = 'Suherman'
nama_akhir = 'Sitompul'
nama_lengkap = nama_awal + ' ' + nama_tengah + ' ' + nama_akhir
print('Nama Lengkap =', nama_lengkap)


# 2. Len (Menghitung jumlah fonem)
count_nl = len(nama_lengkap)
print('Jumlah fonem pada', nama_lengkap, 'yaitu :', count_nl)

# 3. In | Not In (Mengetahui keberadaan fonem pada suatu variabel)
randomwordo = ' budi lari bersama andi dikejar reza kecap naik icikiwir ketemu farhan kebab'

check1 = "r" in randomwordo
check2 = "a" in randomwordo

print('Eksistensi fonem "r" pada variabel diatas yaitu :', str(check1))
print('Eksistensi fonem "a" pada variabel diatas yaitu :', check2)


check3 = 'i' not in randomwordo
check4 = 'x' not in randomwordo

print('Eksistensi fonem "i" pada variabel diatas yaitu :', str(check3))
print('Eksistensi fonem "x" pada variabel diatas yaitu :', check4)

print('----------------------------------------------------------------------------------')

# 4. Repeating STR
print('011001'*3)
print(5*'True,False,False')

# 5. Indexing
# Fonem pertama adalah 0
print('Indeks ke 0 dari', nama_lengkap, '=', nama_lengkap[0])
print('Indeks ke 5 dari', nama_lengkap, '=', nama_lengkap[5])
# Dihitung dari belakang
print('Indeks ke -2 dari', nama_lengkap, '=', nama_lengkap[-2])
# Sampling dalam rentang tertentu
print('Indeks ke 4 sampao 13 dari', nama_lengkap, '=', nama_lengkap[4:13])
# Sampling dalam rentang dengan syarat
print('Indeks ke 9 sampai 19 dengan syarat tiap 2 fonem', nama_lengkap, '=', nama_lengkap[9:19:2])

# Min
print('Variabel terkecil dalam', nama_lengkap, '=', min(nama_lengkap))
# Max
print('Variabel terbesar dalam', nama_lengkap, '=', max(nama_lengkap))





print('----------------------------------XV.Ascii Code----------------------------------')
Var2 = ord('s')

print('Ascii code dari "S" =', ord("s"))
print('Ascii code dari "s" =', Var2)

# Konversi Ascii code
sample = 2863
sample2 = 387478

print('Ascii Code untuk', sample, '=', chr(sample))
print('Ascii Code untuk', sample2, '=', chr(sample2))

# INTERMEZZO (COUNT function)
yagiri = 'Black Chain Lifesteal Effect'
kenshin = 'Dominic Spade Execution Sword Rebellion Streetfire'
kenshins = kenshin.count('e')
print('Jumlah karakter "a" pada', yagiri, 'yaitu =', yagiri.count('a'))
print('Jumlah karakter "e" pada', kenshin, 'yaitu =', str(kenshins))

print('------------------------------XVI.Manipulasi STR II (17)------------------------------')
meta = 'verse'
# Upper (Merubah Case)
print('Meta =', meta)
print('Meta di UPPERCASE menjadi =', meta.upper())

neta = 'VeRSe'
# Lower (Merubah Case)
print('Meta di LOWERCASE menjadi =', neta.lower())

# Cek assigned variabel, upper/lower
xeta = 'zeta'
print(xeta, 'merupakan uppercase =', xeta.isupper())
print(xeta, 'merupakan lowercase =', xeta.islower())
# Jika menggunakan concatenate (+) maka perlu casting data ke STR
print(xeta, 'merupakan lowercase ='+ str(xeta.islower()))

print('----------------------------------------------------------------------------------------')

isa = 'tees'
# ISALPHA cek assigned variabel jika alfabet
print('ISA merupakan alfabet =', isa.isalpha())

# Variabel harus STR
isd = '97'
# ISDECIMAL cek assigned variabel jika angka
print('ISD merupakan decimal =', isd.isdecimal())

isan = 'ShadowMonarch1'
# ISALNUM  cek assigned variabel jika alfabet atau huruf
print('ISAN merupakan alfabet/number =', isan.isalnum())

# Capslock di awal huruf
ist = 'The Story Of Shadow Monarch'
# ISTITLE  cek assigned variabel jika alfabet atau huruf
print('IST merupakan title =', ist.istitle())

print('----------------------------------------------------------------------------------------')

# Fonem yang dicari harus disertakan dengan presisi (Upper/Lowercase-nya)
# STARTSWITH untuk cek assigned variabel dimulai dengan ' '
prepeture = 'Blue Cobald Telestrato'.startswith('Blue')
print('prepeture diawali dengan "Blue"=', prepeture)

# ENDSWITH untuk cek assigned variabel diakhiri dengan ' '
propeture = 'Red Kobold Telecaster'.endswith('caster')
print('propeture diakhiri dengan "caster"=', propeture)

print('----------------------------------------------------------------------------------------')

# JOIN menggabungkan fonem yang ada pada suatu variabel
monarch1 = ('Red','Green','Blue')
con1 = ','.join(monarch1)
print(monarch1, 'Jika di concatenate menggunakan rumus join menjadi =', con1)
con2 = ' '.join(monarch1)
print(monarch1, 'Jika di concatenate menggunakan rumus join menjadi =', con2)
con2 = ' and '.join(monarch1)
print(con2)

# SPLIT memisahkan fonem yang ada pada suatu variabel
print(con2, 'Jika di separate menggunakan rumus split menjadi =', con2.split('and'))

print('----------------------------------------------------------------------------------------')

# RJUST meletakan variabel dalam space yang diinginkan, dihitung dari kanan
examp0 = 'Right Corner'.rjust(25)
print('Maka, Right Corner akan diprint dari kanan, dan menjadi :')
print(examp0)

# LJUST meletakan variabel dalam space yang diinginkan, dihitung dari kiri
examp1 = 'Left Corner'.ljust(35)
print('Maka, Left Corner akan diprint dari kiri, dan menjadi :')
print(examp1)

# CENTER meletakan variabel dalam space yang diinginkan, ditengah
# Dapat menyematkan simbol pada command -------x-------
examp2 = 'The Center'.center(52,"-")
print('Maka, The Center akan diprint dari tengah, dan menjadi :')
print(examp2)

# STRIP mengeliminasi bagian yang diinginkan pada suatu variabel
examp2 = 'The Center'.strip('-')
print(examp2)




































