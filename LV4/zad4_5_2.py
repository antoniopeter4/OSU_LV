import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn . model_selection import train_test_split
from sklearn.preprocessing import StandardScaler,OneHotEncoder
import sklearn . linear_model as lm
from sklearn . metrics import mean_squared_error,mean_absolute_error,mean_absolute_percentage_error,r2_score

data=pd.read_csv("LV4\data_C02_emission.csv")

numerical=[
    "Engine Size (L)",
    "Cylinders",
    "Fuel Consumption City (L/100km)",
    "Fuel Consumption Hwy (L/100km)",
    "Fuel Consumption Comb (L/100km)"]

X=data[numerical]
y=data["CO2 Emissions (g/km)"]

X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.2,random_state=1)


ohe = OneHotEncoder(sparse=False)
fuel_encoded = ohe.fit_transform(data[['Fuel Type']])