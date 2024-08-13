# write a program enter marks of 3 subject fromm the user and store them in dictionary.start with an empty dictionary & add one by one. use subject name as key & marks as value

marks={}
x=int(input("enter phy:"))
marks.update({"phy":x})
y=int(input("enter che:"))
marks.update({"che":y})
z=int(input("enter math:"))
marks.update({"math":z})
print(marks)
