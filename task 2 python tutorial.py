#defining a function

'''def fib(n):
    result=[]
    a,b=0,1
    while a<n:
        result.append(a)
        a,b=b,a+b
        return result
n=int(input("enter the n value:"))
print(fib(n))
    
  
#default arguments values
def college(name,person=3,msg="attend class"):
    while True:
        ok=input(name)
        if ok in ('y','yes'):
            return "please attend class"
        if name in ('n','no'):
            return "please attend college"
        print(msg)
print(college("are you a person:"))'''


#ex:keyword arguments
def parrot(voltage,state='a stiff',action='voom',type='norwegian blue'):
    print("--this parrot wouldn't, action,end=' '")
    print("if you put",voltage,"volts through it.")
    print("--lovely plumage,the",type)
    print("--it's,state,!")

parrot(100)
parrot(10000,action='acceptance',state='a bird',type='animal')
parrot(1000,'alive','deaf','animal')
parrot('a million',state='flying')

#ex:1 put *infornt of arguments

def milkproducts(kind,*reason,**details):
    print("--do you have any",kind)
    print("--i am sorry,we are all out of",kind)
    for arg in reason:
          print(arg)
    print("*"*40)
    for kw in details:
          print(kw,":",details[kw])
milkproducts("pardian","It's very runny, sir.",
           "It's really sorry,sir","its is really runny in our location,sir",
           shopkeeper="Michael Palin",
           client="John",
           sketch="milk products Sketch",
           location = "vizag")


#
def standard_arg(arg):
    print(arg)
def pos_only_arg(arg, /):
    print(arg)

def kwd_only_arg(*, arg):
     print(arg)
def combined_example(pos_only, /, standard, *, kwd_only):
     print(pos_only, standard, kwd_only)
standard_arg(234)
standard_arg(arg = 243)
pos_only_arg(234)
#pos_only_arg(arg = 243)
#kwd_only_arg(243)
kwd_only_arg(arg = 243)
#combined_example(1,2,3)
combined_example(1,2,kwd_only = 3)

#
def foo(name, **kwds):
    return 'name' in kwds

foo(1,name= 'saritha')

def foo(name,/, **kwds):
    return 'name' in kwds

print(foo(1,name= 'saritha',age = 24,gender = 'female'))

#
def concat(*args, sep="/"):
     return sep.join(args)

print(concat("earth", "mars", "venus"))

print(concat("x = earth", "y = mars", "z = venus", sep="."))

#positional and keyword arguments

def standard_arg(arg):
    print(arg)
def pos_only_arg(arg, /):
    print(arg)

def kwd_only_arg(*, arg):
     print(arg)

def combined_example(pos_only, /, standard, *, kwd_only):
     print(pos_only, standard, kwd_only)

standard_arg(234)
standard_arg(arg = 243)
pos_only_arg(234)
#pos_only_arg(arg = 243)
#kwd_only_arg(243)
kwd_only_arg(arg = 243)
#combined_example(1,2,3)
combined_example(1,2,kwd_only = 3)






        




       



    
