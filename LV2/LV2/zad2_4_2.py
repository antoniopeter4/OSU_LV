import numpy as np
import matplotlib.pyplot as plt

data=np.loadtxt("data.csv",delimiter=",",skiprows=1)

print ("Broj osoba:",data.shape[0])

visina=data[:,1]
masa=data[:,2]
plt.scatter(visina,masa)
plt.title("Odnos visine i mase")
plt.xlabel("visina u cm")
plt.ylabel("masa u kg")
plt.show()

plt.scatter(visina[::50],masa[::50])
plt.show()

print("Mnimalna visina je:",np.min(visina))
print("Maksimalna visina je:",np.max(visina))
print("Srednja visina je:",np.mean(visina))

muskarci=data[data[:,0]==1]
muskarci_v=muskarci[:,1]
zene=data[data[:,0]==1]
zene_v=zene[:,1]
print("Minimalna visina muskaraca je:",np.min(muskarci_v))
print("Maksimalna visina muskaraca je:",np.max(muskarci_v))
print("Srednja visina muskaraca je:",np.mean(muskarci_v))
print("Minimalna visina zena je:",np.min(zene_v))
print("Maksimalna visina zena je:",np.max(zene_v))
print("Srednja visina zena je:",np.mean(zene_v))









