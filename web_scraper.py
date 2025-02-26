import requests as req
from bs4 import BeautifulSoup
import streamlit as st

def set_page_layout():
    st.set_page_config(layout = "wide")
    
set_page_layout()

st.title("Web Scraper")

with st.form("web scraper"):
     url = st.text_input("Enter Url to scrape")
     
     col1,col2,col3,col4,col5 = st.columns(5)
     
     with col1:
         tag = st.text_input("Enter the tag you want to find:")
     with col2:
         class_ = st.text_input("Enter class to find class or tag:")
     with col3:
         how_many = st.text_input("number of elements to find:")
         st.write("(enter all to find all)")
     with col4:
         id_ = st.text_input("Enter id to find the element:")
     with col5:
         just_text = st.radio("extract just inner text ?",["yes","no"])   
         
     submitted = st.form_submit_button("submit")
     if submitted:
        if url.strip() == "":
           st.write("The url should not be empty")
        else:
         html = req.get(url)
         soup = BeautifulSoup(html.text,features = "html.parser")
             
         if tag.strip() != "" and class_.strip() != "":
            html = soup.find_all(tag,attrs={"class":class_})
            
         elif tag.strip() == "" and class_.strip() != "":
            html = soup.select(class_)
            
         elif tag.strip() != "" and class_.strip() == "":
            html = soup.find_all(tag)
         
         
         if id_.strip() != "" and  tag.strip() != "" and class_.strip() != "": 
             html = soup.find_all(tag,attrs={"class":class_,"id":id_})
             
         if id_.strip() == "" and  tag.strip() != "" and class_.strip() != "":
             html = soup.find_all(tag,attrs={"class":class_})
         
         if id_.strip() == "" and  tag.strip() == "" and class_.strip() != "":
             html = soup.find_all(class_ = class_)
         
         if id_.strip() != "" and  tag.strip() != "" and class_.strip() == "":
             html = soup.find_all(tag,attrs={"id":id_})
         
         if id_.strip() != "" and  tag.strip() == "" and class_.strip() == "":
             html = soup.find_all(id = id_)
         
         if id_.strip() == "" and  tag.strip() != "" and class_.strip() == "":
             html = soup.find_all(tag)
         
         if id_.strip() != "" and  tag.strip() == "" and class_.strip() != "":
             html = soup.find_all(id = id_, class_ = class_)
         
         
         if just_text == "yes":
             extracted_tags = ""
             if how_many == "all" or how_many.strip() == "":                 
                for tag in html:
                    extracted_tags += " " + tag.get_text(strip = True, separator = " ") + "\n"
                if extracted_tags == "":
                    st.code("not found")
                else:
                    st.code(extracted_tags)
             else:
                try:
                    for i in range(int(how_many)+1):
                        extracted_tags += " " + html[i].get_text(strip = True, separator = " ") + "\n"
                    if extracted_tags == "":
                       st.code("not found")
                    else:
                       st.code(extracted_tags)  
                except:
                    st.write("reduce the number of elements to find")           
                    st.write("and make sure it's an integer")   
         else:
             extracted_tags = ""
             if how_many == "all" or how_many.strip() == "":                 
               for tag in html:
                   extracted_tags += str(tag) + "\n"
               if extracted_tags == "":
                    st.code("not found")
               else:
                    st.code(extracted_tags)  
             else:
                try:
                    for i in range(int(how_many)+1):
                       extracted_tags += str(html[i]) + "\n"
                    if extracted_tags == "":
                       st.code("not found")
                    else:
                       st.code(extracted_tags)  
                except:
                    st.write("reduce the number of elements to find") 
                    st.write("and make sure it's an integer")   
    
