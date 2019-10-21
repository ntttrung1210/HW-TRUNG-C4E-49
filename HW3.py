#A nested list is a list that appears as an element in another list
#A list can store both integers and strings in it
#1
import turtle
ntt=turtle.Screen()
tt=turtle.Turtle()
tt.color("Red")
angle=0
i=2
for cl in ['Red','Blue','Brown','Yellow','grey']:
    i=i+1
    tt.color(cl)
    angle=(180*i-360)/i
    for j in range(i):
        tt.forward(150)
        tt.left(180-angle)
    if i==7:
        break   
ntt.mainloop()
#2
import turtle
ntt=turtle.Screen()
tt=turtle.Turtle()
cl=['Red','Blue','Brown','Yellow','grey']
for i in range(5):
        tt.color(cl[i],cl[i])
        tt.begin_fill()
        tt.forward(50)
        tt.left(90)
        tt.forward(100)
        tt.left(90)
        tt.forward(50)
        tt.left(90)
        tt.forward(100)
        tt.left(90)
        tt.forward(50)
        tt.end_fill()
ntt.mainloop()
#CRUD exercise
k='Y'
shop=['T-Shirt','Sweater']
while k=="Y":
    n=input("Welcome to our shop, what do you want (C,R,U,D)? ")
    n=str.upper(n)
    while n!='C' and n!='R' and n!='U' and n!='D':
        n=str.upper(input("Welcome to our shop, what do you want (C,R,U,D)? "))
    if n=='R':
        print("Our items: ",end='')
        for i in range(len(shop)-1):
            print(shop[i],end=', ')
        print(shop[i+1])
        k='b'
        while k!='N' and k!='Y':
            k=str.upper(input("Do you want to continue(Y/N)? "))
        if k=='N':
            break
    elif n=='C':
        shop.append(input("Enter new item: "))
        print("Our items: ",end='')
        for i in range(len(shop)-1):
            print(shop[i],end=', ')
        print(shop[i+1])
        k='b'
        while k!='N' and k!='Y':
            k=str.upper(input("Do you want to continue(Y/N)? "))
        if k=='N':
            break
    elif n=='U':
        pos=int(input("Update position? "))
        shop[pos-1]=input("New item? ")
        print("Our items: ",end='')
        for i in range(len(shop)-1):
            print(shop[i],end=', ')
        print(shop[i+1])
        k='b'
        while k!='N' and k!='Y':
            k=str.upper(input("Do you want to continue(Y/N)? "))
        if k=='N':
            break
    else:
        pos=int(input("Delete position? "))
        shop.pop(pos-1)
        print("Our items: ",end='')
        for i in range(len(shop)-1):
            print(shop[i],end=', ')
        print(shop[i+1])
        k='b'
        while k!='N' and k!='Y':
            k=str.upper(input("Do you want to continue(Y/N)? "))
        if k=='N':
            break
#2
sheep=[5,7,300,90,24,50,75]
print("Hello, my name is Trung and these are my sheep sizes")
print(sheep)
big=int(sheep[0])
for i in range(len(sheep)):
    if int(sheep[i])>big:
        big=int(sheep[i])
index=sheep.index(big)
print("Now my biggest sheep has size "+str(big)+" let's shear it")
sheep[index]=8
print("After shearing, here is my flock")
print(sheep)
for k in range(3):
    for i in range(len(sheep)):
         sheep[i]=sheep[i]+50
    print("MONTH ",k+1)
    print("One month has passed, now here is my flock")
    print(sheep)
    big=int(sheep[0])
    for i in range(len(sheep)):
        if int(sheep[i])>big:
            big=int(sheep[i])
    index=sheep.index(big)
    print("Now my biggest sheep has size "+str(big)+" let's shear it")
    sheep[index]=8
    print("After shearing, here is my flock")
    print(sheep)
sum=0
for i in range(len(sheep)):
    sum=sum+sheep[i]
print("My flock has size in total: ",sum)
print("I would get "+str(sum)+" * 2$ = "+str(sum*2)+"$")
#3 OPTIONAL
import random
def choose():
    words=['champion','meticulous','hexagon']
    pick=random.choice(words)
    return pick
def jumble(word):
    rd_word=random.sample(word,len(word))
    return rd_word
k='Y'
while k=='Y':
    print("                   python word_jumble.py")
    pick_word=choose()
    jq=jumble(pick_word)
    for i in range(len(jq)):
       print(jq[i],end=' ')
    print()
    ans=input("Your answer: ")
    if ans==pick_word:
        print("Hura")
    else:
        print(":(")
    k='b'
    while k!='N' and k!='Y':
        k=str.upper(input("Do you want to play again(Y/N)? "))
    if k=='N':
        break







    

        
    
    


        



