# Predicting Heart Disease



# Overview

As of 2020, heart disease is the leading cause of death in the US, with the disease claiming close to 700,000 that year. It is the leading cause of death regardless of gender and for most race/ethnicity. This disease can lead to early death in individuals, increase medicial visits and a lost of productivity in our economy. As such, it is important to try to address this. My project aims to help build a predictive model for heart disease. By being able to predict whether a patient has heart disease or not, this can be used in hospital to flag doctors to discuss way to manage this disease and prevent early death and potentially slow/mitigate the disease progression.


# Business Problem

With how prevalent heart disease is in the nation, it is important for doctors to discuss with their patients about early prevention. In order to do this, doctors would need to know more about a patient’s history in order to diagnose them with having heart disease, potentially requiring blood work in addition. Getting the results from the blood work usually happens after the patient’s is already out of the doctor’s office. Calls will then be made to discuss these results and potential follow up appointments will be made. 

Our model aims to predict whether a patient, who comes into a doctor’s office/hospital, has heart disease. By being able to predict if the patient has heart disease or not, we can then flag this patient for the doctor electronically. Instead of having to waiting for a phone call for a discussion on, that may not be between the patient and doctor, conversation between the doctor and patient about managing heart disease can begin. This flagging can help start the conversation between the doctor and patient about early prevention steps that can be made and can help lead the doctor in asking certain questions for further verification and testing.

# Data

The data was taken from the [CDC's 2020 Behavorial Risk Factor Surveillance System](https://www.cdc.gov/brfss/annual_data/annual_2020.html) (BRFSS). Due to how large the data is, this data was not uploaded to the github but can be found where the data was taken underneath the data files section.

It is a survey data performed between 2020 to 2021 from the CDC to monitor people's health-behavior, chronic health conditions, and use of services to help manage their disease. The data contains information of the individual such as `race` and `gender` that we will not use to avoid these biases in our models. A new column was created as the data does not specifically have a column called heart disease but instead has two two columns called `cvdinfr4` and `cvdcrhd4` that corresponded with whether the individual was ever told/diagnose with having a heart attack and told that they had coronary heart disease. Both questions, get at the issue of heart disease.

# Results



# App
Our best model was deployed in an app. The function development in the app.py file can be found in the app development notebook. In addition, the code used to make the app on streamlit can be found in the app.py. Unfortunately, due to how big the model file is (2-4 Gb), I was unable to implement my model on the streamlit website, but managed to run it locally. As such, it is not available for others to use. In my GitHub, I have provided the streamlit environment in which I created it. This app can be run locally with the streamlit environment along with running the modeling notebook in order to get the model file into your local computer.

# Next Steps

The next step for this project would be to further refine our target. This projects only looks at heart attack and Cornary Artery Disease. These two conditions are some of the conditions that fall under the heart disease. Heart disease encompasses other conditions such as high blood pressure, congenitial heart disease etc., it's not just CAD and heart attacks as such we would have to refine the questions being asked to individual. 

Not only that but more time to refine our model. Due to computational limitation of my system and the computational time, I am not able to perform as much gridsearches to fine-tune the model even further. Not only that but we can refine our model on data from patients' information form and the diagnoses given by the doctor to help improve the flagging of indivduals with such a condition that way their primary doctor know to discuss this with the patient.

Build a better app. The app created was for demonstrated purposes. 
# Conclusion


# Repository Structure
```
├── Workspace  
│       ├── EDA.ipynb
│       └── modeling.ipynb
│
├── data
├── image
├── Heart_disease_EDA.ipynb
├── Heart_disease_Modeling.ipynb
├── presentation.pdf
├── README.md
├── get_features.py
└──model.py
```


