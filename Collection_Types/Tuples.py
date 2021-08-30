# Bir tuple oluşturulduktan sonra, değerlerini değiştiremezsiniz. Tuple değiştirilemez.
# Parantezlerin içine değerlerin eklenmesi ile oluşturulur. deger = (1, 2, 3)
# Tupple tek elemanlı olarak tanımlandığında içindeki değerin type 'ını döndürür.

# deger = ([2, 3]) type(deger) = list
# Tek elmanlı tupple için virgül koymalıyız.
# value= ([2, 3],) type(value) = tuple

# Important----------------
# What is Tuple: A tuple is a collection type that includes one or more characters
# A tuple is a collection type that includes one or more characters
# Paranteze alınmayan ve virgüllerle ayrımış her eleman,  değerler tuple olarak saklanır.

# Tuple eleman ekleyip çıkaramayız ama elemanlarını değiştirebiliyoruz. Örneğin bir liste varsa listenin iç değerini
# değiştirebiliriz. Elemanlarının içine girerek metodlarda değişiklik yapabiliriz.
# (Bu istenilen bir durum değildir yapılmaması gerekir.)

# Broadcasting spesifik bir indexe değer atanmasıdır


def ornek1():
    """1. Örnek : Tuple hakkında genel bilgi
    """
    a = tuple()
    star = ("a", 1, [1, "2"])
    y = 1,
    # bu üç öğe de tuple'dır

    city = ["los-angeles", "beirut", "tokyo"]
    city[0] = True  # Broadcasting
    print(city)
    city[1:] = "istanbul", "seoul"  # tuple değer ile çoklu atama
    print(city)
    city[1:] = "bangladeş"  # verilir ise harf harf atama yapar
    # bangladeş değişkeninin yanına virgül konursa tek değer
    # olarak alınır aksı taktirde strig iterable olarak alır
    print(city)
    # tuples support indexing
    tple = 1, 2, 3
    print(tple[0], tple[1], tple[2])
    print()

if __name__ == "__main__":
    print(ornek1.__doc__)
    ornek1()
