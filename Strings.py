def string_methods():
    """STRING METHODS
    """
    # IMMUTABILITY (Değiştirilemezlik) ----------

    # Stringi print dışına yazılan metodları çıktı alırken kalıcı değişiklik yapamaz, string türünü değiştiremez.
    # Değişiklik olabilmesi için değiştirilecek olan değişkeni metoduyla yeni değişkene atarak yeni değişkeni çıktı
    # alabiliriz.

    # immutability (değiştirilemezlik) örneği
    var_str = "AHMET is Clever"
    var_str.lower()
    print(var_str)  # çıktı normal çıkar

    # Searching a String ------------

    # Arama sonucu True ya da False döndürür.
    # string arama yapma metodu
    text = "www.clarusway.com"

    text.startswith("http:")
    text.endswith(".com")

    # Changing a String -------------

    # *string.method(arguments)* şekliyle metod (capitalize(),title(),uppercase(),split()..) çağırarak değiştirilebilir.
    # .strip()* satır sonu karakterlerini (\n ,\b) ve spaceleri kırpar
    # .rstrip()* ve .*lstrip()* belirtilen karakterden ilk tekrarı görene kadar kesmeye devam eder,
    # eğer istenilen değer görmez ise durur.

    # -> strip metodu listede stringi depolarken temiz \n , \t gibi satır sonu kelimeleri ve boşluklardan
    # arındırmak için kullanılır.

    # 1. yazılan karakteri 2 ile değiştir
    # 3. yazılan ise kaç kere yapılacağını söyler
    text = "clarusway"
    text.replace('a', 'u', 1)

    text1 = "           ahmet          "
    text1.strip()
    # boşlukları kaldırır .lstrip() soldan değeri
    # rstrip() sağdaki değerleri kaldırır

    text1.strip("aw")
    # içindeki değerker olan 'a' ları ve sadece 'w' leri
    # 'aw' leri, 'wa' ları kaldırır

    # satır sonu karakterleri ve boşlukları temizler
    var = "\n\nahmet\nehmet      "
    var.strip()
    print(var)

    # strip örneği
    text = "tyou can learn almost everything in pre-classz"
    text = text.rstrip('z').lstrip('t').upper()
    print(text)
    print()


def asterisk():
    """ASTERISK : * (asterisk) in strings
    """
    # Stringlerde + 2 stringi birleştimek için kullanılır.
    #
    # Stringlerde * kullanımı aşağıdaki gibidir. (* başta olursa elemanlarına ayırır.)
    str_one = "upper"
    str_two = 3 * "upper"
    str_comb = str_one * 3

    print(str_two)
    print(str_comb)
    print(* str_one)
    print()


def iterable():
    """ITERABLE'S :
    """
    # girdi = input("")  ile çekilen verilerde string olarak değer çekilir.(girdi str 'dir.)
    # 21 // 3 = 7 sonucunu verir.  21%3 = 0 sonucu verir.

    # Python'da gezinilebilen(iterable) nesne olarak kullanılabilen bir nesneye iterable obje denir. Bu temel
    # olarak nesnedeki dizinin gezinilebileceği ve ilerlenebileceği anlamına gelir. Liste(list), sözlük(dict),
    # kümeler(set) ve hatta range gibi Python koleksiyonlarının çoğu iterable olarak ele alınabilir.
    # [start:stop:step]
    isim = "orange"  # start değeri (2) dahil stop değeri (4) dahil değil.
    print("değer : ", isim[2:4])  # 2 ve 3. karakterler çıktı verir
    print("deger: ", isim[::2])  # 2. değerleri atlayarak gider
    print(isim[-5:-2])  # ora çıkar soldaki değer dahil (-5) sağdaki (-2) dahil değil
    print()


