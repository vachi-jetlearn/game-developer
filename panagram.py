x=input("Please write sentence")
x=x.lower()

y=list(x)

y= set(y)

set={'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'} 

print(y)

if set.issubset(y):
    print("This is a panagram")