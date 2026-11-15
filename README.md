# 🌽 South African Maize Yield Prediction Using Machine Learning

## 📌 Problem Statement
Maize is South Africa's primary staple crop, vital for national food security and rural livelihoods. However, erratic rainfall and temperature shifts make annual harvests difficult to predict. This project uses historical weather, pesticide usage, and agricultural trends to predict annual maize yield (in hg/ha), helping farmers and planners make informed decisions on storage, financing, and supply.

---

## 📊 Key Results & Model Recommendation
* **Recommended Model:** Random Forest Regressor
* **R² Score (Test Set):** `0.964` (explains **96.4%** of yield variation)
* **Mean Absolute Error (MAE):** `2,351.75 hg/ha` (~`0.24 tons/hectare`)

### Engineering Journey
1. **Baseline Model (South Africa Only):** Training strictly on South African historical rows achieved an **R² of 0.37** due to limited annual records.
2. **Global Transfer & Encoding:** Expanding the dataset to include global maize records with One-Hot Encoded country features (`Area`) and `Year` trends boosted accuracy to **0.964**.

---

## 📈 Visuals

### Actual vs. Predicted Yield (South Africa)
![South Africa Maize Prediction](sa_maize_prediction.png)

### Top Factors Driving Maize Yield
![Feature Importance](feature_importance.png)

---

## 🛠️ Tech Stack & Workflow
* **Language:** Python
* **Libraries:** Pandas, NumPy, Scikit-Learn, Matplotlib, Seaborn, Joblib
* **Workflow:** Data Cleaning ➔ Exploratory Data Analysis ➔ One-Hot Encoding ➔ Train/Test Split ➔ Random Forest Regression ➔ Model Serialization

---

## 🚀 Future Improvements
* Incorporate **monthly seasonal rainfall** rather than annual averages to capture dry spells during critical planting windows.
* Integrate local **soil moisture and nutrient data** at the South African provincial level.
