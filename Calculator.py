a=int(input("enter your first number:"))
b=int(input("enter your second number:"))
choice=int(input("enter your choice:"))

def add():
    c=a+b
    return c
def sub():
    c=a-b
    return c
def mul():
    c=a*b
    return c
    
def div():
    c=a/b
    return c

if choice==1:
    print(add())
    
if choice==2:
    print(sub())
    
if choice==3:
    print(mul())
if choice==4:
    print(div())
