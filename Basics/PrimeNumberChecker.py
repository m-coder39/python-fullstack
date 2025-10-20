def PrimeNumberChecker(x):
    'PrimeNumberChecker'
    if(x<=1):
        print("not prime")
    else:
        for i in range(2,x+1):
            if(x!=i and x%i==0):
                print("not prime")
                break
        else:
            print("prime")
    return

n=int(input("enter number"))
PrimeNumberChecker(n)