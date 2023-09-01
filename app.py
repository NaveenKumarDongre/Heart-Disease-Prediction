import streamlit as st
import base64
import sklearn
import numpy as np
import pickle as pkl
from sklearn.preprocessing import StandardScaler
scal=StandardScaler()

#Load the saved model
# model=pkl.load(open("final_model.p","rb"))
model=pkl.load(open("model_wcc.pkl","rb"))

st.set_page_config(page_title="Healthy Heart App",page_icon="⚕️",layout="centered",initial_sidebar_state="expanded")


# Predicting the class
def predict_disease(x): 
    return model.predict([x])


#Preprocessing user Input
# def preprocess(age,sex,cp,trestbps,restecg,chol,fbs,thalach,exang,oldpeak,slope,ca,thal ):   
def preprocess(age,sex,cp,trestbps,chol,thalach,exang,oldpeak,slope,ca,thal ):   
 
    
    # Pre-processing user input   
    if sex=="male":
        sex=1 
    else: sex=0
    
    
    if cp=="Typical angina":
        cp=0
    elif cp=="Atypical angina":
        cp=1
    elif cp=="Non-anginal pain":
        cp=2
    elif cp=="Asymptomatic":
        cp=2
    
    if exang=="Yes":
        exang=1
    elif exang=="No":
        exang=0
 
    # if fbs=="Yes":
    #     fbs=1
    # elif fbs=="No":
    #     fbs=0
 
    if slope=="Upsloping: better heart rate with excercise(uncommon)":
        slope=0
    elif slope=="Flatsloping: minimal change(typical healthy heart)":
          slope=1
    elif slope=="Downsloping: signs of unhealthy heart":
        slope=2  
 
    if thal=="fixed defect: used to be defect but ok now":
        thal=6
    elif thal=="reversable defect: no proper blood movement when excercising":
        thal=7
    elif thal=="normal":
        thal=2.31

    # if restecg=="Nothing to note":
    #     restecg=0
    # elif restecg=="ST-T Wave abnormality":
    #     restecg=1
    # elif restecg=="Possible or definite left ventricular hypertrophy":
    #     restecg=2
        
        
        
        
    # col_names = np.array(['age', 'sex', 'trestbps', 'chol', 'thalach', 'oldpeak', 'cp_1', 'cp_2','cp_3', 'fbs_1', 'restecg_1', 'restecg_2', 'exang_1', 'slope_1','slope_2', 'ca_1', 'ca_2', 'ca_3', 'ca_4', 'thal_1', 'thal_2','thal_3'])
    col_names = np.array(['age', 'sex', 'trestbps', 'chol', 'thalach', 'oldpeak', 'cp_1', 'cp_2','cp_3', 'exang_1', 'slope_1','slope_2', 'ca_1', 'ca_2', 'ca_3', 'ca_4', 'thal_1', 'thal_2','thal_3'])
    cp = "cp_"+str(cp)
    # fbs = "fbs_"+str(fbs)
    exang = "exang_"+str(exang)
    slope = "slope_"+str(slope)
    ca = "ca_"+str(ca)
    thal = "thal_"+str(thal)
    # restecg = "restecg_"+str(restecg)
    
    
    cp_index = -1 if np.where(col_names==cp)[0].size==0 else np.where(col_names==cp)[0][0]
    # fbs_index = -1 if np.where(col_names==fbs)[0].size==0 else np.where(col_names==fbs)[0][0]
    exang_index = -1 if np.where(col_names== exang)[0].size == 0 else np.where(col_names==exang)[0][0]
    slope_index = -1 if np.where(col_names==slope)[0].size == 0 else np.where(col_names==slope)[0][0]
    ca_index = -1 if np.where(col_names==ca)[0].size == 0 else np.where(col_names==ca)[0][0]
    thal_index = -1 if np.where(col_names==thal)[0].size == 0 else np.where(col_names==thal)[0][0]
    # restecg_index = -1 if np.where(col_names == restecg)[0].size == 0 else np.where(col_names==restecg)[0][0]
    
    x = np.zeros(len(col_names))
    if cp_index >= 0:
        x[cp_index] = 1
    # if fbs_index >= 0:
    #     x[fbs_index] = 1
    if exang_index >=0:
        x[exang_index] = 1
    if slope_index >= 0:
        x[slope_index] = 1
    if ca_index >= 0:
        x[ca_index] = 1
    if thal_index >= 0:
        x[thal_index] = 1
    # if restecg_index >= 0:
    #     x[restecg_index] = 1

    
    x[0] = age
    x[1] = sex
    x[2] = trestbps
    x[3] = chol
    x[4] = thalach
    x[5] = oldpeak

    
    # Feature scaling kar raha hu abhi
    from sklearn.preprocessing import StandardScaler
    scalar= StandardScaler()

    x[0:5] = scalar.fit_transform(x[0:5].reshape(1,-1))

    return x

    

       
    # front end elements of the web page 
