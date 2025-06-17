# Exploratory Data Analysis of a Car Dataset

## 📌 Introduction

This project focuses on performing **Exploratory Data Analysis (EDA)** on a dataset of cars to uncover meaningful patterns, trends, and relationships. The dataset used is **`Cars_data.csv`**, which contains various attributes of cars such as make, model, fuel type, engine specifications, and pricing.

The EDA process followed these key steps:
- Data Loading and Initial Exploration
- Data Cleaning and Preprocessing
- Descriptive Analysis and Insights
- Data Visualization for Deeper Understanding

---

## 📥 Data Loading and Exploration

- The dataset was loaded into a **pandas DataFrame** using standard CSV loading techniques.
- **Initial Dataset Shape:** `n_rows x n_columns` (e.g., 11914 rows × 15 columns).
- **Missing Values Handling:**
  - Replaced **0s in key numeric fields** with `NaN` (e.g., `Engine HP`, `Engine Cylinders`).
  - Dropped rows with missing values to ensure analysis accuracy.
  - **Dataset Shape After Cleaning:** Reduced to a smaller, cleaner subset.

- **Column Data Types:**
  - Object (Categorical): `Make`, `Model`, `Transmission Type`, `Vehicle Size`, etc.
  - Integer/Float: `Engine HP`, `Engine Cylinders`, `MSRP`, `Highway MPG`, `City MPG`.

---

## 📊 Data Analysis

### 🔠 Categorical Columns:

- **Unique Car Makes:** Many makes, with **Chevrolet** being the most frequent.
- **Transmission Types:** Multiple types; **AUTOMATIC** was the most common.
- **Fuel Type:** Most cars used **regular unleaded** fuel.
- **Vehicle Size:** Most cars fell under **Midsize** or **Compact** categories.
- **Vehicle Style:** Varied styles such as **Sedan**, **SUV**, **Convertible**, etc.

### 🔢 Numerical Columns:

- **Average MSRP by Make:**
  - Luxury brands like **Bugatti**, **Maybach**, and **Rolls-Royce** had the **highest average prices**.
- **Correlation Insights:**
  - **Engine HP vs Engine Cylinders:** Strong positive correlation (~0.91)
  - **Engine HP vs MSRP:** Moderate positive correlation (~0.66)
  - **MPG (Highway/City) vs Engine Specs:** Notable **negative correlations** — higher horsepower/cylinders generally lead to lower fuel efficiency.

---

## 📈 Data Visualization

The following visualizations were created to better understand the data:

- **Histograms:** To observe the distribution of numeric values like MSRP, Engine HP, and MPG.
- **Bar Charts:** For categorical variables such as `Make`, `Transmission Type`, and `Vehicle Style`.
- **Scatter Plots:** 
  - `Engine HP` vs `MSRP`
  - `Highway MPG` vs `City MPG`
- **Heatmap:** 
  - Displayed a correlation matrix highlighting strong and weak relationships among numeric features.

### 🧠 Key Insights from Visuals:

- **Skewed Distributions:** MSRP and Engine HP were heavily right-skewed due to luxury brands.
- **Trends:** Positive trend between Engine HP and MSRP in scatter plots.
- **Correlation Heatmap:** Helped quickly identify which numerical variables had strong or weak associations.

---

## ✅ Summary and Conclusion

- **Main Findings:**
  - **Chevrolet** was the most frequent car make.
  - **Automatic transmissions** dominated the dataset.
  - **High-end brands** significantly skewed MSRP and horsepower averages.
  - **Engine HP and Engine Cylinders** had a strong correlation.
  - **Higher performance** usually meant **lower fuel efficiency**.

- **Interesting Patterns:**
  - Luxury vehicles not only cost more but also tend to have more powerful engines and lower MPG ratings.
  - Compact and midsize vehicles are more prevalent and fuel-efficient.

- **Next Steps:**
  - Predictive modeling (e.g., predict MSRP or MPG based on car features).
  - Feature engineering for improving model accuracy.
  - Deep dives into brand-specific trends or engine configurations.

---

## 📁 File Structure

📦Car_EDA_Project/
┣ 📄 Cars_data.csv
┣ 📄 Car_EDA.ipynb
┗ 📄 README.md




---

## 🛠️ Tools & Libraries Used

- Python 3.x
- pandas
- matplotlib
- seaborn
- numpy
- Jupyter Notebook

---

## 📬 Contact

For any questions or suggestions, feel free to reach out at:  
**📧 bhardwaj520gopal.com**

---



