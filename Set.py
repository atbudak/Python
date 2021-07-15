# Pre Class

# .add() : Adds a new item to the set.
# .remove() : Allows us to delete an item.
# .intersection() : Returns the intersection of two sets.
# .union() : Returns the unification of two sets.
# .difference() : Gets the difference of two sets.

a = set('abracadabra')  # aynı harfleri vermedi
print(a)

a = set('abracadabra')
b = set('alacazam')

print(a - b)  # same as '.difference()' method
print(a.difference(b))  # a difference from b

print(a | b)  # same as '.union()' method
print(a.union(b))  # unification of a with b

print(a & b)  # same as '.intersection()' method
print(a.intersection(b))  # intersection of a with b

# Additionally we can
# Get the number of set’s elements using len() function,
# Check if an element belongs to a specific set(in / not in operators), you get the boolean value.
print(len(set('listen to the voice of enlisted')))

# Lesson Notes

# sets takes only iterables

letter = "a b c d e f g h i j k l m n o p q r s t u x w v z".split()
print(set(letter))

# İçeriği farklı fakat eşiler
a = {'carnation', 'orchid', 'rose', 'violet'}
b = {'rose', 'orchid', 'rose', 'violet', 'carnation'}
print(a == b)

frst = set('philadelphia')
sec = set('dolphin')
print("İki kümenin Kesişimi: ", frst.intersection(sec))
print("İki kümenin farkı: ", frst.difference(sec))
print("İki kümenin birleşimi: ", frst.union(sec))

date = {"12/07/2021"}
date1 = set("12/07/2021")
print(date, date1)

given_list = [1, 2, 3, 3, 3, 3, 4, 4, 5, 5]
# test = {given_list}  Hata verir
test = set(given_list)
print(test)
# Collection type'ları set e çeviremiyor

