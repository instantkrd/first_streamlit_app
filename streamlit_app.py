import streamlit 
import pandas
streamlit.title('abcd')
streamlit.header('efgh')
streamlit.text('ijkl')
streamlit.text('mnop')
streamlit.text('qrst')
streamlit.header('uvwx')

my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
streamlit.dataframe(my_fruit_list)
