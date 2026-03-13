import streamlit as st
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

# Load data from CSV (Ensure the file has "HoursStudied" and "ExamScore" columns)
df = pd.read_csv("data.csv")

# Split data into Features (X) and Target (y)
X = df[['HoursStudied']]
y = df['ExamScore']

# Train-Test Split (80% training, 20% testing)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train the model
model = LinearRegression()
model.fit(X_train, y_train)

# Streamlit User Interface
st.title("📚 Exam Score Predictor")
st.write("Enter hours studied to predict the exam score.")

# User Input
hours = st.number_input("Hours Studied:", min_value=0.0, step=0.1)

# Predict Button
if st.button("Predict Score"):
    # Reshape input to 2D array for the model
    predicted_score = model.predict([[hours]])[0]
    st.success(f"✅ Predicted Score: {predicted_score:.2f}")

# Show Sample Data
st.write("### 📊 Sample Training Data")
st.dataframe(df)
