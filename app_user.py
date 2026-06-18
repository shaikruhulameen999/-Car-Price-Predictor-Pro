
import streamlit as st
import pandas as pd
import joblib

# ----------------------------
# PAGE CONFIG
# ----------------------------

st.set_page_config(
    page_title="Used Car Price Prediction",
    page_icon="🚗",
    layout="wide"
)

# ----------------------------
# LOAD MODEL
# ----------------------------

model = joblib.load("model (1).pkl")
transformer = joblib.load("transformer_new.pkl")

# ----------------------------
# CUSTOM CSS
# ----------------------------

st.markdown("""
<style>

.stApp {
    background: linear-gradient(135deg, #0f172a, #1e293b);
    color: white;
}

.main-title {
    text-align:center;
    font-size:45px;
    font-weight:bold;
    color:#38bdf8;
    margin-bottom:10px;
}

.subtitle {
    text-align:center;
    font-size:18px;
    color:#cbd5e1;
    margin-bottom:30px;
}

.block-container {
    padding-top: 2rem;
}

.stTextInput > div > div > input,
.stNumberInput input {
    border-radius:10px;
    border:2px solid #38bdf8;
}

.stSelectbox > div > div {
    border-radius:10px;
}

.stButton button {
    width:100%;
    height:55px;
    font-size:18px;
    font-weight:bold;
    background-color:#38bdf8;
    color:white;
    border-radius:12px;
}

.prediction-box {
    background:#0ea5e9;
    padding:25px;
    border-radius:15px;
    text-align:center;
    font-size:30px;
    font-weight:bold;
    color:white;
    margin-top:20px;
}

</style>
""", unsafe_allow_html=True)

# ----------------------------
# HEADER
# ----------------------------

st.markdown(
    '<div class="main-title">🚗 Used Car Price Prediction System</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">AI Powered Vehicle Price Estimation Platform</div>',
    unsafe_allow_html=True
)

# ----------------------------
# INPUTS
# ----------------------------

col1, col2 = st.columns(2)

with col1:

    brand = st.text_input("Brand", "Maruti")

    model_name = st.text_input("Model", "Swift")

    fuel_type = st.selectbox(
        "Fuel Type",
        ["Petrol", "Diesel", "CNG", "Electric"]
    )

    transmission = st.selectbox(
        "Transmission",
        ["Manual", "Automatic"]
    )

    owner_type = st.selectbox(
        "Owner Type",
        ["First", "Second", "Third"]
    )

    color = st.text_input("Color", "White")

    city = st.text_input("City", "Hyderabad")

with col2:

    year = st.number_input(
        "Year",
        min_value=2000,
        max_value=2030,
        value=2020
    )

    mileage = st.number_input(
        "Mileage (kmpl)",
        value=20.0
    )

    engine_cc = st.number_input(
        "Engine CC",
        value=1200
    )

    horsepower = st.number_input(
        "Horsepower",
        value=80
    )

    kms_driven = st.number_input(
        "Kms Driven",
        value=50000
    )

    insurance_valid = st.number_input(
        "Insurance Valid",
        value=1
    )

    service_history = st.number_input(
        "Service History",
        value=5
    )

    accidents = st.number_input(
        "Accidents",
        value=0
    )

    tax_paid = st.number_input(
        "Tax Paid",
        value=1
    )

    number_of_doors = st.number_input(
        "Number of Doors",
        value=4
    )

    seats = st.number_input(
        "Seats",
        value=5
    )

    registration_age = st.number_input(
        "Registration Age",
        value=3
    )

# ----------------------------
# PREDICTION
# ----------------------------

if st.button("Predict Price"):

    input_df = pd.DataFrame({
        "Brand": [brand],
        "Model": [model_name],
        "Fuel_Type": [fuel_type],
        "Transmission": [transmission],
        "Owner_Type": [owner_type],
        "Color": [color],
        "City": [city],
        "Year": [year],
        "Mileage_kmpl": [mileage],
        "Engine_CC": [engine_cc],
        "Horsepower": [horsepower],
        "Kms_Driven": [kms_driven],
        "Insurance_Valid": [insurance_valid],
        "Service_History": [service_history],
        "Accidents": [accidents],
        "Tax_Paid": [tax_paid],
        "Number_of_Doors": [number_of_doors],
        "Seats": [seats],
        "Registration_Age": [registration_age]
    })

    transformed_data = transformer.transform(input_df)

    prediction = model.predict(transformed_data)

    st.markdown(
        f"""
        <div class="prediction-box">
            Estimated Market Value <br><br>
            ₹ {prediction[0]:,.2f}
        </div>
        """,
        unsafe_allow_html=True
    )

    st.markdown("### 📊 Vehicle Summary")

    c1, c2, c3 = st.columns(3)

    with c1:
        st.metric("Vehicle Age", 2026 - year)

    with c2:
        st.metric("Mileage", f"{mileage} kmpl")

    with c3:
        st.metric("KMs Driven", f"{kms_driven:,}")

    st.success("Prediction Generated Successfully!")