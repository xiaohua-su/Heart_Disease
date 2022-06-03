import streamlit as st
import pandas as pd
import numpy as np
import joblib

st.title("Heart Disease Prediction")

st.subheader('Disclaimer: THIS APP IS A TOOL TO FLAG A DOCTOR AND SHOULD NOT BE TAKEN AS A DIAGNOSIS')

st.write("## This app is a proto-type of what would be used to input in the system")


height = st.number_input("How tall are you in meters?", min_value=0.0, max_value=3.0, format="%.2f")

weight = st.number_input("What is your weight in kg", min_value=0, max_value=500)

sleep = st.number_input("On average, how many hours of sleep do you get a day?", min_value=0.00, max_value=24.00,
                        format="%.2f")

general_health = st.number_input("How would you rate your health from a scale of 1 to 5? "
                                 "With 1 being excellent and 5 being poor?",
                                 min_value=1.00, max_value=5.00)

phys_health = st.number_input("How many days during the past 30 days was your physical health not good?",
                              min_value=0, max_value=30)

alcohol_consumption = st.number_input("How many days do you drink in a month?",
                             min_value=0, max_value=30)

men_health = st.number_input("how many days during the past 30 days was your mental health not good?",
                                      min_value=0, max_value=30)

smoke = st.selectbox("Have you ever smoke 5 packs of cigarettes (100 cigarettes) in your lifetime?",
                       options=['yes' , 'no', 'not sure'])

stroke = st.selectbox("Have you ever had a stroke? ", options=['yes' , 'no', 'not sure'])

diabetes = st.selectbox("Do you have or ever had diabetes? ",
                          options= ['yes', 'no', 'Only during pregnancy', 'Pre-diabetic', 'not sure'])

asthma = st.selectbox("Do you have asthma?", options=['yes', 'no', 'not sure'])


arthritis = st.selectbox("Do you have arthritis of any for such as : rheumatism, polymyalgia rheumatica;"
                           " osteoarthritis (not osteporosis); tendonitis, bursitis, bunion,"
                           "tennis elbow; carpal tunnel syndrome, tarsal tunnel syndrome; joint infection, etc?",
                       options=['yes' , 'no', 'not sure'])
skincancer = st.selectbox("Have you ever had skin cancer?", options=['yes', 'no', 'not sure'])

cancer = st.selectbox("Have you ever had any other cancer?  ", options=['yes', 'no', 'not sure'])

insurance = st.selectbox("Do you have health insurance?", options=['yes', 'no', 'not sure'])

copd = st.selectbox("Do you have copd or any relative issues?", options=['yes', 'no', 'not sure'])

depresdisorder = st.selectbox("Have you ever been diagnosed with any form of depression",
                                options=['yes', 'no', 'not sure'])
kidney = st.selectbox("Do you have kidney disease? ", options=['yes', 'no', 'not sure'])

walking = st.selectbox("Would you say you have difficulty walking", options=['yes', 'no', 'not sure'])

last_checkup = st.selectbox("when was your last check up?",
                              options=['Within past year', 'Within past 2 but more than 1 year',
                                       'Within past 5 but more than 2 years','5+ years', 'never', 'not sure'])

exercise = st.selectbox("Did you participate in any physical activities or exercise during the past month", options=['yes', 'no', 'not sure'])

f = open('./log2.sav', 'rb')
model = joblib.load(f)
f.close()

#Function here
def information_gather(diabetes,asthma,arthritis,smoke,stroke,general_health,
                       insurance,skincancer,cancer,copd,depresdisorder,
                       kidney,walking,phys_health, last_checkup, exercise,
                       sleep,weight ,height, alcohol_consumption):
    info = {'general_health': [general_health],
            'health_insurance': [insurance],
            'stroke': [stroke],
            'asthma': [asthma],
            'skin_cancer': [skincancer],
            'other_cancer': [cancer],
            'copd_type_issue': [copd],
            'arthritis_anyform': [arthritis],
            'depressive_disorder': [depresdisorder],
            'kidney_disease': [kidney],
            'diabetes': [diabetes],
            'difficulty_walking': [walking],
            'smoke100_lifetime': [smoke],
            'physical_health': [phys_health],
            'mental_health': [men_health],
            'last_checkup': [last_checkup],
            'excercise_30': [exercise],
            'sleep': [sleep],
            'weight_kg': [weight],
            'height_m': [height],
            'alcohol_consumption_30': [alcohol_consumption]
            }

    df = pd.DataFrame.from_dict(info)

    same_coding = ['health_insurance', 'stroke', 'asthma', 'skin_cancer',
                   'other_cancer', 'copd_type_issue', 'arthritis_anyform',
                   'kidney_disease', 'difficulty_walking', 'depressive_disorder',
                   'smoke100_lifetime', 'excercise_30']

    for x in same_coding:
        df[x] = df[x].apply(lambda x: 1 if (x == 'yes') else (2 if (x == 'no') else None))

    for x in df['diabetes']:
        if x == 'Only during pregnancy':
            df['diabetes'] = 2
        elif x == 'yes':
            df['diabetes'] = 1
        elif x == 'no':
            df['diabetes'] = 3
        elif x == 'Pre-diabetic':
            df['diabetes'] = 4
        else:
            df['diabetes'] = None

    for x in df['last_checkup']:
        if x == 'Within past year':
            df['last_checkup'] = 1
        elif x == "Within past 2 but more than 1 year":
            df['last_checkup'] = 2
        elif x == 'Within past 5 but more than 2 years':
            df['last_checkup'] = 3
        elif x == '5+ years':
            df['last_checkup'] = 4
        elif x == 'never':
            df['last_checkup'] = 8
        else:
            df['last_checkup'] = None

        return model.predict(df)[0]


run = st.button("click to run")

if run:
    results = information_gather(diabetes,asthma,arthritis,smoke,stroke,general_health,
                       insurance,skincancer,cancer,copd,depresdisorder,
                       kidney,walking,phys_health, last_checkup, exercise,
                       sleep,weight ,height, alcohol_consumption)
    st.info('This is a purely informational message')

    if results == 1 :
        st.write('This person LIKELY has heart disease. '
             'Please discuss ways the person can manage this condition and verify'
             'this diagnosis')
    else:
        st.write('This individual DOES NOT have heart disease. Preventative'
                 ' measures can still be discuss with them though.')
