# looping through values
# break statement
#continue statement
for x in "apple":
    print(x)

fruits= ["apple","mango","cherry"]
for x in fruits:
    print(x)
    if x== "banana":
        break
    print(x)

fruits = ["apple","mango","cherry"]
for x in fruits:
    if x == "banana":
        continue
    print(x)
