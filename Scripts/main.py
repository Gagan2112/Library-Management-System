import streamlit as st
import pandas as pd
import mysql.connector
import datetime
st.title("LIBRARY MANAGEMENT SYSTEM")
choice=st.sidebar.selectbox("My Menu",("Home","User","Admin","Read Books"))
st.write(choice)
if(choice=="home"):
    st.image("https://clipground.com/images/library-management-system-logo-clipart-4.jpg")
    st.markdown("<center><h1>WELCOME</h1><center>",unsafe_allow_html=True)
    st.write("This is a Web Application developed by Gagan as a part of Learning.")
elif(choice=="User"):
    btn2=st.button("Temporary")
    if 'login' not in st.session_state:
        st.session_state['login']=False
    uid=st.text_input("Enter User ID")
    upwd=st.text_input("Enter Password")
    btn=st.button("Login")
    if btn:
        mydb=mysql.connector.connect(host="localhost",user="root",password="12345678",database="library")
        c=mydb.cursor()
        c.execute("select * from users")
        for r in c:
            if(r[0]==uid and r[1]==upwd):
                st.session_state['login']=True
                break
        if(not st.session_state['login']):
            st.write("Incorrect credentials")
    if(st.session_state['login']):
        st.write("Login Successful")
        choice2=st.selectbox("Features",("None","View All Books","Issue the Books")) 
        if(choice2=="View All Books"):
            mydb=mysql.connector.connect(host="localhost",user="root",password="12345678",database="library")
            df=pd.read_sql("select * from books",mydb) 
            st.dataframe(df)
        elif(choice2=="Issue the Books"):
            bid=st.text_input("Enter Book ID")
            usid=st.text_input("Enter your User ID") 
            btn2=st.button("Issue Book")
            if btn2:
                iid=str(datetime.datetime.now()) 
                mydb=mysql.connector.connect(host="localhost",user="root",password="12345678",database="library")
                c=mydb.cursor()
                c.execute("insert into issue values(%s,%s,%s)",(iid,bid,usid))
                mydb.commit()
                st.header("Book Issued Successfully")
elif(choice=="Admin"):
    if 'alogin' not in st.session_state:
        st.session_state['alogin']=False
    aid=st.text_input("Enter Admin ID")
    apwd=st.text_input("Enter Password")
    btn=st.button("Login")
    if btn:
        mydb=mysql.connector.connect(host="localhost",user="root",password="12345678",database="library")
        c=mydb.cursor()
        c.execute("select * from admins")
        for r in c:
            if(r[0]==aid and r[1]==apwd):
                st.session_state['alogin']=True
                break
        if(not st.session_state['alogin']):
            st.write("Incorrect credentials")
    if(st.session_state['alogin']):
        st.write("Login Successful")
        choice2=st.selectbox("Features",("None","View Issue Books","Add new Books","Delete Book","Add new account")) 
        if(choice2=="View Issue Books"):
            mydb=mysql.connector.connect(host="localhost",user="root",password="12345678",database="library")
            df=pd.read_sql("select * from issue",mydb) 
            st.dataframe(df)
        elif(choice2=="Add new Books"):
            bid=st.text_input("Enter Book ID")
            bname=st.text_input("Enter Book name") 
            aname=st.text_input("Enter Author name")
            btn2=st.button("Add Book")
            if btn2:
                mydb=mysql.connector.connect(host="localhost",user="root",password="12345678",database="library")
                c=mydb.cursor()
                c.execute("insert into books value(%s, %s, %s)",(bid,bname,aname))
                mydb.commit()
                st.header("Book Added Successfully")
        elif(choice2=="Delete Book"):
           bid=st.text_input("Enter Book ID")
           btn2=st.button("Delete book")
           if btn2:
               mydb=mysql.connector.connect(host="localhost",user="root",password="12345678",database="library")
               c=mydb.cursor()
               c.execute("delete from books where book_id=%s",(bid,))
               mydb.commit()
               st.header("Book Deleted Successfully")
        elif(choice2=="Add new account"):
           uid=st.text_input("Enter user ID")
           upwd=st.text_input("Enter user password")
           btn2=st.button("Add new account")
           if btn2:
               mydb=mysql.connector.connect(host="localhost",user="root",password="12345678",database="library")
               c=mydb.cursor()
               c.execute("insert into users value(%s,%s)",(uid,upwd))
               mydb.commit()
               st.header("User Added Successfully")
elif(choice=="Read Books"):
    choice3=st.selectbox("Choose Books",('None','Machine Learning','Data Science','SQL'))
    if(choice3=="Machine Learning"):
        st.markdown("<iframe src='http://ai.stanford.edu/~nilsson/MLBOOK.pdf' width='100%' height='500px'></iframe>",unsafe_allow_html=True)
    elif(choice3=="Data Science"):
        st.markdown("<iframe src='https://mrcet.com/downloads/digital_notes/CSE/II%20Year/DS/Introduction%20to%20Datascience%20[R20DS501].pdf' width='100%' height='500px'></iframe>",unsafe_allow_html=True)
    elif(choice3=="SQL"):
        st.markdown("<iframe src='https://www.hcoe.edu.np/uploads/attachments/r96oytechsacgzi4.pdf' width='100%' height='500px'></iframe>",unsafe_allow_html=True)  
        