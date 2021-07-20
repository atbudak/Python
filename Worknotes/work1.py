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
