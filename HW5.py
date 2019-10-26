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