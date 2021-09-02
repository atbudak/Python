# In this module we work with file operations as open, read, close, write etc.
# Pre Class
import json
from urllib.request import urlopen
import os
# Reading Files

# open has following parameters :
# the file should be stored in the current working directory
files = "fishes.txt"
with open(files, mode='r', buffering=-1, encoding=None, errors=None, newline=None, closefd=True, opener=None) as fl:
    pass
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


def reading_files():
    """READING FILE
    """
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

# Data in the other type that we intend to write to the file must be converted to string type before the writing process


def writing_file():
    """WRITING FILES
    """
    with open("fishes.txt", 'a', encoding="utf-8") as file:
        print(file.write("\nFirst one has been died for centuries."))

    with open("fishes.txt", 'r', encoding="utf-8") as file:
        print(file.read())


def writing_with_loop():
    """WRITING FILE WITH LOOP
    """
    # Inserting list with loop
    fruits = ['Banana', 'Orange', 'Apple', 'Strawberry', 'Cherry']

    with open("fruits.txt", 'w', encoding="utf-8") as file:
        for basket in fruits:
            file.write(basket + '\n')  # adds a newline character to each string

    with open("fruits.txt", 'r', encoding="utf-8") as file:
        print(file.read())

    with open("fruits.txt", 'r', encoding="utf-8") as file:
        print(file.readlines())  # reads and displays entire lines in a list


def write_lines():
    """WRITING LISTS WITH WRITELINES
    """
    # Unlike .write() method, .writelines() takes the iterable sequence of strings and writes them to the file.
    # The difference between these two methods is just similar to the logic of difference between .read() & .readlines()

    fruits = ['Banana\n', 'Orange\n', 'Apple\n', 'Strawberry\n', 'Cherry\n']
    # the strings in the list must also include the separator chars such as \n, \t, space.

    with open("fruits.txt", 'w', encoding="utf-8") as file:
        file.writelines(fruits)  # takes an iterator for writing

    with open("fruits.txt", 'r', encoding="utf-8") as file:
        print(file.read())

    with open("fruits.txt", 'r', encoding="utf-8") as file:
        print(file.readlines())

# Working with CSV Files

# CSV stands for Comma Separated Values. A CSV file is basically a table made up of rows and columns.
# The structure of a simple CSV file is as follows :
# column 1,column 2,column 3
# first row 1,first row 2,first row 3
# second row 1,second row 2,second row 3
# third row 1,third row 2,third row 3

# There are several ways to read CSV files in Python.
#
# You can use the ordinary way of reading using open() function and .read() method.
# You can use csv Module.
# You can use the Pandas library for which created data analysis purposes.

# JSON (Javascript Object Notation) in Python


def changing_file_strings():
    """FIND AND REPLACE STRINGS IN MULTIPLE FILES
    """
    # First we import os module
    filepath = "find&replace/"
    path = os.listdir(filepath)  # inserted all document's name in filepath into path as list element
    # print(type(path), path)
    for c in path:  # checking the files name
        print(c)

    current, new, total = "Lorem Ipsum", "XXXX", 0  # creating changes and how many files has changed
    for content in path:
        counter = 0  # how many changes we made in document
        try:
            with open(filepath + content, "r", encoding="utf-8") as file:
                result = file.read()  # we have read and take the file content inside result to change below
                counter = result.count(current)
        except Exception as e:
            print("I can not read th content. Error : ", e)
            pass
        else:
            result = result.replace(current, new)  # changed current word with new word
            with open(filepath + content, "w", encoding="utf-8") as newFile:
                newFile.write(result)  # we inserted the changed result string into file

            if counter:
                print(content, ":", counter, "changes")
                total += 1

    print("Totally", total, "files has been changed.")


def creating_JSON():
    """CREATING JSON WITH DUMPS FUNCTION
    """
    # with JSON module we can create dictionaries in python and with the help of .dumps() we can convert dictionaries to
    # JSON format
    staff_dict = {"first": "Jennifer", "second": "Alias", "third": "James"}
    staff_json = json.dumps(staff_dict, indent=3)
    print(staff_json)


def creating_nested_JSON():
    """CREATING NESTED JSON
    """
    staff_dict = {}
    person_dict = {"first": "Jennifer", "second": "Alias", "third": "James"}
    staff_dict['Program Manager'] = person_dict
    staff_json = json.dumps(staff_dict, indent=3)
    print(staff_json)


def key_list_pair_JSON():
    """CREATING KET-LIST PAIR IN JSON
    """
    person_dict = {"first": "Jennifer", "second": "Alias",
                   "Attributes": {"Name": "John", "LastName": "Rudy", "Age": 32, "ısWorking": True,
                                  "Positions": ["Scrum Master", "Senior Developer", "DevOps Engineer"]}}
    languages_list = ["Python", "JavaScript", "CSharp"]
    # Adding list to dict
    person_dict["languages"] = languages_list
    person_json = json.dumps(person_dict, indent=3, sort_keys=True)
    # indent adds spaces after indentation
    # sort_keys is sorting the keys in alphabetic order
    print(person_json)


def loading_JSON_Files():
    """LOADING JSON
    """
    with open("json_example.json") as f:
        data = json.load(f)  # Loaded JSON file into Python file
        for item in data.items():
            print(item)


def urlopen_JSON():
    """REAL LIFE EXAMPLE OF JSON
    """
    # we implement from urllib.request import urlopen module
    with urlopen("https://query2.finance.yahoo.com/v7/finance/quote?symbols=AAPL") as response:
        source = response.read()
    # print(source)
    data = json.loads(source)
    print(json.dumps(data, indent=3))


# In Class
def reading_inClass():
    """READING FILE (IN-CLASS)
    """
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


if __name__ == "__main__":
    print(reading_files.__doc__)
    # reading_files()
    print(writing_file.__doc__)
    # writing_file()
    print(writing_with_loop.__doc__)
    # writing_with_loop()
    print(write_lines.__doc__)
    # write_lines()
    print(changing_file_strings.__doc__)
    # changing_file_strings()
    print(creating_JSON.__doc__)
    # creating_JSON()
    print(creating_nested_JSON.__doc__)
    # creating_nested_JSON()
    print(key_list_pair_JSON.__doc__)
    # key_list_pair_JSON()
    print(loading_JSON_Files.__doc__)
    # loading_JSON_Files()
    print(urlopen_JSON.__doc__)
    # urlopen_JSON()
    print(reading_inClass.__doc__)
    # reading_inClass()
