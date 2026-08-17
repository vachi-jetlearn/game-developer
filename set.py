'''sett={}
#print(type(sett))
sett=set()
#print(type(sett))


set1={433,33,"hi",True, 443548584, "ggrrggrr",433,33}
#print(set1)

set1.add("part")
print(set1)

list1=["##$#","$%##@$#@$#$%$"]
list1=set(list1)
#print(type(list1))
#print(list1)

#print(len(list1))



#for i in list1:
    #print(i)


#if ("hi") in set1:
    #print("hi is in this set")

#else:
    #print("no")

set1.remove("hi")
set1.discard("hi")
set1.pop()


print(set1)'''

x={22,"hi"}
y={44,"hello",22}
z={33,98,"hello"}

print(x|y)

print(x&y)

print(x-y)
print(y-x)

print(x^y^z)