import streamlit as ar
from streamlit_option_menu import option_menu

with ar.sidebar:
    select=option_menu(
        menu_title="Internship",
        options=["Internship","about","contact"],
        icons=['book','file-person','telephone'],
   )
if select == "Internship":
    ar.title("Internship")
elif select=="about" :
    ar.title("about")
    
elif select == "contact" :
    ar.title("contact")
    
# ar.title("VINSUP INFOTECH")#title name
# ar.header("PM TOWER")#header
# ar.subheader("Kalavasal")
# ar.text("madurai")
# ar.write("Theni road")
# ar.badge("add",color="red")
# ar.metric("Vinsup","10","20%")
# ar.latex("a+b=a+b+2ab")
# ar.code("""
# a=20
# b=10
# c=a+b
# print(c)
# """,language="python")
# a=ar.text_input("Enter the name")
# ar.write(a)
# ar.text_input("Name")
# ar.number_input("Age",min_value=0)
# ar.selectbox("gender",["male","female"])
# ar.multiselect("skills",["HTML","CSS","JS","PYTHON"])
# ar.radio("state",["TN","KL","AP"])
# ar.checkbox("Agree ton terms and cconditions")
# ar.button("Submit")
# ar.button("Click")

# #for columns
# col1,col2=ar.columns(2)

# with col1:
#     ar.text_input("username")
#     ar.image("https://i.pinimg.com/originals/ea/fd/16/eafd1603d0937a7fe51208013cc84eb2.jpg")
# with col2:
#     ar.text_input("password")

# #for sidebar use
# with ar.sidebar:
#     ar.write("side bars")