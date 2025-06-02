# app.py
import streamlit as st
from power_calc import calculate_powers

st.title("Power Calculator")
st.write("Enter a number to calculate its square, cube, and fifth power")

n = st.number_input("Enter an integer", value=1, step=1)

results = calculate_powers(n)

st.write(f"The square of {n} is: {results['square']}")
st.write(f"The cube of {n} is: {results['cube']}")
st.write(f"The fifth power of {n} is: {results['fifth_power']}")
