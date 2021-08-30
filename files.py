# In this module we work with file operations as open, read, close, write etc.
# Pre Class

# Reading Files

# open has following parameters :
# the file should be stored in the current working directory
files = "fishes.txt"
open(files, mode='r', buffering=-1, encoding=None, errors=None, newline=None, closefd=True, opener=None)

# Default and most common value of encoding is UTF-8
# mode Parameter Attributes:
# 'r' => Open for reading (default). If the file doesn't exist, FileNotFoundError will raise.
# 'a' => Open for writing. It will append to the end of the file if it already exists. If there is no file,
# it will create it.
# 'w' => Open for writing. It will be overwritten if the file already exists. If there is no file, it will create it.
# 'x' => Open for exclusive creation, it will fail if the file already exists.
# 'b' => Open in binary mode.
# 't' => Open as a text file (default).
# '+'=> Open for updating (reading and writing).

# If you want to open and be able to read, modify, and update the existing file you should set the mode as 'r+'

# .read(size) display the first size characters of text

sea = open("fishes.txt", 'r')
print(sea.read(5))
sea.seek(0)  # seek içine ne yazarsak içine cursor oraya gider
sea.tell()  # "tell" object tell us which cursor we were
print(sea.readline())  # shows the first line of the text
print(sea.readline(7))  # shows the second line of the text and takes first 7 line because we specified it to 7
print(sea.readlines())  # .readlines() makes list of text element. If we use after readline(), it takes remaining
# texts from the file

# reading file with loop. we can iterates sea.readlines() too in for loop
for line in sea:
    print(line)

sea.close()  # be sure to close file

# if we use with ... as ... block it closes the file automatically. For instance we can call example above as :
# with open("file.py", "r") as sea

# Writing Files


# In Class

# os ve shutil modulleri import edilerek çeşitli dosya işlemleri yapılabilir.
file = open("fishes.txt", "r")
print(file.read(25))
file.seek(0)  # cursoru sıfırlama
print()
print(file.read(75))
print(file.tell())  # cursorun yerini yazar
print(file.read(13))  # sıfrlamadığımız için kaldığı yerden okumaya devam eder
print(file.tell())
file.close()

