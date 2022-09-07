class Numbers:
    def __iter__(self):
        self.a = 1
        return self

    def __next__(self):
        x = self.a
        self.a += 1
        return x

myclass = Numbers()
myiterator = iter(myclass)

print(next(myiterator))
print(next(myiterator))
print(next(myiterator))
print(next(myiterator))
print(next(myiterator))
print(next(myiterator))
print(next(myiterator))
print(next(myiterator))
print(next(myiterator))
print(next(myiterator))