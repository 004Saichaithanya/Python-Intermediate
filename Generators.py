#GENERATORS
print("Generators:")
def simple_gen():
    yield 1
    yield 2
    yield 3

for x in simple_gen():
    print(x)

#--or--
print("By next Method:")
x=simple_gen()
print(next(x))
print(next(x))
print(next(x))

def fibonacci(limit):
    a,b=0,1
    while(a<limit):
        yield a
        a,b=b,a+b

for x in fibonacci(10):
    print(x ,end=" ")

print()

# generator expression 
generator_exp=(i*5 for i in range(20) if i%2==0)

for x in generator_exp:
    print(x,end=" ")
