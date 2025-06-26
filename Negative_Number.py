#program to extract the negative number form a given list
l=eval(input("enter your list:"))
def Negative():
    l1=[]
    for i in l:
        if i<=0:
            l1.append(i)
        
    return l1
print(Negative())
