#python dates concept
# python dates not a data type / it is  date object

import datetime

a=datetime.datetime.now( )
print(a)


# creating Date objects

import datetime
a= datetime.datetime(2020,5,17)
print(a)

# using strftime( ) method ('string formatting time method)
#"%B" == month name display output

import datetime
a=datetime.datetime(2019,8,12)
print(a.strftime("%B"))

#"%A" == weekday full version


import datetime
a=datetime.datetime(2019,8,12)
print(a.strftime("%A"))

#"%a" == weekday short version



import datetime
a=datetime.datetime(2019,8,12)
print(a.strftime("%a"))

#"%b" == month name short version
import datetime
a=datetime.datetime(2019,8,12)
print(a.strftime("%b"))


# Date output

import datetime
a=datetime.datetime.now( )
print(a.year)
print(a.strftime("%A"))
