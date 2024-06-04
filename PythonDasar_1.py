print('-----------------I.FUNGSI PRINT DASAR-----------------')
#I. Fx-Print dasar
print('Hello World')

"""Menginput suatu value"""
x = 122
k = 23
print('Nilai x=122, k=23 nnilai x+k=', x+k)

Nama = 'Johan'
Marga = 'Liebert'
#Gunakan petik jika nilai variabel string
#Menghubungkan variabel melalui print
print('Nama Lengkap =', Nama, Marga)




print('---------------II.REWRITE NILAI VARIABEL---------------')
#II. Rewrite Nilai Data / Assignment Indirect
Nama = 'Joanna'
Marga = 'Steinburg'
#Mengubah nilai suatu variabel(Updated)
print('Nama lengkap anda (orang kedua) =', Nama + " " + Marga)



print('---------------------III.Tipe Data---------------------')
#III. Tipe data (4 jenis)
"""1. Int / Integer yaitu data angka yang bulat
   2. Float / Desimal yaitu data angka berkoma
   3. Str / String yaitu data karakter berupa huruf
   4. Bool / Boolean yaitu tipe data yang menyatakan true/false"""
#0 JIKA DIKONVERSI KE BOOL MENJADI FALSE

aku_int = 1788
print('Data Integer (INT) =', aku_int, type(aku_int))
aku_float = 0.759
print('Data Float (FLOAT) =', aku_float, type(aku_float))
aku_str = "Jordyi"
print('Data Integer (STR) =', aku_str, type(aku_str))
aku_bool = False
print('Data Integer (BOOL) =', aku_bool, type(aku_bool))



print('-------------IV.Konversi Data berbagai tipe-------------')
#STR ke BOOL
stering1 = "Budi"
print('Data String "Budi" jika dikonversi ke BOOL=', bool(stering1), type(bool(stering1)))
#STR ke INT
stering2 = 9173
print('Data String "917423" jika dikonversi ke INT=', int(stering2), type(int(stering2)))
#STR ke FLOAT
stering3 = 784.34
print('Data String "784.34" jika dikonversi ke INT=', float(stering3), type(float(stering3)))
      

#Jika Data 0 dikonversi ke BOOL maka menjadi false
#INT ke BOOL
intrejer1 = 0
print('Data INT "17736" jika dikonversi ke BOOL=', bool(intrejer1), type(bool(intrejer1)))
#INT ke STR
intrejer2 = 102090
print('Data INT "102090" jika dikonversi ke STR=', int(intrejer2), type(str(intrejer2)))
#INT ke FLOAT
intrejer3 = 784
print('Data INT "784.34" jika dikonversi ke FLOAT=', float(intrejer3), type(float(intrejer3)))



print('--------------------V.Input User Data--------------------')
#Input User String
Nama_Perusahaan = input('Nama Perusahaan = ')
print('Nama Perusahaan =', Nama_Perusahaan, '|Tipe Data :', type(Nama_Perusahaan))
#Input User INT
Umur_Perusahaan = int(input("Umur Perusahaan = "))
print('Umur Perusahaan =', Umur_Perusahaan, '|Tipe Data :', type(Umur_Perusahaan))
#Input User FLOAT
Indeks_Perusahaan = float(input('Indeks Perusahaan = '))
print('Indeks Perusahaan =', Indeks_Perusahaan, '|Tipe Data :', type(Indeks_Perusahaan))
#Input User BOOLEAN 
Operasional_Perusahaan = bool(input('Status Operasional Perusahaan = '))
print('Status Operasional Perusahaan =', Operasional_Perusahaan, '|Tipe Data :', type(Operasional_Perusahaan))



print('--------------------VI.Komputasi Operasi Aritmetika--------------------')
a = 12
b = 2
plus = a+b
minus = a-b
half = a/b
point = a*b
two = a**b
modu = a%b
#Penjumlahan +
print('Jika a=12, b=2, maka', a, '+', b, '=', plus)
#Pengurangan -
print('Jika a=12, b=2, maka, a-b =', minus)
#Perkalian *
print('Jika a=12, b=2, maka, a*b =', point)
#Pembagian /
print('Jika a=12, b=2, maka, a/b =', half)
#Pemangkatan, Eksponen **
print('Jika a=12, b=2, maka, a**b =',two)
#Pembagian Bersisa, Modulus %
print('Jika a=12, b=2, maka, a%b =', modu)

#Prioritas
# 1. () kurungan
# 2. Pemangkatan, Eksponen
# 3. Perkalian *
# 4. Pembagian /
# 5. Penjumlahan + | Pengurangan -



print('--------------------VI.Operasi Komparasi--------------------')
"""
Tanda yang Digunakan :
1. >
2. <
3. >=
4. <=
5. ==
6. !=
7. is
8. is not
"""

alpha = 12010
beta = 722
teta = 722
# > lebih kecil dari
print('Jika alpha=12010, dan beta=722 maka : alpha > beta =', alpha>beta)
# < lebih besar dari
print('Jika alpha=12010, dan beta=722 maka : alpha < beta =', alpha<beta)
# >= lebih kecil dari sama dengan
print('Jika beta=722, dan teta=722 maka : beta >= teta =', beta>=teta)
# <= kurang dari sama dengan
print('Jika alpha=12010, dan teta=722 maka : alpha <= teta =', alpha<=teta)
# == sama dengan
print('Jika beta=722, dan teta=722 maka : beta == teta =', beta==teta)
# != tidak sama dengan
print('Jika beta=722, dan teta=722 maka : beta != teta =', beta!=teta)


# IS digunakan untuk membandingkan nilai variabel/objek
# IS NOT digunakan untuk membandingkan literal

# IS statement
x=18
y=9
z=x is y
print('x=18 dan y=9')
print('Nilai x is y =', z)
print('Nilai x is not y =', x is not y)



print('-----------------VII.ID variabel dan Hexadecimal-----------------')
#Fungsi id(x), digunakan untuk mengetahui id objek/variabel
#Fungsi hex(id(x)), digunakan untuk mengonversi id ke hexadecimal

j=178
k=76237915
l='SUPEERYAN'
m='Brody'
n=1982.25
print('Dibawah ini variabel dan ID nya secara berturut-turut :')
print(j, '=' , id(j))
print(k, '=' , id(k))
print(l, '=' , id(l))
print(m, '=' , id(m))
print(n, '=' , id(n))

print('--------------------------------------------------------------------')

print('Dibawah ini variabel dan Hexadecimal nya secara berturut-turut :')
print(j,'=' , hex(id(j)))
print(k,'=' , hex(id(k)))
print(l,'=' , hex(id(l)))
print(m,'=' , hex(id(m)))
print(n,'=' , hex(id(n)))


