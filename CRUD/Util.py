import random
import string


def random_string(panjang:int) -> str :
     strgen = ''.join(random.choice(string.ascii_letters) for i in range(panjang))
     return strgen

# def random_string2(panjang2:int) -> str :
#     strgen2 = ''.join(random.choice(string.ascii_letters) for i in range(panjang2))
#     return strgen2

# def random_string3(panjang3:int) -> str :
#     strgen3 = ''.join(random.choice(string.ascii_letters) for i in range(panjang3))
#     return strgen3