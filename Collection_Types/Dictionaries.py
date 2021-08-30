# Dictionaries

# 2 şekilde dict tanımlanır. Collectionlardan tuple,list i value ekleyebiliriz
grocer1 = {"fruit": "apple", "drink": "water"}
grocer2 = dict(fruit="apple", drink="water")
print(grocer1)
print(grocer2)

# key ve value'ye int string boolean değer atanabilir
# dict' dict() şeklindeyken key değişken şeklinde olduğundan int atılamaz
# çünkü stringe çevrilir
first_Dict = {1: "one", "two": 2, False: [1, 2, 3]}
print(first_Dict)

# sec_dict'teki key listeyi kabul etmezken tuple'ı kabul eder.
# sec_dict = {[1, 2, 3]: "Listele", "clarus": "the best"}
third_dict = {(1, 2, 3): "Listele", "clarus": "the best"}
# print(sec_dict)
print(third_dict)

# key değeri olarak dictionary atanamaz ama value dict. atanabilir.
# fourth_dict = {{1: "bir", 2: "iki"}: "sözlük"}
fifth_dict = {"erkekler": {"ahmet": 35, "mehmet": 20, "recep": 55}, \
              "kadınlar": {"aslı": 22, "selman": 42, "fatma": 19}}
# print(fourth_dict)
print(fifth_dict)

# dict. key'i parenteze yazarak value'sünü döndürür.
print(fifth_dict['erkekler'])

# aşağıdaki şekilde dict.'e ekleme yapabiliriz
fifth_dict['hayvanlar'] = 'Kedi'
print(fifth_dict)

# Task
# Dictionary oluşturma

family = {
    'mother': 'Türkan',
    'father': 'Ömer',
    'brother': 'Adem'}

print(family)

family['sister'] = 'Hacer'

# append ile listeye ekleme yapabiliriz.
sayılar = {'tek': [], 'çift': []}
sayılar['tek'].append(1)
print(sayılar)

# fromkeys gönderilen değerleri key olarak atıyor
meyveler = {}.fromkeys(['elma', 'armut'], 0)
print(meyveler)

# int değeri artırma += şeklinde yapılabilir
meyveler['elma'] += 3
print(meyveler)

dict_by_dict = {'animal': 'dog',
                'planet': 'Neptun',
                'number': 40,
                'pi': 3.14,
                'is_good': True}

# item, key, value değerlerini döndürür
# iterable şeklindedir, döngü içine girebilir
print("Items : ", dict_by_dict.items())
print(dict_by_dict.keys())
# dict. leri list şekline çevirir
print(dict_by_dict.values())

print(list(dict_by_dict.items()))
print(list(dict_by_dict.values()))

# dict. kalıcı olarak değiştirir, sonuna ekler
# {} kullanarak eklenir ve birden fazla ekleme yapılabilir
# yoksa ekler varsa değiştirir
dict_by_dict.update({'is_bad': False, 'is_qualified': True})
print(dict_by_dict)

# value-key silme işlemi
# yan yana yazarakta silme işlemi yapabiliriz
del dict_by_dict['is_qualified'], dict_by_dict['is_bad']
print(dict_by_dict)

# using 'in' and 'not in' operator,
# you can check if key is in dictionary,
# aramaları sadece key 'lerde yapar
clarusway = {'ali': 12, 'veli': 32, 'ahmet': 22}
print('zeka küpü' in clarusway)

# dict. i value metoduyla çağırarak value araması yapabiliriz.
print(12 in clarusway.values())

school_records = {
    'personal_info':
        {'kid': {'tom': {'class': 'intermediate', 'age': 10},
                 'sue': {'class': 'elemantary', 'age': 8}
                 },
         'teen': {'joseph': {'class': 'college', 'age': 19},
                  'marry': {'class': 'high school', 'age': 16}
                  },
         },
    'grades_info':
        {'kid': {'tom': {'math': 88, 'speech': 69},
                 'sue': {'math': 90, 'speech': 81}
                 },
         'teen': {'joseph': {'coding': 80, 'math': 89},
                  'marry': {'coding': 70, 'math': 96}
                  },
         }
}
print("school_records uzunluğu : ", len(school_records))
print("Marry'nin yaşı :", school_records['personal_info']['teen']['marry']['age'])

# Liste biçiminde joseph'in ders ve notları
print("joseph (Liste):", list(school_records['grades_info']['teen']['joseph'].items()))
print("joseph (Dict):", school_records['grades_info']['teen']['joseph'])

print("joseph :", school_records['grades_info']['teen']['joseph'])

# İki dictionary birleştirmenin kısayolu
combined_dict = dict(**dict_by_dict, **school_records)
print(combined_dict)
