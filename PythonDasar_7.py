# ----------------------------------------------------Python Chapter 38-42-------------------------------------------------------


print(f'''




{149*'-'}''')
print('-------------------------------------------------------XXXVIII. Dictionary (38)--------------------------------------------------------')
print(149*'-')

# LIST ---> ARRAY
# Bentuk Identitas : INDEX

print(f'1. Data LIST (menggunakan INDEX)')

samlist = ('Blue', 'White', 'Black')
print(f'   Diketahui data SAMLIST : {samlist}')

print(f'    1. Ocean seems so {samlist[0]}')


print(149*'-')


# DICTIONARY ---> ASSOCIATIVE ARRAY
# Bentuk Identitas : KEY

print(f'2. Data DICTIONARY (menggunakan KEY)')

samdict = {
    'cb' : 'Cobold',
    'cp' : 'Champion',
    'kn' : 'Knight',
    'pd' : 'Paladin',
    'ep' : 'Emperor'
}
# DICTIONARY support tipe data : str, bool, int, float, hex, list

print(f'   Diketahui data SAMDICT : {samdict}')

print(f'    2. Igris when first meet Ranked as {samdict['kn']}')





print(f'''




{149*'-'}''')
print('-------------------------------------------------------XXXIX. Operasi Dictionary (39)--------------------------------------------------------')
print(149*'-')

bops = {
    'g' : 'Ghost',
    'y' : 'Yansil',
    'z' : 'Zogratis'
}
print(f'Diketahui Dictionary BOPS : {bops}')

print(149*'-')

# 1. Operasi LEN
print('1. Operasi LEN')
LENBOPS = len(bops)
print(f'     I Panjang Dictionary BOPS = {LENBOPS}')

print(149*'-')

# 2. Operasi measure DATA dalam DICTIONARY
print('2. Measure data dalam Dictionary')
Y = 'y'
ASKY = Y in bops
print(f'    II Apakah "Yansil" ada dalam BOPS : {ASKY}')


# 3. Operasi GET dalam Dictionary
print('3. Pick UP data dalam Dictionary')
print(f'     -Data g dalam BOPS : {bops['g']} (Cara Umum)')
print(f'     -Data g dalam BOPS : {bops.get('g')} (Cara GET)')

print(149*'-')

print(f'{48*'-'}Jika mencari Variabel yang tidak ada dalam Dictionary{48*'-'}')

print(149*'-')

print(f'     -Data U dalam BOPS : {bops.get('U')}                 (Cara GET)')
print(f'     -Data U dalam BOPS : {bops.get('U','Key tidak ada')} (Cara GET)')

print(149*'-')

# 4. Operasi EXCHANGE dalam Dictionary
print('4. Exchange data dalam Dictionary')
bops['y'] = 'Yudi'
print(f'   III Dict BOPS setelah diganti = {bops}')

print(149*'-')

# 5. Add On DATA dalam Dictionary
print('5. Add ON Data dalam Dictionary')
bops['u'] = 'Ultimatia'
print(f'    IV Dict BOPS setelah ditambahkan = {bops}')

print(149*'-')

# 6. Update DATA dalam Dictionary
print('6. Update Data dalam Dictionary')
bops.update({'yan': 'Yan Suran'})
print(f'     V Dict BOPS setelah Update Variabel yang tidak ada = {bops}')

print(149*'-')

# 7. Delete DATA dalam Dictionary
print('6. Delete Data dalam Dictionary')
del bops['yan']
print(f'     VI Dict BOPS setelah Mendelete variabel yan = {bops}')

print(149*'-')






print(f'''




{149*'-'}''')
print('-----------------------------------------------------------XXXX. Looping Dictionary (40)------------------------------------------------------------')
print(149*'-')


# 1. 2024 World Map Data
obj01 = {
    'Th':'Inazuma',
    'Oc':'Fontaine',
    'Mo':'Mondstadt',
    'Li':'Liyue',
    'Na':'Sumeru'
}

# 1. Metode Looping ALL KEYS (1)
print(f'1. Metode Looping ALL KEYS (1)')
for obj in obj01 :
    print(f'   I.  Variabel yang ada pada Dict OBJ01 = {obj01}')
    
print(149*'-')

# 2. Metode Looping KEY, ITEM / ITTERABLES KEYS (2)
print(f'2. Metode Looping KEY, ITEM / ITTERABLES KEYS (2)')
objedit = obj01.keys()
print(f'   II.  KEY item yang ada pada Dict OBJ01 = {objedit}')

for o in obj01.keys() :
    print(f'     {obj01.get(o)}')

print(149*'-')

