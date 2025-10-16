def add(a,b):
    'add'
    sum=a+b
    print("sum=",sum)
    return
def sub(a,b):
    'subtraction'
    diff=a-b
    print("difference",diff)
    return
def mul(a,b):
    'multiplication'
    mul=a*b
    print("product",mul)
    return
def div(a,b):
    'division'
    if(b!=0):
        div=a/b
        print("division",div)
    else:
        print("cannot divide by zero")
    return

while(1):
    print("Arithemetic operations")
    print("1.Addition")
    print("2.Subtraction")
    print("3.Multiplication")
    print("4.Division")
    print("5.Exit")

    ch=int(input("enter the choice"))
    if ch in [1,2,3,4]:
        n1=int(input("enter number n1:"))
        n2=int(input("enter number n2:"))

    if ch==1:
        add(n1,n2)
    elif ch==2:
        sub(n1,n2)
    elif ch==3:
        mul(n1,n2)
    elif ch==4:
        div(n1,n2)
    else:
        exit()


