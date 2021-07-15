# Pre Class
# Conditional Statements

# If you need to remember the result of a condition check
# later in your code, use boolean variables as flags

gpa, lowest_grade = .9, .7
if gpa >= .85 and lowest_grade >= .7:
    honor_role = True
else:
    honor_role = False
# Somewhere later in our code
if honor_role:
    print('Well Done')

# Loops

# * before range() function to separate its elements
# * can separate other iterable objects
print(range(5))  # it will not print the numbers in sequence
print(*range(5))  # '*' separates its elements

# In some cases, you will need to set up
# the for loop with multiple variables and the iterables.
text = ['one', 'two', 'three', 'four', 'five']
numbers = [1, 2, 3, 4, 5]
for x, y in zip(text, numbers):
    print(x, ':', y)

# zip() function make an iterator that aggregates
# elements from each of the iterables.

# Lesson Notes

# String değerlerde ilk karakterin ASCII karşılıklarını karşılaştırır
value1 = '2020'
if value1 >= '1200':
    print('string values checks by first value')

# boolean değer aldık kullanıcıdan
convert = input("yes or no ? ").title().strip() == 'Yes'
print(convert, type(convert))


num = int(input("Enter a number: ").strip())
if num % 2 == 0:
    print(f"{num} is even")
else:
    print(f"{num} is odd")
