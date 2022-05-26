import streamlit as st
import pandas as pd
import joblib

st.title("Heart Disease Prediction")

st.subheader('Disclaimer: THIS APP IS NOT FOR DIAGNOSIS PURPOSES AND SHOULD NOT BE TAKEN AS ONE')

st.write("## This app is a proto-type of what would be used to input in the system")


height = st.number_input("How tall are you?", min_value=1, max_value=610)

weight = st.number_input("What is your weight in lbs", min_value=1, max_value=1500)

smoke = st.multiselect("Have you ever smoke 5 packs of cigarettes (100 cigarettes) in your lifetime?",
                       options=['yes' , 'no', 'not sure'])

stroke = st.multiselect("Have you ever had a stroke?",
                       options=['yes' , 'no', 'not sure'])

# need to fix this so that it can code in pre-diabetic-female-during pregnancy
diabetes = st.multiselect("Do you have diabetes?",
                       options=['yes', 'no', 'pre-diabetic','not sure'])

asthma = st.multiselect("Do you have asthma?",
                       options=['yes' , 'no', 'not sure'])
arthritis = st.multiselect("Do you have arthritis of any for such as : rheumatism, polymyalgia rheumatica;"
                           " osteoarthritis (not osteporosis); tendonitis, bursitis, bunion,"
                           "tennis elbow; carpal tunnel syndrome, tarsal tunnel syndrome; joint infection, etc?",
                       options=['yes' , 'no', 'not sure'])


f = open('./data/final_fitted_model.sav', 'rb')
final_model = joblib.load(f)
f.close()

users_movies_seen = pd.read_csv('./data/users_movies_seen.csv', index_col='userId')
movies = pd.read_csv('./data/movies_cleaned.csv', index_col=0)

#Function here

#function notes: need to convert lbs to kg in it, convert height into meters


hide_table_row_index = """
            <style>
            tbody th {display:none}
            .blank {display:none}
            </style>
            """
st.markdown(hide_table_row_index, unsafe_allow_html=True)

run = st.button("click to run")

if run:
    results = recommender2(user, genre, num_recs)
    st.table(results['Title'])