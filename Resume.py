import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image as im
with open("style.css") as f:
    st.markdown('<style>{}</style>'.format(f.read()), unsafe_allow_html=True)
df=pd.read_csv('education.csv')
# Header
st.write(''' # Rohan Gurubhaiye, MTech 
##### *Resume* ''')

img=im.open('RG.JPEG')
st.image(img,width=150)
st.markdown('## Summary', unsafe_allow_html=True)
st.info('''
- Currently working on project to classify data into certain categories using NLP and using the same data to generate Graphs that can give a consolidated insights.

- Worked On specific text extraction from a certain types of files Using Python, OCR, Image Processing and PDF mining.

- Developed Human Profession Identification Model Using Computer Vision methodology.

- Performed Bit Transfer using LiFi Technology.

- Worked as Backend Developer and Delivered 2 Commercial website.

- Developed a Automatic Time Table Generator as Final year Diploma(Computer Technology) project .
''')
#####################
# Navigation

st.markdown('<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">', unsafe_allow_html=True)

st.markdown("""
<nav class="navbar fixed-top navbar-expand-lg navbar-dark" style="background-color: #DB73F7;">
  <a class="navbar-brand" href="https://www.linkedin.com/in/rohan-gurubhaiye/" target="_blank">Rohan Gurubhaiye</a>
  <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
    <span class="navbar-toggler-icon"></span>
  </button>
  <div class="collapse navbar-collapse" id="navbarNav">
    <ul class="navbar-nav">
      <li class="nav-item active">
        <a class="nav-link disabled" href="/">Home <span class="sr-only">(current)</span></a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#education">Education</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#work-experience">Work Experience</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#social-media">Social Media</a>
      </li>
    </ul>
  </div>
</nav>
""", unsafe_allow_html=True)

#####################



#####################
# Custom function for printing text
def txt(a, b):
  col1, col2 = st.columns([4,1])
  with col1:
    st.markdown(a)
  with col2:
    st.markdown(b)

def txt2(a, b):
  col1, col2 = st.columns([1,4])
  with col1:
    st.markdown(f'`{a}`')
  with col2:
    st.markdown(b)

def txt3(a, b):
  col1, col2 = st.columns([1,2])
  with col1:
    st.markdown(a)
  with col2:
    st.markdown(b)
  
def txt4(a, b, c):
  col1, col2, col3 = st.columns([1.5,2,2])
  with col1:
    st.markdown(f'`{a}`')
  with col2:
    st.markdown(b)
  with col3:
    st.markdown(c)

#####################

st.markdown('''
## Education
''')
st.bar_chart(data=df.sort_values(by=['Score'],ascending=True), x='Education', y='Score', width=400, height=400)
txt('**Master of Technology** (Computer Science and Engineering with Specialization in Big Data Analytics), *Vellore Institute of Technology*, Chennai, Tamilnadu, India',
'2020-2022')
st.markdown('''
- GPA: `8.09`
- Passed with Distinction.
Project Undertaken:- 
- Title: "Human Profession Identification Model Using Computer Vision methodology".
- Title: “Predicting Hospital Mortality using Multiparameter Intelligent Monitoring in Intensive Care (MIMIC3) Dataset”
- Title: “Football Data Visualization”
- Title: “Analysis of customer shopping behaviour in an e commerce landscape”

''')

txt('**Bachelor of Technology** (Computer Science and Engineering), *Maharashtra Institute of Technology*, Aurangabad, Maharashtra, India',
'2017-2020')
st.markdown('''
- GPA: `7.78`
- Graduated with Distinction.
Project Undertaken:- 
- Title: “Data Transmission Using Light Fidelity”
- Title: “CRM for Ktrans” (Currently being used)
- Title: “Commercial Website for ISP” http://www.webnetbroadband.com
- Title: “Lab Booking System”
''')

txt('**Diploma** (Computer Technology), *Marathwada Institute of Technology*, Aurangabad, Maharashtra, India',
'2014-2017')
st.markdown('''
- Percentage: `75.53`
- Passed with Distinction.
Project Undertaken:- 
- Title: “Goal Tracking” 
''')

#####################
st.markdown('''
## Work Experience
''')

txt('**Data Scientist**, Great Lakes E Learning Services Pvt Ltd',
'June 2022 (Currently working)')
st.markdown('''
- Currently working on project to classify data into certain categories using NLP and using the same data to generate Graphs that can give a consolidated insights.
''')

txt('**Data Scientist Intern**, Worley India Pvt Ltd',
'August 2021-April 2022')
st.markdown('''
- Worked On specific text extraction from a certain types of files Using Python, OCR, Image Processing and PDF mining.''')
txt('**Intern**, Webnet Broadband',
'Jan 2020 - May 2020')
st.markdown('''
- Worked as Network Engineer
''')



#####################


#####################
st.markdown('''
## Skills
''')
txt3('Programming', '`Python`, `R`, `Linux`')
txt3('Data processing/wrangling', '`SQL`, `pandas`, `numpy`')
txt3('Data visualization', '`matplotlib`, `seaborn`, `plotly`, `altair`, `ggplot2`')
txt3('Machine Learning', '`scikit-learn`')
txt3('Deep Learning', '`TensorFlow`')
txt3('Web development', '`Flask`, `HTML`, `CSS`')
txt3('Model deployment', '`streamlit`, `gradio`, `R Shiny`, `Heroku`, `AWS`, `Digital Ocean`')

#####################
st.markdown('''
## Social Media
''')
txt2('LinkedIn', 'https://www.linkedin.com/in/chanin-nantasenamat')
txt2('Twitter', 'https://twitter.com/thedataprof')
txt2('GitHub', 'https://github.com/chaninn/')
txt2('', 'https://github.com/chaninlab/')
txt2('', 'https://github.com/dataprofessor')
txt2('ORCID', 'http://orcid.org/0000-0003-1040-663X')
txt2('Scopus', 'http://www.scopus.com/authid/detail.url?authorId=12039071300')
txt2('ResearcherID', 'http://www.researcherid.com/rid/F-1021-2010')
txt2('ResearchGate', 'https://www.researchgate.net/profile/Chanin_Nantasenamat')
txt2('Publons', 'https://publons.com/a/303133/')