# 3. Metode Looping VAR dalam KEY (3)
print(f' 3. Metode Looping VAR dalam KEY (3)')
objvar = obj01.values()
print(f'   III.  Item-item yang ada pada Dict OBJ01 = {objvar}')

for i in obj01.values() :
    print(f'         > Item-item yang ada pada Dict OBJ01 = {i}')

print(149*'-')

# 4. Metode Looping ITEM (key dan variabel) (4)
print(f' 4. Metode Looping ITEM (key dan variabel) (4)')

objtems = obj01.items()
print(f'   IV.  Items yang ada pada Dict OBJ01 = {objtems}')

for u in obj01.items() :
    print(f'         > Items yang ada pada Dict OBJ01 = {u}')

print(149*'-')

# 5. Metode Looping KEY dan VARIABEL
print(f' 5. Metode Looping KEY dan VARIABEL Items (5)')

for o, u in obj01.items() :
    print(f'     Key = {o}, Items = {u}')

print(149*'-')





print(f'''




{149*'-'}''')
print('------------------------------------------------------------XXXXI. Copy Dictionary (41)-------------------------------------------------------------')
print(149*'-')

# 1. Copy Dictionary
print('1. Copy Dictionary')

print(149*'-')

entry0 = {
    '7':'Islet',
    '8':'N-Buna',
    '9':'Yuiko Ohara',
    '10':'Eve'
}

# Gunakan .copy agar ID dari Dictionary berbeda dan dapa dimanipulasi Variabelnya tanpa mempengaruhi Dictionary lainya
entryzero = entry0

print(f'   X. Key dan Variabel pada ENTRY0 = {entry0}')

print(149*'-')

print(f'   X. Key dan Variabel pada ENTRYZERO = {entryzero}')

print(149*'-')


entry0['8'] = 'Sawano Hiroyuki'


print(f'   X. Key dan Variabel pada ENTRYZERO = {entryzero}')

print(149*'-')
print(f'   X. Key dan Variabel pada ENTRY0 = {entry0}')

print(149*'-')


# 2. Pop (Transfer Data) Dictionary
print('2. Pop (Transfer Data) Dictionary')

print(149*'-')

Sawano = entry0.pop('8')

print(f'   X. Key dan Variabel pada SAWANO = {Sawano}')

print(149*'-')

print(f'   X. Key dan Variabel pada ENTRY0 = {entry0}')

print(149*'-')


# 3. PopItem (Transfer Data terakhir) Dictionary
print('3. PopItem (Transfer Data Terakhir) Dictionary')

popentry = entry0.popitem()

print(f'   X. Output dari popitem ENTRY0 = {popentry}')
      
print(149*'-')

print(f'   X. Key dan Variabel pada ENTRY0 = {entry0}')

print(149*'-')






print(f'''




{149*'-'}''')
print('---------------------------------------------------XXXXII. Multi Key dan Nesting Dictionary (42)----------------------------------------------------')
print(149*'-')

import datetime

# 1. Dictionary Biodata

sub0 = {
    'Name'   : 'Roger Sumatra',
    'Born'   : datetime.datetime(1792,10,20),
    'Age'    : 328,
    'Class'  : 'Keter',
    'Hunted' : True
}

print(f'1. Dictionary Roger Sumatra  = {sub0}')

sub1 = {
    'Name'   : 'Herman Ujung Kulon',
    'Born'   : datetime.datetime(1650,2,10),
    'Age'    : 438,
    'Class'  : 'Fluid',
    'Hunted' : True
}

sub2 = {
    'Name'   : 'Sigit Rendang',
    'Born'   : datetime.datetime(1512,7,13),
    'Age'    : 488,
    'Class'  : 'Safe',
    'Hunted' : False
}


subject = {
    'ZERO001'  : sub0,
    'ZERO002'  : sub1,
    'ZERO003'  : sub2
}

print(149*'-')

print(f'2. Data Subjek Pengamatan = {subject}')

print(149*'-')

print(f'{'Key':<16} {'Name':<36} {'Age':<24} {'Class':<18} {'Status':<18} {'Born':<42}')
print(149*'-')

for subjek in subject :
    KEY         = subjek
    NAME        = subject[KEY]['Name']
    AGE         = subject[KEY]['Age']
    CLASS       = subject[KEY]['Class']
    STATUS      = bool(subject[KEY]['Hunted'])
    BORN        = subject[KEY]['Born'].strftime('%x')

    print(f'{KEY:<16} {NAME:<36} {AGE:<24} {CLASS:<18} {STATUS:^8} {BORN:^28}')
print(149*'-')