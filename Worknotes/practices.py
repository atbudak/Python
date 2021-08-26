import math
import random
from timeit import timeit, repeat
# List Comprehensions
# Start
liste = [i for i in range(5)]
print(liste)

# Ternary if Statements
trn = [i for i in range(12) if i % 2]
print(trn)

condition = True
a = "Cond is True" if condition else 0
print(a)
# End
# time calculator
# Start
sec = input('Please enter second:')

if not sec.strip().isdigit():
    result = f'{sec} is not decimal number!!'
else:
    sec = int(sec)
    h, m, s = (sec // 3600), (sec % 3600) // 60, (sec % 3600) % 60
    result = f'{sec} second is equal to {h} hours {m} minutes and {s} seconds.'
print(result)
# End
# common abc and xyz elements
# Start
abc = list(range(10, 10000))
xyz = list(filter(lambda x: x % 4 == 0, abc))
print(xyz.__len__())
# End
# finding longest word in sentence
# Start
sentence = input('Sentence? ')
liste = [sentence]
liste = liste[0].split()
liste = sorted(liste, key=len)
print(liste[-1])
# End
# finding vowel and consonant in sentence
# Start
sentence = input("Enter a sentence : ").strip().lower()
vowels = list('aeıiouöü')
consonants = list('qwrtypğşlkjhgfdzxcvbnmç')
vowel = 0  # sesli
consonant = 0  # sessiz
for i in sentence.strip():
    if i in vowels:
        vowel += 1
    elif i in consonants:
        consonant += 1
print(f"{vowel} vowels and {consonant} consonants are in the sentence")
# End
# Finding digit log for each number of 0 to n range
# Start
# uses math library
# with the help of math lib.
# we made faster then turning in to string in a long run
num = int(input('Enter a Number : '))


def calc(number):
    lst = []
    [lst.append(i) for i in range(1, number)]
    ls2 = list(map(lambda x: int(math.log10(x)) + 1, lst))
    return sum(ls2)


print(calc(num))
# End
# Yıldız çizme
# Start
usercount = 12
count = 0
halfcount = int(usercount / 2)
flag = True
while flag:
    if count <= usercount / 2:
        print("*"*count)
        count += 1
    elif count >= usercount / 2:
        count += 1
        halfcount -= 1
        print("*"*halfcount)
        if count == usercount:
            flag = False
# End
# math operation
# Start


def calculator(cn1, cn2, op):
    if op != "+" and op != "-" and op != "%" and op != "*":
        return "Enter valid arg."
    else:
        cn1, cn2 = str(cn1), str(cn2)
        cal = eval(cn1 + op + cn2)
        return cal


print(calculator(5, 2, "*"))
# End
# Start
# with __doc__ (docstring) we can add explanation
# to our code as below


def absolute_value(val):
    """ This function turns absolute value of number"""
    if val < 0:
        return val * -1
    else:
        return val


print(absolute_value(-4))
print(absolute_value.__doc__)
# End
# Start
# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
# Note that an empty string is also considered valid.
# defined other solution at work1 line 42
user = input("Enter brackets: ").strip()
user = list(user)


def compare(lst1):
    """Comparing brackets with inputs"""
    brackets = list("{[()]}")
    check = []
    for i in range(len(lst1)):
        check.append(lst1[i] in brackets)
    return all(check)


result = 0
if compare(user) and (len(user) % 2) == 0:
    if user[0] == "(":
        result = True if user[1] == ")" or user[-1] == ")" else False
    elif user[0] == "{":
        result = True if user[1] == "}" or user[-1] == "}" else False
    elif user[0] == "[":
        result = True if user[1] == "]" or user[-1] == "]" else False
else:
    result = "Invalid Entry"

print(result)
# End
# Start
# We have a loud talking parrot. We are in trouble if the parrot is talking and the hour is before 6 or after 21.


def parrot_trouble(talking, hour):
    if talking:
        if (hour in range(0, 7)) or (hour in range(21, 24)):
            return True
        else:
            return False
    else:
        return False


print(parrot_trouble(True, 5))
print(parrot_trouble(True, 8))
print(parrot_trouble(False, 22))
# End
# koordinatlar ile hareket etme
# Start
C = ["right 20", "right 30", "left 50", "up 10", "down 20"]

x = y = 0

for i in range(len(C)):
    if C[i].startswith("r"):
        x = x + int(C[i].split()[1])
    elif C[i].startswith("l"):
        x = x - int(C[i].split()[1])
    elif C[i].startswith("u"):
        y = y + int(C[i].split()[1])
    elif C[i].startswith("d"):
        y = y - int(C[i].split()[1])

result = [x, y]
print(result)
# End
# Factorial
# Start


def factorial(z):
    fac = 1
    for i in range(1, z+1):
        fac *= i
    return fac


print(factorial(4))
# End

# Password Generator
# Start
# random imported
uppers = [chr(random.randint(65, 90)) for i in range(3)]
lowers = [chr(random.randint(97, 122)) for j in range(3)]
numbers = [chr(random.randint(48, 57)) for k in range(3)]
chars = chr(random.randint(33, 47)) + chr(random.randint(58, 64))
password = "".join(uppers) + "".join(lowers) + "".join(numbers) + chars


def shuffleit(arg):
    temp = list(arg)
    random.shuffle(temp)
    return "".join(temp)


print(shuffleit(password))
# End
# Start
# list comprehension faster than loops
# timeit imported


def for_loop():
    res = []
    for i in range(1):
        res.append(i)
    return len(res)


def list_comp():
    l = [i for i in range(1)]
    return len(l)


a, b = timeit(for_loop, number=1), timeit(list_comp, number=1)

print(round(b/a, 2))
print(for_loop(), round(timeit(for_loop, number=1), 20))
print(list_comp(), round(timeit(list_comp, number=1), 20))
# End
# Letter count with timeit
# Start
# from timeit import repeat
testcode = """
def letter_count(sentence="This sentence will be example."):
    ls = list(sentence)
    dic = {}
    for i in ls:
        if i not in dic:
            dic[i] = 1
        else:
            dic[i] += 1
    return dic
"""


print(repeat(stmt=testcode, repeat=6))
# End

# Permutation of given list
# Start
# 1 2 3
# 2 1 3
# 2 3 1
# 3 2 1
# 3 1 2
# 1 3 2
# I took [1, 2 ,3] as a example list to create an algorithm. As you can see above first number iterates to the end
# and the iteration time decrease at outer loop when each inner loop cycle is completed
lst = [1, 2, 3]
permutations = []
ls = lst.copy()

for i in range(len(ls), 0, -1):
    for j in range(i):
        if ls not in permutations:
            permutations.extend(ls)
        index = ls[j]
        ls.pop(j)
        ls.insert(j+1, index)
ls.clear()

permutation = [permutations[x:x+len(lst)] for x in range(0, len(permutations), len(lst))]
print(permutation)
# End
