import numpy as np
import streamlit as st
import pandas as pd
data=pd.read_csv(r"D:\disorder project\Sleep_health_and_lifestyle_dataset.csv")
data=data.fillna("no disorder")
data.head()
data=data.drop(['Person ID','Gender','Occupation','BMI Category','Blood Pressure'],axis=1)
X = data.drop(["Sleep Disorder"],axis=1)
y = data["Sleep Disorder"]
print("d")
# Split the data to train and test the dataset.
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
print("j")
# Support vector machine algorithm
from sklearn.svm import SVC
model = SVC()
model.fit(X_train, y_train)
predictions = model.predict(X_test)
print("kk")
a=model.predict([[19,6,6,70,7,80,10000,120,80]])
print(a)

print("dd")
from sklearn.metrics import accuracy_score
accuracy_score(y_test, predictions)
 

st.markdown("<h1 style='text-align: center; font-size:35px;'>SLEEP DISORDER PREDICTION</h1>",
    unsafe_allow_html=True,)
hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True)
st.text("            by sidharth raj")
name=st.text_input('ENTER YOUR NAME')
gen= st.radio(
    "GENDER",
    ["MALE", "FEMALE"],
    index=None,
)
age=st.slider("AGE")
col1, col2 = st.columns(2)

with col1:
    a = st.number_input("ENTER DAILY STEPS",0,100000)
    b= st.number_input("ENTER SLEEP DURATION (in hours)",0,24)
    c= st.number_input("RATE QUALITY OF SLEEP(out of 10)", 0,10)
    d= st.number_input("RATE PHYSICAL ACTIVITY(out of 100)", 0,100)
with col2:
    e = st.number_input("RATE STRESS LEVEL(out of 10)",0,10)
    f= st.number_input("ENTER BLOOD PRESUURE(SYSTOLIC)",0,200)
    g= st.number_input("ENTER BLOOD PRESSURE(DIASTOLIC)",0,140)
    h= st.number_input("HEART RATE", 0,100)
str1=''.join(model.predict([[age,b,c,d,e,h,a,f,g]]))
print(str1)
if st.button("PREDICT THE DIORDER WITH SOLUTON"):
    r=model.predict([[age,b,c,d,e,h,a,f,g]])
    print(r)
    aaa="DISORDER:"
    st.success(aaa)
    st.success(r)

    if(str1=='Sleep Apnea'):
            a=",your solution includes maintaining a healthy weight through regular exercise and a balanced diet.\nAvoiding alcohol and sedatives before bedtime, practicing good sleep hygiene,\n and sleeping on your side can all contribute to improved breathing patterns \nand reduced symptoms of sleep apnea"
            aa="Hello\t "+ name+ a
            st.success(aa)
    