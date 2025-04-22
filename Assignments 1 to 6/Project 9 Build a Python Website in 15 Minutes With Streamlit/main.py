import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title('My Data Dashboard')

uploaded_file = st.file_uploader("Choose a file", type=['csv', 'xlsx'])

df = None

if uploaded_file is not None:
    st.write('File uploaded successfully')

    file_extension = uploaded_file.name.split('.')[-1]
    try:
        if file_extension == 'csv':
            df = pd.read_csv(uploaded_file)

        elif file_extension == 'xlsx':
            df = pd.read_excel(uploaded_file)

        st.subheader('Data Preview')
        st.write(df.head())

        st.subheader('Data Summary')
        st.write(df.describe())
        if not df.empty:
            st.subheader('Filter')
            columns = df.columns.tolist()
            selected_column = st.selectbox("Select Column", columns)
            unique_items = df[selected_column].unique()
            selected_values = st.multiselect("Select Values", unique_items)
            if selected_values:
                filtered_data = df[df[selected_column].isin(selected_values)]
                st.subheader("Filtered Data")
                st.write(filtered_data)
        else:
            st.write('No data to display')

        st.subheader('Plot Data')
        x_column = st.selectbox("Select X-axis", columns)
        y_column = st.selectbox("Select Y-axis", columns)
        df[y_column] = pd.to_numeric(df[y_column], errors="coerce")

        if st.button('Generate Plot'):
            st.line_chart(filtered_data.set_index(x_column)[y_column])
    except:
        st.write('An error occured while reading the file')
else:
    st.write('Please upload a file')