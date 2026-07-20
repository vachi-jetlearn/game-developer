import pgzrun

list=[]

Bob=("Bob","Marks=50")
Max=("Max","Marks=80")
Sarah=("Sarah","Marks=85")

list.append(Sarah)
list.append(Max)
list.append(Bob)

print(list)

name=input("Which student would yomnaxu like to see?")
    
name=name.capitalize()

for i in list:
    name1,marks=i
    if name1==name:
        print(name+"  "+marks)

'''if name=="Bob":
    print(Bob)

elif name=="Max":
    print(Max)

elif name=="Sarah":
    print(Sarah)''

else:
    print("Sorry, that person is not in our system.")'''

