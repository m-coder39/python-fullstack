def prime_numbers(a,b):
    'prime numbers in a range'
    l=[]
    for i in range(a,b+1):
        for j in range(2,i):
            if(i%j==0):
                break
        else:
            l.append(i)
    s=set(l)
    print(s)


m=int(input("enter first number"))
n=int(input("enter second number"))
prime_numbers(m,n)


