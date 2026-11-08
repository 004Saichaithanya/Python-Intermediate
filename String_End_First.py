str=input()
L=str.split(" ")
x=0
flag=1
for x in range(len(L)-1):
            
            s1=L[x]
            s2=L[x+1]
            if(s1[-1]!=s2[0]):
                flag=0
                break

if flag:
    print("true")
else:
    print("false")
