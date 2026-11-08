def notprime():
    x=int(input("Enter a:"))
    y=int(input("Enter b:"))

    for i in range(x,y+1):
        if checkprime(i)==False:
            print(i)
            


def checkprime(num):
    count=0
    for j in range(2,num+1):
        if num%j==0:
            count+=1
        if count>2:
            return False
    if count==2:
        return True


notprime()