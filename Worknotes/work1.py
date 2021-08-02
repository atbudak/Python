# Önemli bilgiler
items = (10, 20)
x, y = items
print("tuple iki değere atma : ", x, y)

a, _, b, _ = (10, 20, 30, 40)
print(a, b)

x, y, *z = (11, 22, 33, 44, 55, 66, 77)
print("2 değerden sonrasını listeye alma :", z)

c, z, *_ = (11, 22, 33, 44, 55, 66, 77, 88, 99)
print("ilk iki değeri alma : ", _)

t, k, *l, m = (11, 22, 33, 44, 55, 66, 77)
print("aradaki değerleri alma : ", l)

empty = []
print(max(empty, default="boş"))
# list boş olması durumunda default içeriğini verir

# Enumarate
para = 1000
gunluk_kazanc = enumerate([para * 1.07 ** i for i in range(1, 8)], 1)
print(list(gunluk_kazanc))

print(*'seperate')

# 2. sırada bulunan liste elemanı 1. listedeki belirtilen
# index'teki liste elemanların uzunluğunu verir
print(len([[12, 34, 56], [2, 4, 5, 5], [3, 2]][1]))

generate = (i**2 for i in range(12))
print(*generate)
# *generate ile içeriği sergiledik daha sonra generate'in
# içi boşaldı, aşağıdaki boş verir. doldurulmuş değişkeni
# 1 kere kullanabiliriz. for döngüsü ile kullanılan/yazdırılan
# collection type değişkeni 2. kez kullanılamaz
for i in generate:
    print(i)

