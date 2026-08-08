from numbers import Number
from sys import exception


class Book:
    name = ''
    def __init__(self, name):
        self.name = name

class PP(Book):
    #price = 0
    def __init__(self,price,name):
        self.price = int(price)
        Book.__init__(self,name)
        #super().__init__(name)

# book = Book('金庸')
# book.name = '古龍'
# print(book.name)

try:
    pp = PP('1','K-POP')
    print(pp.price)
    print(pp.name)
except:
    print('error')
else:
    print('1223')
finally:
    print('finally')




