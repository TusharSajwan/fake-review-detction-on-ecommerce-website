import streamlit as st
from joblib import load
import nltk
nltk.download('stopwords')
from nltk.corpus import stopwords
import string

def text_process(review):
    nopunc = [char for char in review if char not in string.punctuation]
    nopunc = ''.join(nopunc)
    return [word for word in nopunc.split() if word.lower() not in stopwords.words('english')]

st.title('Spam Review Detection')
with st.sidebar:
    st.title('menu')
    app_mode = st.selectbox('choose app mode', ['review detection', 'about'])
if app_mode == 'review detection':
    # Text input for user's comment
    user_input = st.text_input('Input your comment here :', '')
    if st.button('Predict'):
        try:
            # Attempt to load the model
            model = load('text_classification_model_SVC.joblib')
            # Make predictions
            prediction = model.predict([user_input])
            
            # Display prediction
            st.write(f'comment is: {prediction[0]}')
        except Exception as e:
            st.subheader("Information on the Models")
   # if st.checkbox("Performance of various ML models:"):
            
       # st.write('1.K Nearest Neighbors Prediction Accuracy: 57.52%')   
       # st.write('2.Support Vector Machines Prediction Accuracy: 87.9%')
if app_mode =='about':
    st.header('About Data', False)
    st.markdown('This is spam review detection mady by tushar sajwan')



