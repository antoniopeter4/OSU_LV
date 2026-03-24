import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn . model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
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

plt.figure()
plt.scatter(X_train["Cylinders"],y_train,color="blue",label="Train")
plt.scatter(X_test["Cylinders"],y_test,color="red",label="Test")
plt.xlabel("Engine Size (L)")
plt.ylabel("CO2 Emissions")
plt.legend()
plt.title("Ovisnost CO2 o veličini motora")
plt.show()


sc=StandardScaler()
X_train_sc=sc.fit_transform(X_train)
X_test_sc=sc.fit_transform(X_test)
plt.figure()
plt.hist(X_train["Cylinders"],bins=20)
plt.title("Prije skaliranja")
plt.show()

plt.figure
plt.hist(X_train_sc[:,0],bins=20)
plt.title("Poslije skaliranja")
plt.show()

linearModel=lm.LinearRegression()
linearModel.fit(X_train_sc,y_train)
print("Intercep (θ0):",linearModel.intercept_)
print("Koficijent (θ):",linearModel.coef_)

y_test_p=linearModel.predict(X_test_sc)
plt.figure()
plt.scatter(y_test,y_test_p)
plt.xlabel("Stvarna vrijednost")
plt.ylabel("Predikcija")
plt.show()

MSE=mean_squared_error(y_test,y_test_p)
RMSE=np.sqrt(MSE)
MAE=mean_absolute_error(y_test,y_test_p)
MAPE=mean_absolute_percentage_error(y_test,y_test_p)
R2=r2_score(y_test,y_test_p)
print("Evaualcija:\n")
print("MSE:",MSE)
print("RMSE:",RMSE)
print("MAE:",MAE)
print("MAPE:",MAPE)
print("R2:",R2)







