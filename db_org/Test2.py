"""
test example
"""
import sys
str_a = "Hello"
print(type(str_a))
str_a = u"Hello"
print(type(str_a).__bases__)
print(sys.getdefaultencoding())