# list metodlarını bulunduran döküman = https://docs.python.org/3/library/stdtypes.html#mutable-sequence-types
# Collection Type 'lar (list,set,taple,dict) içine alınan iterable elemanı kelimelerine ayrırarak alır.

def pre_class():
    """Pre class içerikleri içerir
    """
    # list atamalırını ⇒ country = ['USA', 'Brasil', 'UK', 'Germany', 'Turkey', 'New Zealand'] bu şekilde yapabiliriz.
    # listi method olarakta kullanabiliriz. Aşağıda string ataması yapılan değişken listeye atılma şekilleri verilmiştir
    string_1 = 'I quit smoking'

    new_list_1 = list(string_1)  # we created multi element list
    print(new_list_1)

    new_list_2 = [string_1]  # this is a single element list
    print(new_list_2)
    print()


def ornek1():
    """1. Örnek : Liste elemanı
    """
    list_1 = ['one', 'four', 'nine']
    list_2 = ['@', '*-', 'False']
    list_3 = [True, False]
    list_4 = [[3], [44], [-12]]
    list_5 = [[1, 3], [44, -40], [-12, 1]]

    list_1.sort()
    list_2.sort()
    list_3.sort()
    list_4.sort()
    list_5.sort()

    print(list_1)
    print(list_2)
    print(list_3)
    print(list_4)
    print(list_5)

    # aşağıdaki elemanlar liste elemanı sayılır
    print(len(["a b", False, None, []]))
    print()


if __name__ == "__main__":
    print(pre_class.__doc__)
    pre_class()
    print(ornek1.__doc__)
    ornek1()

