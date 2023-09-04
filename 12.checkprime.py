n=int(input("enter the number"))
flag=False
for i in range(2,n):
    if(n%i)==0:
        flag=True
        break
if flag:
    print(n,"is not a prime number")
else:
    print(n,"is a prime number")
