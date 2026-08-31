import random

plist=[]

for i in range(16):
    plist.append(i)


print(plist)

flist=[]

flist=list(range(0,16))

print(flist)

slist=[]


for i in flist:
    b=i**2
    slist.append(b)

print(slist)

even=[]
odd=[]

for s in slist:
    if s%2==1:
        odd.append(s)
    else:
        even.append(s)

print(odd)
print(even)

d2=[["XXXXXXXXXXX"],
    ["XXXXXXXXXXX"],
    ["XXXXXXXXXXX"],]

print(d2)

d3=[[3,7],[32,4],[32,5],[34,5]]
print(len(d3))

print(len(d3[0]))
print(d3[1][0])

for i,t in d3:
    print(str(i)+" "+str(t))

for i in d3:
    for f in i:
        print(f,end=" ")

    print("\n")

r=int(input("How many rows do you want?"))
c=int(input("How many columns do you want?"))

r2d=[]

for i in range(r):
    e=[]
    for o in range(c):
        x=random.randint(1,10)
        e.append(x)
    r2d.append(e)


print(r2d)




    






















