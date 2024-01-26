import streamlit as st
import re


# App title
st.title("Keyword Density Checker")
st.divider()

# A text area input to collect the paragraph
text = st.text_area('Drop a Paragraph here...')
# st.subheader("The Density Report:")
st.divider()

# Declaring Keyword List
words_dict = dict()

# Declaring Columns
col1, col2, col3 = st.columns(3)


if text:
    col1.markdown(f"<u><h4>Keyword</h4></u>", unsafe_allow_html=True)
    col2.markdown(f"<u><h4>Occurance</h4></u>", unsafe_allow_html=True)
    col3.markdown(f"<u><h4>Percentage</h4></u>", unsafe_allow_html=True)
    # Using re (regular expression) to filter out punctuations
    sim_text = re.sub("[,.?!&*;:]", '', text)

    # Collecting words in an array or list
    words = sim_text.lower().split(" ")
    total_length = len(words)

    for word in words:
        if word in words_dict:
            words_dict[word] = words_dict[word] + 1
        else:
            words_dict[word] = 1

    keys = list(words_dict.keys())
    values = list(words_dict.values())


    for i in range(len(keys)):
        col1.markdown(f"<h5>{keys[i]}</h5>", unsafe_allow_html=True)
        col2.markdown(f"<h5>{values[i]}</h5>", unsafe_allow_html=True)
        col3.markdown(f"<h5>{values[i] / total_length * 100:.2f}%</h5>", unsafe_allow_html=True)
     


    # st.write(words_dict)