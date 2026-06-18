import pandas as pd
import joblib

from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder, MinMaxScaler

df = pd.read_csv("used_car_price_prediction_1M.csv")

df = df.dropna().drop_duplicates()

X = df.drop("Price", axis=1)

categorical_cols = [
    'Brand',
    'Model',
    'Fuel_Type',
    'Transmission',
    'Owner_Type',
    'Color',
    'City'
]

numerical_cols = [
    'Year',
    'Mileage_kmpl',
    'Engine_CC',
    'Horsepower',
    'Kms_Driven',
    'Insurance_Valid',
    'Service_History',
    'Accidents',
    'Tax_Paid',
    'Number_of_Doors',
    'Seats',
    'Registration_Age'
]

transformer = ColumnTransformer(
    transformers=[
        ("cat", OneHotEncoder(handle_unknown="ignore"), categorical_cols),
        ("num", MinMaxScaler(), numerical_cols)
    ]
)

transformer.fit(X)

joblib.dump(transformer, "transformer_new.pkl")

print("transformer_new.pkl created successfully")