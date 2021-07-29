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
