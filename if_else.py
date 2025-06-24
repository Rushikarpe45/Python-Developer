# voting
# age=int(input("Enter the age: "))
# if age>=18:
#      print("Eligible for voting.") 
# else:
#     print(" not eligible for voting")

# even or odd
# n=int(input("enter the num: "))
# if n%2==0:
#     print("the given num is even")
# else :
#     print("the given num is odd")

# check digit
# num=eval(input("enter the num: "))
# if type(num)==int:
#    print( "the given num is a digit")
# else:
#     print(" the given num is not digit")

#  check special chr
# n=input("enter the chr: ")
# if not ('A'<=n<='Z' or 'a'<=n<='z' or '0'<=n<='9'):
#     print ("the given chr is special chr")
# else:
#     print("the given chr is not special chr")

# check mutable
# a=eval(input("enter the ch"))
# if type(a)==str or tuple or int or float or complex or bool:
#     print(" the given datatype is immutable ")
# else:
#     print("the  given datatype is mutable")

# check middle 
# a=eval(input("enter the list: "))
# if len(a)%2!=0:
#     print("the middle value is: ",a[len(a)//2])
# else :
#     print("the length of the collection is even")

# # check existence
# a=eval(input("enter the first value: "))
# b=eval(input("enter the second value: "))
# if (a is b) or (b is a):
#     print('the value belongs to same memmory location:')
# else:
#     print("the given value not belongs to same memory location")

# check tuple
# tup=tuple(eval(input("enter the tuple: ",)))
# if len(tup)==2 and type(tup[0])==type(tup[1]):
#     print('the tuple is homogenous')
# else:
#    print('the tuple is  not homogenous')
    
# check positive or negative
# num=int(input('enter the no.: '))
# if num>0:
#     print('the no. is positive')
# else:
#     print('the no. is negative')

# check palindrome
# st=input("enter the str: ")
# if st[-1::]:
#      print('the given str is palindrome.')
# else:
#     print('the given str is not palindrome.')

# elif
# check chr
# chr=eval(input("enter the character: "))    
# if chr=='A'<=chr<='Z':
#      print("chr is in uppercase")
# elif chr=='a'<=chr<='z':
#      print("chr is in lowercase")
# elif  type(chr)==int:
#    print( "the given num is a digit")
# else :
#      print("the given chr is special chr")

# check the no. of digit
# num=int(input("enter the no.: "))
# if 0<=num<=9:
#      print(" the no. is single digit  ")
# elif 10<=num<=99:
#      print(" the no. is double digit  ")
# elif 100<=num<=999:
#      print(" the no. is 3 digit  ")
# else :
#      print("the no. is more than 3 digit")

# check quadrant
# x=int(input("enter the x axis pt: "))
# y=int(input("enter the y axis pt: "))
# if x>0 and y>0:
#      print(" the point lying in first quadrant")
# elif x>0 and y<0:
#      print(" the point lying in second quadrant")    
# elif x<0 and y<0:
#      print(" the point lying in third quadrant")
# else:
#      print(" the point lying in fourth quadrant")    

# find greatest num
# num1=int(input("enter the num 1:"))
# num2=int(input("enter the num 2:"))
# num3=int(input("enter the num 3:"))
# if num1>num2 and num1>num3:
#      print("the greatest no. is: ",num1)
# elif  num2>num1 and num2>num3:
#      print("the greatest no. is: ",num2)
# else:
#      print("the greatest no. is: ",num3)

# find smallest
# num1=int(input("enter the num 1:"))
# num2=int(input("enter the num 2:"))
# num3=int(input("enter the num 3:"))
# if num1<num2 and num1<num3:
#      print("the smallest no. is: ",num1)
# elif  num2<num1 and num2<num3:
#      print("the smallest no. is: ",num2)
# else:
#      print("the smallest no. is: ",num3)
     
# check relation between integer
# num1=int(input("enter the num 1:"))
# num2=int(input("enter the num 2:"))
# if num1>num2:
#      print("num1 is greater than num2.")
# elif num1<num2:
#      print("num2 is greater than num1.")
# else:
#      print("the numbers are equal to each other")
     
# check greatest number
# num1=int(input("enter the num 1:"))
# num2=int(input("enter the num 2:"))
# num3=int(input("enter the num 3:"))
# num4=int(input("enter the num 4:"))
# if num1>num2 and num1>num3 and num1>num4:
#      print("the greatest no. is: ",num1)
# elif  num2>num1 and num2>num3 and num2>num4 :
#      print("the greatest no. is: ",num2)
# elif  num3>num1 and num3>num2 and num3>num4 :
#      print("the greatest no. is: ",num3)
# else:
#      print("the greatest no. is: ",num4)
     
# check smallest number
# num1=int(input("enter the num 1:"))
# num2=int(input("enter the num 2:"))
# num3=int(input("enter the num 3:"))
# num4=int(input("enter the num 4:"))
# if num1<num2 and num1<num3 and num1<num4:
#      print("the smallest no. is: ",num1)
# elif  num2<num1 and num2<num3 and num2<num4 :
#      print("the smallest no. is: ",num2)
# elif  num3<num1 and num3<num2 and num3<num4 :
#      print("the smallest no. is: ",num3)
# else:
#      print("the smallest no. is: ",num4)

# the string
# num=int(input("enter the num: "))
# if num%3==0:
#      print("Fizz")
# elif num%5==0:
#      print("buzz")
# elif  num%3==0 and num%5==0:
#      print("Fizzbuzz")
# else:
#     print("it is not the multiple of 3 and 5")


# convert the string
# num=input("enter the char: ")
# if "A"<=num<="Z":
#      print(chr(ord(num)+32))
# elif "a"<=num<="z":
#      print(chr(ord(num)-32))
# elif "0"<=num<="9":
#      print(int(num)%3)
# else:
#      print ('the chr is special chr')
