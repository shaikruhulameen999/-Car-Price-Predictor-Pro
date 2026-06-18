🚗 AutoValue AI - Used Car Price Prediction System

An end-to-end Machine Learning Web Application that predicts the market value of used cars based on vehicle specifications and historical data. This project uses K-Nearest Neighbors (KNN) Regression, data preprocessing pipelines, and an interactive Streamlit dashboard for real-time predictions.

📌 Project Overview

The Used Car Price Prediction System helps users estimate the resale value of a vehicle by analyzing multiple car attributes such as brand, model, fuel type, mileage, engine capacity, ownership history, and more.

The system automates the complete machine learning workflow including:

Data Cleaning
Exploratory Data Analysis (EDA)
Feature Engineering
Data Preprocessing
Model Training
Model Evaluation
Deployment using Streamlit
🎯 Features

✅ Real-Time Price Prediction

✅ Interactive Streamlit Dashboard

✅ Automated Data Preprocessing Pipeline

✅ Machine Learning-Based Predictions

✅ User-Friendly Interface

✅ Responsive Professional Design

🛠 Technologies Used
Programming Language
Python
Libraries
Pandas
NumPy
Scikit-Learn
Streamlit
Joblib
Matplotlib
Seaborn
Machine Learning
K-Nearest Neighbors (KNN) Regression
One-Hot Encoding
MinMax Scaling
ColumnTransformer
📊 Dataset Features

The model predicts car prices using the following features:

Feature
Brand
Model
Fuel Type
Transmission
Owner Type
Color
City
Year
Mileage (kmpl)
Engine CC
Horsepower
Kms Driven
Insurance Valid
Service History
Accidents
Tax Paid
Number of Doors
Seats
Registration Age
🔄 Machine Learning Workflow
1. Data Collection

Used Car Price Dataset containing vehicle specifications and selling prices.

2. Data Preprocessing
Missing Value Handling
Duplicate Removal
Feature Selection
Data Transformation
3. Feature Engineering

Categorical Features:

Brand
Model
Fuel Type
Transmission
Owner Type
Color
City

Numerical Features:

Year
Mileage
Engine Capacity
Horsepower
Kms Driven
Service History
Accidents
Registration Age
4. Encoding & Scaling
OneHotEncoder
MinMaxScaler
5. Model Training

K-Nearest Neighbors Regressor (KNN)

6. Model Evaluation

Evaluation Metrics:

MAE (Mean Absolute Error)
MSE (Mean Squared Error)
RMSE (Root Mean Squared Error)
R² Score
🚀 Streamlit Application

The web application allows users to:

Enter vehicle details.
Submit vehicle information.
Generate predicted market value instantly.
View results through a professional dashboard.
📂 Project Structure
AutoValue-AI/
│
├── app_user.py
├── model.pkl
├── transformer.pkl
├── requirements.txt
├── used_car_price_prediction_1M.csv
├── car_prediction.ipynb
│
├── screenshots/
│   ├── dashboard.png
│   └── prediction.png
│
└── README.md
⚙️ Installation

Clone the repository:

git clone https://github.com/yourusername/AutoValue-AI.git

Move into project folder:

cd AutoValue-AI

Create virtual environment:

python -m venv venv

Activate virtual environment:

Windows
venv\Scripts\activate
Linux/Mac
source venv/bin/activate

Install dependencies:

pip install -r requirements.txt
▶️ Run Application
streamlit run app_user.py
📈 Future Enhancements
Car Image Recognition
Vehicle Condition Analysis
Deep Learning Models
Random Forest & XGBoost Comparison
Price Trend Visualization
Cloud Deployment
User Authentication
PDF Report Generation
Recommendation System
🎓 Learning Outcomes

This project helped in understanding:

Machine Learning Pipelines
Feature Engineering
Data Preprocessing
Model Deployment
Streamlit Development
Real-Time Prediction Systems
👨‍💻 Author

Shaik Ruhul Ameen

Machine Learning & Computer Vision Enthusiast

🙏 Acknowledgements

Special thanks to:

Sonam Mam
Upendra Sir

for their valuable guidance, support, and encouragement throughout the project development process.

⭐ If you like this project

Give this repository a ⭐ on GitHub and share your feedback!

"Transforming Data into Intelligent Predictions with Machine Learning." 🚗📊🤖
