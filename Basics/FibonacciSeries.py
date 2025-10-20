def FibonacciSeries(n):
    'Print first n Fibonacci numbers'
    a=0
    b=1
    if(n<2):
        print("invalid n")
    else:
        for i in range(0,n+1):
            print(a,end=" ")
            a,b=b,a+b
    return

n=int(input("enter n"))
FibonacciSeries(n)