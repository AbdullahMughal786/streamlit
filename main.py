# Importing librarires
import streamlit as st
import division as div
import multiplication as mul
import subtract as sub
import sum as s


st.title("Welcome to the Calculator")   # for Title

num1 = st.number_input("Enter your 1st number: ")   # for taking input from user
operator = st.radio("Enter your operator: ",('Add','Subtract','Multiply','Division'))   # for taking input from user
num2 = st.number_input("Enter your 2nd number: ")   # for taking input from user

if (st.button("Calculate")):        # st.button("Calculate") creates the button and if button is pressed it returns True otherwise False

    if operator=='Add':
        result = s.sum(num1,num2)
        st.success(f"Your result is: {result}")
    elif operator=="Subtract":
        result = sub.subt(num1,num2)
        st.success(f"Your result is: {result}")
    elif operator=="Multiply":
        result = mul.mult(num1,num2)
        st.success(f"Your result is: {result}")

    elif operator == "Division":
        try:
            result = div.div(num1, num2)
        except ZeroDivisionError as e:
            st.error(f"Error: {e} Please try again")
        else:
            st.success(f"Your result is: {result}")