import streamlit as st
import pickle
import pandas as pd


st.sidebar.title('Configure Your Car')


html_temp = """
<div style="background-color:tomato;padding:10px">
<h2 style="color:white;text-align:center;">Predict Value of Your Car</h2>
</div><br><br>"""


st.markdown(html_temp,unsafe_allow_html=True)


selection=st.selectbox("Select Your Model", ["XGBOOST", "Random Forest"])

if selection =="XGBOOST":
	st.write("You selected", selection, "model")
	model= pickle.load(open('xgb_model', 'rb'))
else:
	st.write("You selected", selection, "model")
	model= pickle.load(open('rf_model', 'rb'))
    

age=st.sidebar.selectbox("What is the age of your car",(1,2,3))
hp=st.sidebar.slider("What is the hp of your car", 60,200, step=5)
km=st.sidebar.slider("What is the km of your car", 0,100000, step=500)
car_model=st.sidebar.selectbox("Select model of your car", ('A1', 'A2', 'A3','Astra','Clio','Corsa','Espace','Insignia'))

my_dict = {
    "hp": hp,
    "age": age,
    "km": km,
    "model": car_model
}

columns=['age',
 'hp',
 'km',
 'model_A1',
 'model_A2',
 'model_A3',
 'model_Astra',
 'model_Clio',
 'model_Corsa',
 'model_Espace',
 'model_Insignia']

df = pd.DataFrame.from_dict([my_dict])

X = pd.get_dummies(df).reindex(columns=columns, fill_value=0)

prediction = model.predict(X)

st.header("The configuration of your car is below")
st.table(df)
st.subheader("Press predict if configuration is okay")

if st.button('Predict'):
    st.success("The estimated price of your car is €{}. ".format(int(prediction[0])))



     
   
    





    


