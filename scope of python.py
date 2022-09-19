#scope of python
#local scope

def inner( ):
    x=4
    print(x)
inner( )

#global scope
y=10
def inner( ):
    x=4
    print("x: ",x)
    print("inside the function y: ",y)
print("y: ",y)
inner( )


#redefining variable y

y=10
def inner( ):
    x=5
    y=7
    print("x: ",x)
    print("inside the function y: ",y)
print("y: ",y)
inner( )

#modify the global variable in local scope

y=20
def inner( ):
    x=10                             ##***(i am changing global variable in local scope it gets error not possible 
    y=y+1
    print("x: ",x)
    print("inside the function y: ",y)
print("y: ",y)
inner( )


#Enclosed scope
#as like as nested function
y=10
def outer( ):
    z=10
    def inner( ):
        x=4

        print("x: ",x)
        print("inside the function z: ",z)
    inner( )
    print("z: ",z)
outer( )

#use to modify enclosed scope use key word non local

y=20
def outer( ):
    z=15
    def inner( ):
        x=4
        nonlocal z
        z= z+1
        print("x: ",x)
        print("inside the function z: ",z)
    inner( )
    print("z: ",z)
outer( )

