excel=dict([])
count=1
for i in range(ord('A'),ord('Z')+1):
    print(chr(i))
    excel[chr(i)]=count
    count+=1

print(excel)
val=int(input("Enter number:"))
div=val//26
mod=val%26
print(div,mod)
res=""
for key,value in excel.items():
    if div==value:
        res+=key

for key,value in excel.items():
    if mod==value:
        res+=key

print(res)
    








