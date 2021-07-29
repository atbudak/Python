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

num1 = float(input("Number 1 : "))
num2 = float(input("Number 2 : "))

if num1 > num2:
    print(f"The large number is {num1}")
elif num1 == num2:
    print(f"Both number is equal : {num2}")
else:
    print(f"The large number is {num2}")

age = input('Please Enter your age :')
while not age.isdigit():
    age = input('Wrong Entrance')
if age.isdigit():
    print(age + " is your age")

guess = input('Enter a Number? ').strip()

# while not (int(guess) == 33 and guess.isdigit()) de yazılabilir
while True:
    if int(guess) > 33:
        print("Little lower")
    elif int(guess) < 33:
        print("Little high")
    else:
        print("Congrats!!")
        break
    guess = input('Number? ').strip()

# adding - after words
word = "clarusway"
count = 0
for i in word:
    count += 1
    if count < len(word):
        i += '-'
    print(i, end='')

# dictionery leri itarate ettiğimizde key leri iterate eder
user = {
    'name': "Dan",
    'surname': 'Wards',
    'age': 42
}
for i in user:
    print(i)

for key1, value2 in user.items():
    print(key1, ':', value2)

for i in range(1, 10):
    print(str(i)*i)

# even-odd
# how to add element inside for loop
even = []
odd = []
for i in range(1, 10):
    if i % 2 == 0:
        even.append(i)
    else:
        odd.append(i)
print('even :', even)
print('odd  :', odd)

example_list = [11, 2, 24, 61, 48, 33, 3]
odd = 0
even = 0
for i in example_list:
    if i % 2:
        even += 1
    else:
        odd += 1

print('odd: ', odd, 'even: ', even)
