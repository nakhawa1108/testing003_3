'''with return statement'''
def add(a,b):
    c=a+b
    return c
z=add(10,20)
print(z)

'''without return statement.'''
def add():
    a=10
    b=20
    c=a+b
    print(c)
add()
