from collections import Counter

# method 1
def find_needle(n, h):
    return Counter(h.split())[n]

n = "portugal"
h = 'lobito programmer from portugal hello fromportugal portugal'

# method 2
needle = h.split().count(n)
print(needle)

print(find_needle(n, h))