def formatting():
    """FORMATLAMA 1 :
    """
    x = "güzel"
    y = "arabam"

    # format stringe yazılarak yapılabilmektedir
    "benim {} bir {} var".format(x, y)

    # değişkene atayarakta yapılabilir
    string = "benim {} bir {} var"
    string.format(x, y)

    # formatın içine değişken tamınlayarakta yapabiliriz

    print("{state} is the most {adj} state of {country}" .format(state="California", country="USA", adj="crowded"))

    # formatın içine değişken atamadan sadece stringle de kullanabiliriz
    print("{1} is the most {0} person in the {2}".format("clever", "Ahmet", "his classroom"))
    print()


def f_formatting():
    """F-STRING FORMATTING :
    """
    # Süslü parantezlerin içinde matematiksel işlemleri yapabiliyoruz.
    # Metodları da {} içinde kullanabiliyoruz.
    # Birden fazla satıra bölerek f-string formating kullanabiliriz. Parantez ile yada \ kullanarak yapılabilir.

    # ' \ ' (ters slash) ibaresi uzun string ifadeleri ayırmaya yarar. Alt alta yazmaz birleşik çıktı verir.

    degisken = "mary"
    print(f"8 x 8 is equals to {8 * 8}")  # matematiksel işlem
    print(f"I am {degisken.capitalize()}")  # metod kullanımı

    # Multi-line f-string kullanımı
    name = "Susan"
    age = "young"
    gender = "lady"
    school = "CLRWY IT university"

    # parantez ile kullanım
    message = (
        f"{name} is a {age} {gender}"
        f" and she is a student"
        f" at the {school}."
    )
    # \ ile kullanım
    message = f"{name} is a {age} {gender}" \
              f" and she is a student" \
              f" at the {school}."

    print(message)

    # n ile verilen değeri kelimeden çıkarmak
    word = 'clarusway'
    n = 3
    front = word[:n]
    back = word[n + 1:]
    print(front + back)
    print()


def tekrar():
    """TEKRAR : string formatlama ve yuvarlama komutları
    """
    # "{:2f}" ile noktadan sonra ilk 2 basamagı yuvarlayıp alır. ()
    #
    # Stringte ise {:.2s} ilk 2 tanesini alır. Sayı değiştikçe alıdışı harfte değişir. Sonuna 's' koymaz isek default
    # olarak string olarak yapar. (text1 örn.)
    #
    # - "{:>10}" 10 karakterlik alanda sağa yaslar.(text2 örn.)
    # - "{:<10}" 10 karakterlik alanda sola yaslar.
    # - "{:^10}" boşluk arasında ortalar.(text3 orn)
    # - "{:10.5}" değişkenin 5 karakterini alır.
    print("------1-------")
    text = "{:.2f}, {:.3f}, {:.4f}".format(3.2123123, 2.4123, 5.123123123)
    text1 = "{:.2s}, {:.3s}, {:.4s}".format("a3.b12cda", "d2.4a1j23", "ka5.1sd2d31f")
    text2 = "{:>10}".format("ahmet")
    text3 = "{:^10}".format("ahmet")
    text4 = "{:10.5} hayvanı".format("hippopotamus")

    print(text)
    print(text1)
    print(f"benim adım {text2} idir.")
    print(f"benim adım {text3} idir.")
    print(text4)
    print("------2--------")
    print("we are", "\boosting", "our", "\brotherhood")  # \b bir satır geriye götürür
    print("C:\\norht pole\noise_penguins.txt")  # \\ olursa biri gider \n aşağı alır
    print(True and "True" and "False")  # Bütün değerler True yada Truetie ise sonuncuyu alır
    print([] and ({0} or False))  # Bütün değerler False yada Falsie olması durumunda ilk sonucu alır
    print("Hipotenüs", f"{text}", sep=" : ")
    # sep="" virgül arasına değer atar ve f-string ile değişken atanabilir

    print()


if __name__ == "__main__":
    print(string_methods.__doc__)
    string_methods()
    print(asterisk.__doc__)
    asterisk()
    print(iterable.__doc__)
    iterable()
    print(formatting.__doc__)
    formatting()
    print(f_formatting.__doc__)
    f_formatting()
    print(tekrar.__doc__)
    tekrar()
