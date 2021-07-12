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

# Additionally we can
# Get the number of set’s elements using len() function,
# Check if an element belongs to a specific set(in / not in operators), you get the boolean value.
print(len(set('listen to the voice of enlisted')))
