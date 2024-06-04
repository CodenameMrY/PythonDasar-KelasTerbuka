# ----------------------------------------------------Python Chapter 18-21-------------------------------------------------------

print('Hello World')

print(80*'-')
print('------------------------------XVII.Formatting (18)------------------------------')
print('-----------------------------------PENTING--------------------------------------')
# Opsi Typing 1
# Wajib menggunakan '+' bukan ','
idn = 'Budi'
idn1 = idn + ' Santoso' + ' Sutresno' + ' Sulastri'
print(idn1)

'''KHUSUS STR'''

print('---------------------------------------------------------------------------------')
# 1. Formatting STR
# Opsi Typing 2 (Formatting)
ifn = 'Jordi'
ifn1 = f'{idn} Tordi Simulasikan Sendtri'
print(ifn1)

# 2.A Formatting INT / FLOAT
intf = 508.85
intf1 = f'1. Nilai dari INTF = {intf}'
print(intf1)

# 3. Formatting BOOLEAN
bolf = False ^ True
bolf1 = f'2. Nilai dari BOLF = {bolf}'
print(bolf1)

# 4. Formatting ',' dalam angka
tou = 3289400020
touf = f"3. Variabel TOU senilai = {tou:,}"
print(touf)

# 5. Formatting FLOAT berdasarkan jumlah bilangan yang diinginkan dibelakang koma
sourcef = 70030.5125
sourcef1 = f'4. Variabel SOURCEF jika hanya diambil 2 bilangan dibelakang koma = {sourcef:.2f}'
print(sourcef1)

# 6. Formatting Leading Zero
sourcef0 = 70030.5125
sourcef2 = f'5. Variabel SOURCEF jika hanya diambil 2 bilangan dibelakang koma = {sourcef0:12.3f}'
print(sourcef2)
# JKA INGIN MENYEMATKAN BILANGAN 0 PADA BARIS KOSONG VARIABEL TAMBAHKAN 0 PADA {sourcef0:012.3f}

# 7. Formatting (+) atau (-)
sc00 = -2050
sc01 = +12010
scf00 = f'6. Nilai SC00 = {sc00}'
scf01 = f'7. Nilai SC01 = {sc01:+}'
# WAJIB MENYEMATKAN (+) AGAR DAPAT DITAMPILKAN
print(scf00)
print(scf01)

# 8. Formatting PERCENT
pccode = 0.0152
pccodef = f'8. Nilai persen dari PCCODE = {pccode:.2%}'
print(pccodef)

# PENTING
# 9. Operasi Aritmetika dalam FORMATTING
subjectx = 13
subjecty = 28500
subjectxy = f'9. Income penjualan = Rp.{subjectx*subjecty:,}'
print(subjectxy)

print('---------------------------------------------------------------------------------')

# 10. Formatting LAINYA
various = 20302
fbiner = f'10. Nilai Biner dari VARIOUS = {bin(various)}'
foctal = f'11. Nilai Octa dari VARIOUS = {oct(various)}'
fhex = f'12. Nilai Hex dari VARIOUS = {hex(various)}'

print(fbiner)
print(foctal)
print(fhex)





print(80*'-')
print('----------------------XVIII.OPERASI WIDTH dan ALIGNMENT (19)----------------------')
print(80*'-')



# Diketahui Data :
assign_user = 'Sean'
assign_umur = '21'
assign_tinggi = '178 cm'
assign_bb = '72 kg'

# METODE 1
input1 = f'Data yang diketahui : 1.Nama = {assign_user} 2.Umur = {assign_umur} 3.Tinggi = {assign_tinggi} 4.BB = {assign_bb}'
print(input1)

print(22*'-', 'Jika menggunakan NEWLINE (enter)', '-'*22)

# Metode 2 dengan \n (enter)
input1 = f'Data yang diketahui : \n1.Nama = {assign_user} \n2.Umur = {assign_umur} \n3.Tinggi = {assign_tinggi} \n4.BB = {assign_bb}'
print(input1)

# Metode 3 dengan multiline (triplets)
a2_user = 'I) Nama   = Rendi'
a2_umur = 'I) Umur   = 20'
a2_tinggi = 'I) Tinggi = 176 cm'
a2_bb = 'I) BB     = 70 kg'

print(80*'-')

input2 = f"""
Diketahui Data lainya :
{a2_user}
{a2_umur}
{a2_tinggi}
{a2_bb}
"""
print(input2)

print(80*'-')
print(' ')
# REPOSISI VARIABEL dengan catatan tidak menambahkan STR pada variabel, tambahkan saat FORMATTING
si0 = 'I15233210'
si1 = f"""ID = {si0:>12}
"""
si2 = f"""ID = {si0:<12}
"""
print('ID =', si0)
print(si1)

print(80*'-')





print(80*'-')
print('-----------------------------XIX.Date and Time (20)-----------------------------')
print(80*'-')

# Date and Time Library

import datetime as dt
today = dt.date.today()
birth = dt.date(2005,4,14)

print(today)
print(birth)

# Mengetahui Hari dengan menggunakan %A
print(today, f',Pada tanggal tersebut, hari = {today:%A}')
print(birth, f',Pada tanggal tersebut, hari = {birth:%A}')



print(80*'-')
print('Masukkan Data Kelulusan anda dengan benar :')
tgl = int(input('Tanggal Kelulusan    = '))
bln = int(input('Bulan Kelulusan      = '))
thn = int(input('Tahun Kelulusan      = '))

waktu_kelulusan = dt.date(thn, bln, tgl)
print('Waktu Kelulusan anda =', waktu_kelulusan)
print(f'Hari kelulusan anda  = {waktu_kelulusan:%A}')

cn = today - waktu_kelulusan
cny = cn.days / 365
print(f'Countdown kelulusan anda, dalam = {cn}')
print(f'Countdown kelulusan anda, dalam = {cny:.0f} Tahun')


print(80*'-')

print('Masukkan Data Kelahiran anda dengan benar :')
tgl2 = int(input('Tanggal Lahir        = '))
bln2 = int(input('Bulan Kelahiran      = '))
thn2 = int(input('Tahun Kelahiran      = '))

waktu_kelahiran = dt.date(thn2, bln2, tgl2)
print('Waktu kelahiran anda = ', waktu_kelahiran)

us = today - waktu_kelahiran
usy = us.days / 365
print(f'Umur saya dalam = {us}')
print(f'Umur saya dalam = {usy:.0f} Tahun')





print(80*'-')
print('-----------------------------XX.IF dan ELSE statement (21)-----------------------------')
print(80*'-')

'''
1. (IF) Pernyataan / Kondisi
2. Aksinya
'''

# 1.IF in Line
mbti1 = input('1. Kelas MBTI anda = ')

if mbti1=='INTJ' : print('>  Anda seorang Introvert Intuitive Thinking Judging')
print('Terima kasih telah menjawab')
print(80*'-')

# 2. IF with Indentation (Indentasi)
egram1 = input('2. Ennegram anda = ')
if egram1=='1w9' : 
    print('>  Anda rasional dan perfeksionis')
    print('>  Anda berorientasi pada proses dan optimis')
print('Terima kasih telah menjawab')
print(80*'-')

# 3. Else Statement
tri1 = input('3. Tritype anda = ')
if tri1=='153' :
    print('>  Kamu Dedicated dan bertekad')
else :
    print('>  Sayangnya tritype anda bukan 153')
print('Terima kasih telah menjawab')
print(80*'-')

print(80*'-')