html_temp = """ 
    <div style ="background-color:pink;padding:13px"> 
    <h1 style ="color:black;text-align:center;">Healthy Heart App</h1> 
    </div> 
    """
      
# display the front end aspect
st.markdown(html_temp, unsafe_allow_html = True) 
st.subheader('by Mescoe Student ')
      
# following lines create boxes in which user can enter data required to make prediction
age=st.selectbox ("Age",range(1,121,1))
sex = st.radio("Select Gender: ", ('male', 'female'))
cp = st.selectbox('Chest Pain Type',("Typical angina","Atypical angina","Non-anginal pain","Asymptomatic")) 
trestbps=st.selectbox('Resting Blood Sugar',range(1,500,1))
# restecg=st.selectbox('Resting Electrocardiographic Results',("Nothing to note","ST-T Wave abnormality","Possible or definite left ventricular hypertrophy"))
chol=st.selectbox('Serum Cholestoral in mg/dl',range(1,1000,1))
# fbs=st.radio("Fasting Blood Sugar higher than 120 mg/dl", ['Yes','No'])
thalach=st.selectbox('Maximum Heart Rate Achieved',range(1,300,1))
exang=st.selectbox('Exercise Induced Angina',["Yes","No"])
oldpeak=st.number_input('Oldpeak')
slope = st.selectbox('Heart Rate Slope',("Upsloping: better heart rate with excercise(uncommon)","Flatsloping: minimal change(typical healthy heart)","Downsloping: signs of unhealthy heart"))
ca=st.selectbox('Number of Major Vessels Colored by Flourosopy',range(0,5,1))
thal=st.selectbox('Thalium Stress Result',range(1,8,1))



#user_input=preprocess(sex,cp,exang, fbs, slope, thal )
# pred=preprocess(age,sex,cp,trestbps,restecg,chol,fbs,thalach,exang,oldpeak,slope,ca,thal)


# Basically here we are pre-processing the actual user input
# user_processed_input=preprocess(age,sex,cp,trestbps,restecg,chol,fbs,thalach,exang,oldpeak,slope,ca,thal)
user_processed_input=preprocess(age,sex,cp,trestbps,chol,thalach,exang,oldpeak,slope,ca,thal)
pred = predict_disease(user_processed_input)

if st.button("Predict"):    
  if pred[0] == 0:
    st.success('You have lower risk of getting a heart disease!')
    
  else:
    st.error('Warning! You have high risk of getting a heart attack!')
    
st.sidebar.subheader("About App")

st.sidebar.info("This web app is helps you to find out whether you are at a risk of developing a heart disease.")
st.sidebar.info("Enter the required fields and click on the 'Predict' button to check whether you have a healthy heart")
st.sidebar.info("Don't forget to rate this app")



feedback = st.sidebar.slider('How much would you rate this app?',min_value=0,max_value=5,step=1)

if feedback:
  st.header("Thank you for rating the app!")
  st.info("Caution: This is just a prediction and not doctoral advice. Kindly see a doctor if you feel the symptoms persist.") 