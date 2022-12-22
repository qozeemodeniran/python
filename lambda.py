x = lambda a: a + 10
print(x(5))

def myfunction(n):
    return lambda v: v * n
mydoubler = myfunction(2)
print(mydoubler(11))
print(mydoubler(40))