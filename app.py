import streamlit as st 
from PDF_Extractor import text_extractor
from langchain_google_genai import ChatGoogleGenerativeAI
import os 


# Lets configure the model
gemini_api_key = os.getenv('TestProject1')
model = ChatGoogleGenerativeAI(
    model = 'gemini-2.5-flash-lite',           
    api_key = gemini_api_key,
    temperature = 0.9
) 

#Lets create the sidebar to upload the resume
st.sidebar.title(':red[Upload Your Resume (Only Pdf)]')
file = st.sidebar.file_uploader('Resume',type=['pdf'])
if file :
    file_text = text_extractor(file) 
    st.sidebar.success('File Uploaded Successfully')


#Lets create the mai page of application 
st.title(':orange[SKILL MATCH:-] :blue[AL Assissted Skill Matching App]',width='content')
st.markdown('##### :green[This applications will match and analyze your resume and job description provided by the applicant]',width='content')
tips = '''
Follow these steps:
1. Upload your resume (PDF only) in sidebar .
2. Copy and paste the Job Descriptions below .
3. Click on Submit run the application . 
'''
st.write(tips)

job_desc =  st.text_area(':red[Copy and paste your Job Descriptions over here:]',max_chars=5000)
if st.button(':red[SUBMIT]'):
    prompt = f'''
    <Role> Your are an expert in analyzing the resume and matching with job description and its been 5 years your doing this .Hence your are an expreinced expert in resume analyazing .
    <Goal> Match the resume and the job desciptions provided by the applicant and create a detailed report about the Resume .  
    <Context> The following content has been provided by the applicant .
    * Resume : {file_text}
    * Job Description : {job_desc}
    <Format> The report should follow these steps:
    * Give a breif description of applicant in 3 to 5 lines about the resume .
    * Describe the percentage of what a chances will the resume wil be shortlisted . 
    * Need not be the exact percentage , you may give the interval of percetage . 
    * Give the expected ATS score with matching and non-matching key words . 
    * Perfrom SWOT Analysis and explain each parameter ie Strength,Weakness,Oppurnity,thread . 
    * Give what al section can be changed in order to improve the ATS score and section percentage . 
    * Show both current version and improve version of the sections in the resume . 
    * Create 2 sample resume  which can maximaize the ATS score and section percentange.
    <Instruction> 
    * Use Bullets points for explation , wherever possible, 
    * Create tables for description where ever required . 
    * Do not add any new skill in the sample resumes .
    * The format of sample resume shoud be ina such a way that can be copied and pasted directly in word  .
    '''

    response = model.invoke(prompt)
    st.write(response.content) 
    
    