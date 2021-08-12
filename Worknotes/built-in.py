# built-in functions
li = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print("-------------------------- map() --------------------------")
# we can apply every element of iterator the same
# function or we can convert each element in to
# str, int, bool, float etc.

# converting int to str
print(list(map(str, li)))
# as a function
print(list(map(lambda x: x ** 2, li)))
print("-------------------------- filter() -----------------------")
# filtering out elements based on pre defined func
# we can use this func with map
# Filter(None,list-name) if func. place is None it takes
# only True arguments in collections


def isOdd(x):
    return x % 2 != 0


# b = list(filter(isOdd, li))
c = list(map(lambda x: x + 7, filter(isOdd, li)))
print(c)
print("-------------------------- Lambda -------------------------")
# it takes less space then def in computer also
# we can write definition as long as one line
# help us to use multiple func inside each other
# anonymous, not callable function

def func1(x):
    func2 = lambda x, y=21: x + y
    return func2(x) + 21


print(func1(1))
print("-------------------------- zip() --------------------------")
# make an iterator that aggregtes elements from
# each of the iterable
# uzunluğu kısa olan listenin uzunluğuna kadar birleştirir
text = ['bir', 'iki', 'üç', 'dört', 'beş', 'altı']
numbers = [1, 2, 3, 4, 5, 6, 7]
print(list(zip(text, numbers)))
print("-------------------------- extend() -----------------------")
# append collections with each other
# with append we add inside list as a one element
# with extend we add inside of list as long as extended list
L1 = []
L1.append([1, [2, 3], 4])
L1.extend([7, 8, 9])
print(L1)  # we can check extend and append here
print(L1[0][1][1] + L1[2])
print("-------------------------- sum() --------------------------")
print("-------------------------- super() ------------------------")
print("-------------------------- next() -------------------------")
print("-------------------------- hash() -------------------------")
print("-------------------------- format() -----------------------")
print("-------------------------- enumerate() --------------------")
# takes 2 parameter start and iterator
grocery = ['bread', 'water', 'olive']
enum_grocery = enumerate(grocery)
print(type(enum_grocery))
print(list(enum_grocery))
enum_grocery = enumerate(grocery, 10)
print(*enum_grocery)
print("-------------------------- memoryview() -------------------")
print("-------------------------- pow() --------------------------")
print("-------------------------- repr() -------------------------")
print("-------------------------- strip() ------------------------")
print("-------------------------- round() ------------------------")
print("-------------------------- abs() --------------------------")
print("-------------------------- dir() --------------------------")
print("-------------------------- clear() ------------------------")
print("-------------------------- eval() -------------------------")
print("-------------------------- max() --------------------------")
print("-------------------------- min() --------------------------")
print("-------------------------- open() -------------------------")
print("-------------------------- next() -------------------------")
print("-------------------------- reversed() ---------------------")
print("-------------------------- setattr() ----------------------")
print("-------------------------- @staticmethod() ----------------")
print("-------------------------- globals() ----------------------")
print("-------------------------- callable() ---------------------")
print("-------------------------- bytes() ------------------------")
print("-------------------------- bytearray() --------------------")
print("-------------------------- bin() --------------------------")
print("-------------------------- any() --------------------------")
# eğer collection type larda 1 tane bile True var ise any()
# True değer döndürür. True var mı yok mu kontrol için
names1 = ["ahmet", 0, False]
mood1 = [None, {}, 0]
empty1 = {}
print(any(names1), any(mood1), any(empty1))
print("-------------------------- all() --------------------------")
# collection içi boş yada false item yoksa true döndürür
# False bir değer varsa false döndürür
names = ["ahmet", "mehmet", "recep"]
mood = ["happy", "sad", 0]
empty = {}
print(all(names), all(mood), all(empty))
