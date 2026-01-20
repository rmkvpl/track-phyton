# TODO Найдите количество книг, которое можно разместить на дискете
a = 100
b = 50
c = 24
m = 1.44
byt = 4

symbols1 = a * b * c
bytes1 = symbols1 * byt
diskette = m * 1024 * 1024
kol = int(diskette // bytes1)
print("Количество книг, помещающихся на дискету:", kol)
