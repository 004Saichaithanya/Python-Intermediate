L = []
for x in range(10):
    i = int(input("Enter a value:"))
    L.append(i)

L = list(filter(lambda x: x % 2 == 0, L))
print(sum(L))
