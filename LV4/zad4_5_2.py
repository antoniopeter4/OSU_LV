import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn . model_selection import train_test_split
from sklearn.preprocessing import StandardScaler,OneHotEncoder
import sklearn . linear_model as lm
from sklearn . metrics import mean_squared_error,mean_absolute_error,mean_absolute_percentage_error,r2_score

data=pd.read_csv("LV4\data_C02_emission.csv")

# Numeričke ulazne veličine
numerical = [
    "Engine Size (L)",
    "Cylinders",
    "Fuel Consumption City (L/100km)",
    "Fuel Consumption Hwy (L/100km)",
    "Fuel Consumption Comb (L/100km)"
]

# 1-od-K kodiranje kategoričke varijable Fuel Type
ohe = OneHotEncoder(sparse_output=False)
X_encoded = ohe.fit_transform(data[["Fuel Type"]])

# Spajanje numeričkih i enkodiranih stupaca
X_numerical = data[numerical].to_numpy()
X = np.concatenate([X_numerical, X_encoded], axis=1)
y = data["CO2 Emissions (g/km)"].to_numpy()

# Podjela na skup za učenje i testiranje
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=1)

# Izgradnja modela - bez skaliranja
linearModel = LinearRegression()
linearModel.fit(X_train, y_train)

print("Intercept (θ0):", linearModel.intercept_)
print("Koeficijenti (θ):", linearModel.coef_)

# Procjena na testnom skupu
y_test_p = linearModel.predict(X_test)

# Dijagram raspršenja
plt.figure()
plt.scatter(y_test, y_test_p)
plt.xlabel("Stvarna vrijednost")
plt.ylabel("Predikcija")
plt.title("Stvarne vs predviđene vrijednosti CO2")
plt.show()

# Evaluacija
MSE  = mean_squared_error(y_test, y_test_p)
RMSE = np.sqrt(MSE)
MAE  = mean_absolute_error(y_test, y_test_p)
MAPE = mean_absolute_percentage_error(y_test, y_test_p)
R2   = r2_score(y_test, y_test_p)

print("\nEvaluacija:")
print("MSE:", MSE)
print("RMSE:", RMSE)
print("MAE:", MAE)
print("MAPE:", MAPE)
print("R2:", R2)

# Maksimalna greška
errors = np.abs(y_test - y_test_p)
max_idx = np.argmax(errors)

print("\nMaksimalna greška:", errors[max_idx], "g/km")
print("Marka:", data.iloc[max_idx]["Make"])
print("Model:", data.iloc[max_idx]["Model"])
