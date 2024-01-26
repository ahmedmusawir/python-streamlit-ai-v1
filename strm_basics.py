import streamlit as st
import pandas as pd
import time

st.header('Session State')

st.write(st.session_state)

if 'counter' not in st.session_state:
    st.session_state['counter'] = 0
else:
    st.session_state.counter += 1

st.write(f'Counter: {st.session_state.counter}')

st.subheader('Distance converter')


def miles_to_km():
    st.session_state.km = st.session_state.miles * 1.609

def km_to_miles():
    st.session_state.miles = st.session_state.km * 0.621

col1, buff, col2 = st.columns([2, 1, 2])

with col1:
    st.number_input('Miles: ', key='miles', on_change=miles_to_km)

with col2:
    st.number_input('Km:', key='km', on_change=km_to_miles)

st.divider()

# st.header('Progress Bar')
# st.write('Starting and extensive computation...')

# latest_iteration = st.empty()

# progress_text = 'Operation in progress. Please wait ...'
# my_bar = st.progress(0, text = progress_text)
# time.sleep(2)

# for i in range(100):
#     my_bar.progress(i + 1)
#     latest_iteration.text(f'Iteration {i + 1}')
#     time.sleep(0.1)

# st.write('We are done!')

# st.title('Sidebar & Layouts')
# Sidebar
my_select_box = st.sidebar.selectbox('Select', ['US', 'UK', 'DE', 'FR'])

st.divider()
st.title('Columns')

left_col, right_col = st.columns(2)

import random

# my_list = [12, 34, 56, 67, 90]
# list_comp = [n * 3 for n in my_list if n > 30]
# st.write(list_comp)
data = [random.random() for _ in range(100)]
# st.write(data)

with left_col:
    st.subheader('A Line Chart')
    st.line_chart(data)

# right_col.subheader('Data')
# right_col.write(data[:10])

with right_col:
    st.subheader('The Data (1st 10 of them)')
    st.write(data[:10])

st.divider()

col1, col2, col3 = st.columns([0.2, 0.5, 0.3])

with col1:
    st.write(data[:10])

with col2:
    st.line_chart(data)

with col3:
    st.write(data[11:20])

st.divider()

with st.expander('Click to expand'):
    # st.write(random.randint(2, 10))
    st.bar_chart({'Data': [random.randint(2, 10) for _ in range(25)]})

st.divider()

st.title('Streamlit Widgets:')

#Text Input
name = st.text_input('Your Name: ')

if name:
    st.write(f"Hello, {name}!")

#Number Input
x = st.number_input('Enter a number', min_value=1, max_value=99, step=1)
st.write(f'The current number is {x}')

st.divider()

clicked = st.button('Hit Me!')
if clicked:
    st.write(':ghost:' * 3)
st.divider()

#Checkbox
agree = st.checkbox('I agree')
if agree:
    'Great, you agreed!'

# Pandas Dataframe
df = pd.DataFrame({
    'Name': ['Nihad', 'Nimat', 'Bibo'],
    'Age': [3, 2, 40]
}) 

if st.checkbox('Show data'):
    st.write(df)

st.divider()

# Radio Button
pets = ['cat', 'dog', 'lama', 'lion', 'monkey']
pet = st.radio('Favorite pet', pets, index=2, key='your_pet')
# st.write(f'Your favorite pet: {pet}')
st.write(f'Your Pet is a {st.session_state.your_pet}')

st.divider()

#Select Box
cities = ['Atlanta', 'Savanna', 'Alpharetta', 'Lawrenceville']
city = st.selectbox('Your city: ', cities)
st.write(f'You live in {city}')

st.divider()

#Slider
x = st.slider('tempereture', value=.5, min_value=.1, max_value=.9, step=.1)
st.write(f'x is {x}')

st.divider()

#File Uploader
uploaded_file = st.file_uploader('Upload a file:', type=['txt', 'png', 'pdf', 'jpg', 'csv'])
if uploaded_file:
    # st.write(uploaded_file)

    if uploaded_file.type == 'text/plain':
        from io import StringIO
        stringio = StringIO(uploaded_file.getvalue().decode('utf-8'))
        string_data = stringio.read()
        st.write(string_data)
    elif uploaded_file.type == 'text/csv':
        df = pd.read_csv(uploaded_file)
        st.write(df)
    elif uploaded_file.type == 'application/pdf':
        import base64
        base64_pdf = base64.b64encode(uploaded_file.read()).decode('utf-8')
        pdf_display = f'<iframe src="data:application/pdf;base64,{base64_pdf}" width="700" height="1000" type="application/pdf"></iframe>'
        st.markdown(pdf_display, unsafe_allow_html=True)
    elif uploaded_file.type == 'image/png':
        st.image(uploaded_file)
    elif uploaded_file.type == 'image/jpeg':
        st.image(uploaded_file)
    else:
        df = pd.read_excel(uploaded_file)
    
st.divider()

# Camera Input
camera_photo = st.camera_input('Take a photo NOW!')
if(camera_photo):
    st.image(camera_photo)

st.divider()

#---------------------------------------------------------------------
#Intro
st.title('I am the King! :100:')

st.write('This is our epp!')

l1 = [1, 2, 3]

st.write(l1)

l2 = list('abc')

d1 = dict(zip(l1, l2))

st.write(d1)

# Using magic
'Showing Magic :smile:'

# Pandas Dataframe
df = pd.DataFrame({
    'Trump Votes': [1, 2, 3, 4],
    'Biden Votes': [10, 20, 30, 40]
}) 

df # This is magic which is equal to st.write(df)