import streamlit as st
import pandas as pd

# Navigator (Multi page apps)
st.sidebar.title("Navigator")
page = st.sidebar.selectbox("Choose Page", ["Home", 
                                            "Prediction", 
                                            "Effects", 
                                            "DataFrame"])
### HOME ----------------------------------------------------
if page == "Home":
    st.title("ML Demo")
    st.header("Prediction Sysytem")
    st.subheader("Enter Inputs Below")

    st.write("This app demonstrates ML model Deployment")
    # Text input
    name = st.text_input("Enter Customer name")
    age = st.number_input("Enter Age", min_value=1, max_value=100)
    # Slider
    salary = st.slider("Select Salary", 10000, 100000)
    # select box/drop down
    Gender = st.selectbox("Select Gender", ["Male", "Female"])
    # Radio button
    education = st.radio("Education Level", ["UG", "PG", "PhD"])
    # Check box
    agree = st.checkbox("I agree to terms")
    # File Upload
    uploaded_file = st.file_uploader("Upload Image", type=["jpg", "png"])
    # Button for prediction
    if st.button("Predict"):
        # result = model.predict([[Gender, salary, age]])
        st.success("Prediction Successful")

# -----------------------------------------------------------------
# Prediction Section ----------------------------------------------------
elif page == "Prediction":
    if st.button("Rejected"):
        st.error("The application is rejected")

    if st.button("Check Input"):
        st.warning("Type the input properly")

    # Displaying the written text
    user_input = st.text_input("Enter Something")
    if st.button("Submit to Backend"):
        if user_input:
            result = user_input
            st.success(result)
        else:
            st.warning("Please enter something first!")

# -------------------------------------------------------------------------
# Effects page ------------------------------------------------------------
elif page == "Effects":
    # Effects
    col1, col2 = st.columns(2)
    with col1:
        if st.button("Balloons"):
            st.balloons()
    with col2:
        if st.button("Snow"):
            st.snow()

elif page == "DataFrame":
    # DataFrame
    df = pd.DataFrame({"A":[1, 2, 3, 4], "B":[56, 76, 87, 89]})
    st.dataframe(df)

    # new_up = st.file_uploader("Upload csv/excel file", type=["csv", "xlsx"])
    # if new_up is not None:
    #     file = pd.read_csv(new_up)
    # else:
    #     file = pd.read_excel(new_up)

    #     # Show first 10 rows
    #     st.subheader("Preview first 10 rows")
    #     st.dataframe(file.head(10))

