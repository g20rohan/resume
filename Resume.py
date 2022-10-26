import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image as im
from pathlib import Path

# --- GENERAL SETTINGS ---
PAGE_TITLE = "Rohan Gurubhaiye"
PAGE_ICON = im.open("programmer.png")
NAME = "Rohan Gurubhaiye"
DESCRIPTION = """
Data Scientist at Great Learning.
"""
EMAIL = "g10rohan@email.com"

st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON)

df=pd.read_csv('education.csv')



# Header
st.write(''' # *Resume* ''')
########################################Code for first page########################333
# --- PATH SETTINGS ---
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir / "styles" / "main.css"
resume_file = current_dir /"Rohan_Gurubhaiye_Resume.pdf"
profile_pic = current_dir /"RG_round.png"
with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)
with open(resume_file, "rb") as pdf_file:
    PDFbyte = pdf_file.read()
profile_pic = im.open(profile_pic)

# --- HERO SECTION ---
col1, col2 = st.columns(2, gap="small")
with col1:
    st.image(profile_pic, width=230)

with col2:
    st.title(NAME)
    st.write(DESCRIPTION)
    st.download_button(
        label=" 📄 Download Resume",
        data=PDFbyte,
        file_name=resume_file.name,
        mime="application/octet-stream",
    )
    st.write("📫", EMAIL)


####################


#img=im.open('RG.JPEG')
#st.image(img,width=150)
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
<nav class="navbar fixed-top navbar-expand-lg navbar-dark" style="background-color: #EFD009;">
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
st.line_chart(data=df, x='Education', y='Score',use_container_width=True)
txt('**Master of Technology** (CSE with Specialization in Big Data Analytics), *Vellore Institute of Technology*, Chennai, Tamilnadu, India',
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
txt3('Programming', '`Python`,`PHP`, `Java`, `C`, `C++`, `C#`, `R-Programming`, `Pyspark`')
txt3('Databases','`SQL Server`, `MySQL`, `Oracle`, `PostGRE SQL`, `Neo4j`')
txt3('Data processing/wrangling', '`SQL`, `pandas`, `numpy`')
txt3('Data visualization', '`matplotlib`, `seaborn`, `plotly`')
txt3('Machine Learning', '`scikit-learn`')
txt3('Deep Learning', '`TensorFlow`')
txt3('Web development', '`Flask`, `HTML`')
txt3('Model deployment', '`Streamlit`')


#####################
st.markdown('''
## Social Media
''')
txt2('LinkedIn', 'https://www.linkedin.com/in/chanin-nantasenamat')
