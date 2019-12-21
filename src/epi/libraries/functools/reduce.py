import functools

a = lambda x,y: x+y
print(a(1,2))

print('\n')

print(
    functools.reduce(
        lambda x,y: x+y,
        [' ','Mukund',' ', 'Deshpande'],
        ""
))


modulus = 2000

mul = 997

for s in ["anirudh", "mukund", "deshpande", "Anirudh", "anirudh", "zz", "zzz", "zzzz", "zzzzz", "zzzzzz", "zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz"]:
    print(
        functools.reduce(lambda v,c: (v*mul + ord(c)) % modulus, s, 0)
    )
