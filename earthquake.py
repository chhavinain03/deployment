import streamlit as st
import pickle 






st.title("EARTHQUAKE PREDICTION ")
Latitude=st.number_input('Latitude')
Longitude=st.number_input('Longitude')



clicked=st.button("Get Prediction")

with open ('rfc.dat','rb') as f:
   model= pickle.load(f)
    



if clicked ==True:
    if Latitude==0:
        print("LATITUDE IS NOT DEFINED")
    elif Longitude==0:
        print("LONGITUDE IS NOT DEFINED")
    else:
        data=[Latitude,Longitude]
        print(data)
        st.header("MAGNITUDE")
        st.subheader(model[0][0])
        print(model[0][0])
        st.header("DEPTH")
        st.subheader(model[0][1])
        print(model[0][1])
    
  
    

  

