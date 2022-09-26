# palindrome
# it is string for suppose we take a word that word reverse it we get same ward called as palindrome.

x= input("enter the palindrome word : ")
w=''
for i in x:
    w=i+w
if(x==w):
    print("given word is palindrome")
else:
    print("given word is  not palindrome")
    
