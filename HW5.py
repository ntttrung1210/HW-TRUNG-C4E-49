#streamlit tim nghiem phuong trinh bac 2
import streamlit as st
st.title("Test")
a=int(st.text_input("nhap he so a: "))
b=int(st.text_input("Nhap he so b: "))
c=int(st.text_input("Nhap he so c: "))
if st.button("Tim nghiem"):
    if a==0:
        if b==0:
            st.write("Vo nghiem")
        else:
            st.write(-c/b)
    else:
        dlta=b*b-4*a*c
        if dlta<0:
            st.write("Vo nghiem")
        elif dlta==0:
            st.write("x= ",-b/(2*a))
        else:
            st.write("x1=",(-b+dlta**0.5)/(2*a))
            st.write("x2=",(-b-dlta**0.5)/(2*a))
#Ly thuyet
'''
    -In Python, a function is a named sequence of statements that belong together. Their primary
purpose is to help us organize programs into chunks that match how we think about the problem.

    -1. A header line which begins with a keyword and ends with a colon.
2. A body consisting of one or more Python statements, each indented the same amount —
the Python style guide recommends 4 spaces — from the header line.

    -Function calls contain the name of the function being executed followed by a list of values, called arguments,
which are assigned to the parameters in the function definition.

    -A function that returns a value is called a fruitful function in this book. The opposite of
a fruitful function is void function — one that is not executed for its resulting value, but is
executed because it does something useful

    -No,we don't

    -Most functions require arguments: the arguments provide for generalization.

    -To use function from a different file, we use 'import' and call the function that we need
'''
#Exercises
#1
def hello():
    for i in range(3):
        print("Hello world")
#2
def sum_of(a,b):
    print(a+b)
#3
from turtle import*
def draw_square(do_dai,mau):
    color(mau)
    for j in range (4):
        forward(do_dai)
        left(90)
#4
for i in range(30):
    draw_square(i * 5, 'red')
    left(17)
    penup()
    forward(i * 2)
    pendown()
mainloop()
#5
from turtle import*
def draw_star(x,y,z):
    goto(x,y)
    for i in range(5):
        forward(z)
        right(144)
#6
speed(0)
color('blue')
for i in range(100):
    import random
    x = random.randint(-300, 300)
    y = random.randint(-300, 300)
    length = random.randint(3, 10)
    draw_star(x, y, length)
mainloop()
#7
def remove_dollar_sign(s):
    ns=''
    for i in range(len(s)):
        if s[i]!='$':
            ns=ns+s[i]
    return ns
#8
string_with_no_dollars = remove_dollar_sign("$80% percent of $life is to show $up")
if string_with_no_dollars == "80% percent of life is to show up":
    print("Your function is correct")
else:
    print("Oops, there's a bug")
#9
def get_even_list(l):
    nl=[]
    for i in range(len(l)):
        if l[i]%2==0:
            nl.append(l[i])
    return nl
#10
even_list = get_even_list([1, 2, 5, 9, -10, 6])
if set(even_list) == set([2, -10, 6]):
    print("Your function is correct")
else:
    print("Ooops, bugs detected")
#11
def is_inside(l1,l2):
    if l1[0]>=l2[0] and l1[0]<=l2[0]+l2[2] and l1[1]>=l2[1] and l1[1]<=l2[1]+l2[3]:
        return True
    else:
        return False
print(is_inside([100,120],[140,60,40,50]))
#12
'''
Both dictionary and list
'''



