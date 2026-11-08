n=int(input("enter size:"))
k=int(input("enter no.of rotations:"))
necklace=input(f"enter {n} elements:").split(" ")

necklace=list(map(int,necklace))
print(necklace)
i=0
while i<k:
    necklace.append(necklace.pop(0))
    i+=1

print(necklace)


