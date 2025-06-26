#wap to extract the given string from string is palindrome or not
def palindrome(l):
    l1=[]
    for i in l:
        if i==i[::-1]:
            l1.append(len(i))
            
    return l1
    
print(palindrome(eval(input("enter your string: "))))

