number = input("Enter a number : ")
# print(number, type(number), number.isdigit())
if not number.isdigit():
    print("It is an invalid entry. Don't use non-numeric, float, or negative values!")
else:
    num = list(map(int, number))
    lst = [i**len(num) for i in num]
    if sum(lst) == int(number):
        is_Armstrong = f"{number} is an Armstrong number"
    else:
        is_Armstrong = f"{number} is not an Armstrong number"
    print(is_Armstrong)
