import pandas as pd
#a
data=pd.read_csv("LV3\data_C02_emission.csv")
print("Broj mjerenja:\n",len(data))
print("Tipovi veličina:\n",data.dtypes)
print("Izostale vrijednosti:\n",data.isnull().sum())
print("Duplicirane vrijednosti:",data.duplicated().sum())
data=data.dropna()
data=data.drop_duplicates()
data = data.reset_index(drop=True)
print(len(data))

#b
print("3 vozila s najvećom gradskom potrošnjom:\n")
print(data.nlargest(3, "Fuel Consumption City (L/100km)")[["Make","Model","Fuel Consumption City (L/100km)"]])
print("\n3 vozila s najmanjom gradskom potrošnjom:\n")
print(data.nsmallest(3, "Fuel Consumption City (L/100km)")[["Make","Model","Fuel Consumption City (L/100km)"]])

#c
filtered=data[(data["Engine Size (L)"]>=2.5) & (data["Engine Size (L)"]<=3.5)]
print("Broj vozila  s velicinom motora izmedu 2.5 i 3.5 L:",len(filtered))
print("Prosjecna CO2 emisija plinova za ova vozila:",filtered["CO2 Emissions (g/km)"].mean())

#d
audi=data[data["Make"]=="Audi"]
print("Broj mjerenja audia:",len(audi))
audi_4c=audi[audi["Cylinders"]==4]
print("Prosjecna emisija CO2 audia s 4 cilindra:",audi_4c["CO2 Emissions (g/km)"].mean())

#e
cylinder4=data[data["Cylinders"]==4]
cylinder6=data[data["Cylinders"]==6]
cylinder8=data[data["Cylinders"]==8]
cylinder12=data[data["Cylinders"]==12]

print("Prosjecna emisija CO2 auta s 4 cilindra:",cylinder4["CO2 Emissions (g/km)"].mean())
print("Prosjecna emisija CO2 auta s 6 cilindra:",cylinder6["CO2 Emissions (g/km)"].mean())
print("Prosjecna emisija CO2 auta s 8 cilindra:",cylinder8["CO2 Emissions (g/km)"].mean())
print("Prosjecna emisija CO2 auta s 12 cilindra:",cylinder12["CO2 Emissions (g/km)"].mean())

#f
diesel=data[data["Fuel Type"]=="D"]
benzin=data[data["Fuel Type"]=="X"]
print("Dizel potrošnja:",diesel["Fuel Consumption City (L/100km)"].median())
print("Regularni benzin potrošnja",benzin["Fuel Consumption City (L/100km)"].median())

#g
diesel4=data[(data["Fuel Type"]=="D") & (data["Cylinders"]==4)]
car =diesel4.sort_values(by="Fuel Consumption City (L/100km)",
                         ascending=False).head(1)
print("\nDizel vozilo s 4 cilindra s najvećom potrošnjom:")
print(car[["Make","Model","Fuel Consumption City (L/100km)"]])

#h
manual = data[data["Transmission"].str.contains("M")]

print("\nBroj vozila s ručnim mjenjačem:", manual.shape[0])

#i
corr = data.corr(numeric_only=True)

print("\nKorelacija numeričkih varijabli:")
print(corr)









