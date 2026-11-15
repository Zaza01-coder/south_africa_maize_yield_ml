import streamlit as st
import pandas as pd
import joblib

st.title("🌽 South African Maize Yield Predictor")
st.write("Adjust the weather and farming inputs below to predict annual maize yield.")

# Load your trained model
model = joblib.load("maize_yield_model.joblib")

# User input sliders
year = st.slider("Year", min_value=1990, max_value=2030, value=2025)
rainfall = st.slider("Average Annual Rainfall (mm)", min_value=100, max_value=2000, value=650)
pesticides = st.number_input("Pesticides Used (tonnes)", min_value=0.0, max_value=100000.0, value=26000.0)
avg_temp = st.slider("Average Temperature (°C)", min_value=10.0, max_value=35.0, value=18.5)

if st.button("Predict Maize Yield"):
    # Build a single-row dataframe matching the model's exact training columns
    data = {col: [0] for col in model.feature_names_in_}
    input_df = pd.DataFrame(data)
    
    input_df["Year"] = year
    input_df["average_rain_fall_mm_per_year"] = rainfall
    input_df["pesticides_tonnes"] = pesticides
    input_df["avg_temp"] = avg_temp

    if "Area_South Africa" in input_df.columns:
        input_df["Area_South Africa"] = 1

    prediction_hg = model.predict(input_df)[0]
    prediction_tons = prediction_hg / 10000

    st.success(f"Predicted Yield: {prediction_hg:,.0f} hg/ha ({prediction_tons:.2f} tons per hectare)")
