"""
Counted List
Create a class for an list like object based on UserList wrapper
https://docs.python.org/3/library/collections.html#collections.UserList
That object should have a method to return a Counter
https://docs.python.org/3/library/collections.html#collections.Counter
for all objects in the list
Counter should be updated automatically for at lest 2 methods (append, pop)
"""

# example to test code
# class Example(UserList)
#   ...
#
# x = Example(['1', '2', '3'])
# y = x.get_counter() # y contains Counter({'1':1, '2':1 '3':1})
# x.append(3)
# now y contains Counter({'1':1, '2':1 '3':2})

from collections import UserList,Counter

class CountedList(UserList):

    def Count(self):
        self.cnt=Counter(self.data)
        return self.cnt

    def append(self, item):
        super(CountedList,self).append(item)
        global y
        y = self.Count()

countedlist=CountedList(['1', '2', '3'])
y=countedlist.Count()
print(y)

countedlist.append('3')
print(y)

