def palindrome_checker(s):
    'Palindrome Checker'
    rev=s[::-1]
    if(s==rev):
        print("palindrome")
    else:
        print("not palindrome")
    return


a=input("enter string or a number")
palindrome_checker(a)
