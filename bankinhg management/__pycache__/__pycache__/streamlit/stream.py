import streamlit as st
import pandas as pd
import numpy as np
st.title('📊 CSV Data Dashboard')
name=st.text_input('Enter your name')
file=st.file_uploader('Upload your CSV',type=['csv'])
if file is not None:
    if st.button('Show',type='primary'):
        st.session_state.data=pd.read_csv(file)
        st.session_state.show_data=True
    if st.session_state.get('show_data',False):
        st.success(f'Welcome {name} to dashboard')
        st.subheader('CSV Data')
        st.dataframe(st.session_state.data)
        if st.button('Delete NULL Values'):
            null_values=st.session_state.data.isnull()
            total_null=np.sum(null_values.values)
            if total_null>0:
                st.session_state.data=st.session_state.data.dropna()
                st.success('NULL values deleted successfully!')
            else:
                st.info('There are no NULL values in the data.')
            st.dataframe(st.session_state.data)
            csv=st.session_state.data.to_csv(index=False)
            st.download_button('Save CSV',csv,'updated_data.csv','text/csv')
else:
    st.info('Please upload your CSV file first.')