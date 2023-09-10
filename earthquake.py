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
        st.header("LATITUDE IS NOT DEFINED")
    elif Longitude==0:
        st.header("LONGITUDE IS NOT DEFINED")
    else:
       data=[Latitude,Longitude]
       print(data)
       pred=model.predict([data])
       print(pred)
       st.header("MAGNITUDE")
       st.subheader(pred[0][0])
       print(pred[0][0])
       st.header("DEPTH")
       st.subheader(pred[0][1])
       print(pred[0][1])
    
  
    

  

