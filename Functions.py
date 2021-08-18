# Python Plus Lesson First Subject
# Pre-class
# Global and Local Variables
text = "I am the global one"


def global_func():
    print(text)  # we can use 'text' in a function
    # because it's a global variable


global_func()  # 'I am the global one' will be printed
print(text)  # it can also be printed outside of the function

text = "The globals are valid everywhere "

global_func()  # we changed the value of 'text'


# 'The globals are valid everywhere' will be printed

def local_func():
    local_text = "I am the local one"
    print(local_text)  # local_text is a local variable


local_func()  # 'I am the local one' will be printed as expected

# print(local_text)  # NameError will be raised
# because we can't use local variable outside of its function

# LEGB Ranking Rule

# 1- Locals. The space which is searched first, contains the local names defined in a function body.
# 2- Enclosing. The scopes of any enclosing functions, which are searched starting with the nearest enclosing scope
# (from inner to outer), contains non-local, but also non-global names.
# 3- Globals. It contains the current module’s global names. The variables defined at the top-level of its module.
# 4- Built-in. The outermost scope (searched last) is the namespace containing built-in names.
variable = "global"


def func_outer():
    variable = "enclosing outer local"

    def func_inner():
        variable = "enclosing inner local"

        def func_local():
            variable = "local"
            print(variable)

        func_local()

    func_inner()


func_outer()  # prints 'local' defined in the innermost function
print(variable)  # 'global' level variable holds its value

# Global and Nonlocal
# if we didn't use global count in func.
# counter() it will raise UnboundLocalError

# Global
count = 1


def counter():
    global count  # we've changed its scope
    print(count)  # it's global anymore
    count += 1


counter()
counter()
counter()
# Nonscope


def enclosing_func1():
    x = 'outer variable'

    def enclosing_func2():
        nonlocal x  # its inner-value can be used in the outer scope
        x = 'inner variable'
        print("inner:", x)
    enclosing_func2()
    print("outer:", x)


enclosing_func1()

# In-Class


def brothers(bro1, bro2, bro3):
    print(bro1, bro2, bro3, end='')
    print()


bros = ['ali', 'hasan', 'mehmet']
brothers(*bros)


def merger(*genius):
    print(f"For me, {genius[0]} {genius[1]} and {genius[2]} {genius[3]} are geniuses.")


merger('Bill', 'Gates', 'Guido van', 'Rossum')


def gene(x="Solomon", y="David"):
    print(x, "belongs to x")
    print(y, "belongs to y")


gens = {"y": "Ahmet", "x": "Mehmet"}
gene(**gens)

dict_couple = {"bride": ["esma", "ela", "ayşe", "gönül"],
               "groom": ["ahmet", "semih", "tamer", "ali"]}


def muruvvet2(bride, groom):
    return [x for x in zip(bride, groom)]


print(muruvvet2(** dict_couple))
# average of friend's age
dict_friends = {"ahmet": 23, "alfred": 34, "rose": 41, "sena": 21, "ali": 19}


def meaner(**ages):
    values = sum([i for i in ages.values()])
    return "The average is:", (values / len(ages))


print(meaner(** dict_friends))

# Lambda
# You can use it with its own syntax using parentheses,
# You can also assign it to a variable,
# You can use it in several built-in functions,
# It can be useful inside user-defined functions (def).
# lambda usage
print((lambda x, y: x**y)(2, 3))
v = (lambda x: x[::-1])("arter")
print(v)

n = [1, 4, 6]
n2 = [1, 2, 5]
k = list(map(lambda x, y: x*y, n, n2))
print(k)

words = ["alinin evi", "hasanın ocağı", "keremin yunusu", "asd"]
print(list(map(len, words)))

a = list(filter(lambda x: len(x) < 5, words))
print(a)

# arbitrary func ile lambda
equalambda = lambda *arg: list(arg).count(max(list(arg), key=list(arg).count)) \
    if list(arg).count(max(list(arg), key=list(arg).count)) > 1 else 0

print(equalambda(1, 2, 3, 4, 45, 4, 4))

# Function Generator
# Start


def function_generator(x):
    return lambda j: x(j)


d = function_generator(print)
d1 = function_generator(max)
d2 = function_generator(sorted)
d("hello")
print(d1([3, 4, 5, 6]))
print(d2([32, 45, 66, 90, 2]))
# End
