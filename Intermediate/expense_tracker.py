from unittest import addModuleCleanup


def add(des,amount,category):
    f=open('expenses.txt','a')
    s=str(des)+"-"+str(amount)+"-"+str(category)
    f.write(s+"\n")
    f.close()
def view_all():
    f=open('expenses.txt','r')
    s=f.read()
    print(s)
    f.close()
def view_total():
    f=open('expenses.txt','r')
    lines=f.readlines()
    total=0
    for line in lines:
        des,amount,category=line.strip().split('-')
        total+=int(amount)
    print("total="+str(total))
    f.close()
def search(categ):
    f=open('expenses.txt','r')
    lines=f.readlines()
    for line in lines:
        des,amount,category=line.strip().split('-')
        if(categ==category):
            print("Description-"+des+"\nAmount-"+amount+"\nCategory-"+categ)
    print()


def fun():
    print("Menu")
    print("1.Add a new expense\n2.View all expenses\n3.View total amount spent\n4.search expenses by category\n5.exit")
    ch=int(input("enter your choice"))
    if(ch==1):
        des=input("enter description")
        amount=int(input("enter amount"))
        category=input("enter category")
        add(des,amount,category)
    elif(ch==2):
        view_all()
    elif(ch==3):
        view_total()
    elif(ch==4):
        categ=input("enter the category")
        search(categ)
    elif(ch==5):
        exit()
    else:
        print("invalid choice :( try again")
        fun()
fun()