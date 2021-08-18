# Modules
# Pre-Class

# How to import a module
# import array           # importing using the original module name
# import array as arr    # importing using an alias name
# from array import *    # imports everything present in the array module
import datetime
from datetime import date
import random
import math

# built in modules link https://docs.python.org/3/py-modindex.html
print(dir(math))  # you can find out all names defined in this module
# The built-in function dir() is used to find out which names a module defines. It returns a sorted list of strings.
print(random.random())  # Gives float value between 0, 1

# Packages
# if we are going to work with large project, we have so much modules
# that includes same names so we created packages to classified modules
# Every package and subpackage have to have empty __init__.py file

# In order to display the list of subpackages/modules inside the package,
# we must add the following syntax into the __init__.py files:
# For the package : __all__ = ['subpackage1', 'subpackage2']
# For the subpackage : __all__ = ['module1', 'module2']

# from . import mongolia  # one dot means addressing to a current package/subpackage
# from .. import europe  # two dots mean addressing to a parent package/subpackage
# from ..europe import kosovo  # subpackage name comes immediately after two dots

# Absolute imports syntax are preferred, as they are usually more readable.

# In-Class
# from datetime import date ekleriz
# gün bazında int değer alırız
birth = date(571, 4, 22)
death = date(632, 7, 8)

print(datetime.date.toordinal(death) - datetime.date.toordinal(birth))
