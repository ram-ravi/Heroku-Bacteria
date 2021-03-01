import numpy as np
import pandas as pd
import pickle
import PIL 
import streamlit as st

#open the model

def model_selection(name):
    if name=='RandomForest':
        with open('model_1.pkl', 'rb') as f:
            model= pickle.load(f)
    elif name=='ElasticNet':
        with open('model_2.pkl', 'rb') as f:
            model= pickle.load(f)
    elif name=='XGBoost': 
        with open('model_3.pkl', 'rb') as f:
            model= pickle.load(f)
    return model


def prediction(watertemp, turb, coliforms, color, enterococci, ecolifast_1, ecolifast_2, regressor):
    watertemp=float(watertemp)
    turb=float(turb)
    coliforms=float(coliforms)
    color=float(color)
    enterococci=float(enterococci)
    ecolifast_1=float(ecolifast_1)
    ecolifast_2=float(ecolifast_2)
    model=model_selection(regressor)
    predict=model.predict([[watertemp,turb, coliforms, color, enterococci, ecolifast_1, ecolifast_2]])
    #print(predict)
    return predict

def main():
    st.title("E.coli levels prediction")
    html_temp="""
    <div style= "background-color:tomato;padding:10px">
    <h2 style="color:white;text-align:center;">Streamlit E.coli prediction ML App </h2>
    </div>
    """
    st.markdown(html_temp,unsafe_allow_html=True)
    regressor = st.sidebar.selectbox('Select Regressor', ('ElasticNet', 'RandomForest', 'XGBoost'))
    
    
    watertemp = st.text_input("waterTemp_LAE")
    turb = st.text_input("turb_LAE")
    coliforms = st.text_input("coliforms_LAE")
    color = st.text_input("color_LAE")
    enterococci= st.text_input("enterococciMF_LAE")
    ecolifast_1= st.text_input("ecoli_colifast_LAE_1st")
    ecolifast_2= st.text_input("ecoli_colifast_LAE_2nd")

    

    result=""
    if st.button("Predict"):
            result=prediction(watertemp, turb, coliforms, color, enterococci, ecolifast_1, ecolifast_2, regressor)
            threshold=4.5
            if result <= threshold:
                
                st.success('The output is {} is safe for drinking'.format(str(result)))
                
            else:
                st.success('The output is {} is not safe for drinking'.format(str(result)))

    
    if st.button("About"):
        st.text("Lets LEarn")
        st.text("Built with Streamlit")


if __name__=='__main__':
    main()
    
    