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

#Built in scope
#in built in scope it contains built in names

print("hi")
