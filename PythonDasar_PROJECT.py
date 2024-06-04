import os
import CRUD as CRUD
import CRUD.Operasi

# ---------------------------------------------------------------------Python Chapter 67-71------------------------------------------------------------------------

print(f'''




{155*'-'}''')
print('-----------------------------------------------------------------6[VII] Set Up Project (67)------------------------------------------------------------------')
print(155*'-')

print(f'''




{155*'-'}''')
print('-------------------------------------------------------------6[VIX] Init Database dan Read (68)---------------------------------------------------------------')
print(155*'-')

print(f'''




{155*'-'}''')
print('----------------------------------------------------------------------7[0] Update (70)------------------------------------------------------------------------')
print(155*'-')

print(f'''




{155*'-'}''')
print('----------------------------------------------------------------------7[1] Delete (71)------------------------------------------------------------------------')
print(155*'-')


if __name__ =='__main__' :

    operations = os.name

    match operations :
            case 'posix' : os.system('clear')
            case 'nt'    : os.system('cls')
         
    print(f'1. Read Data')
    print(f'2. Create Data')
    print(f'3. Update Data')
    print(f'4. Delete Data\n')

    # Check Database ada atau tidak
    CRUD.init_console()


    while(True) :
        match operations :
            case 'posix' : os.system('clear')
            case 'nt'    : os.system('cls')

        print(f'{80*'-'}Database  Lagu{80*'-'}')
        print(174*'-')

        print(f'1. Read Data')
        print(f'2. Create Data')
        print(f'3. Update Data')
        print(f'4. Delete Data\n')

        user_path = input('Pilih opsi di atas = ')

        

        match user_path :
            case '1' : CRUD.read_console()
            case '2' : CRUD.create_console()
            case '3' : CRUD.update_console()
            case '4' : CRUD.delete_console()

        
        ncase = input('Keluar dari Program? (Y/N) = ')
        if ncase == 'Y' or ncase == 'y' :
            break

print(f'{78*'-'}Akhir dari Program{78*'-'}')
