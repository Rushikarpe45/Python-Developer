# #program to map to list collection in the form of dictonary

# l1=['a','b','c']
# l2=[10,20,30]

# {'a':10,'b':20,'c':30}



def make_dict():
    l1=['a','b','c','d']
    l2=[10,20,30]
    d=dict(zip(l1,l2))
    print(d)
make_dict()
