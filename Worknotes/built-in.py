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


def isOdd(x):
    return x % 2 != 0


# b = list(filter(isOdd, li))
c = list(map(lambda x: x + 7, filter(isOdd, li)))
print(c)
print("-------------------------- Lambda -------------------------")
# it takes less space then def in computer also
# we can write definition as long as one line
# help us to use multiple func inside each other


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
print("-------------------------- super() ------------------------")
print("-------------------------- hash() -------------------------")
print("-------------------------- format() -----------------------")
print("-------------------------- enumerate() --------------------")
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
print("-------------------------- all() --------------------------")
