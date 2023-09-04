n=int(input("enter the lower number"))
n1=int(input("enter the upper number"))

for num in range(n,n1+1):
    if(num>1):
        for j in range(2,num):
            if(num%j)==0:
                break
        else:
            print(num,"is a prime number")
        
