import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import MinMaxScaler
from matplotlib.colors import ListedColormap
from sklearn.metrics import confusion_matrix, accuracy_score, classification_report
from sklearn.model_selection import train_test_split


labels= {0:'Adelie', 1:'Chinstrap', 2:'Gentoo'}

def plot_decision_regions(X, y, classifier, resolution=0.02):
    plt.figure()
    # setup marker generator and color map
    markers = ('s', 'x', 'o', '^', 'v')
    colors = ('red', 'blue', 'lightgreen', 'gray', 'cyan')
    cmap = ListedColormap(colors[:len(np.unique(y))])
    
    # plot the decision surface
    x1_min, x1_max = X[:, 0].min() - 1, X[:, 0].max() + 1
    x2_min, x2_max = X[:, 1].min() - 1, X[:, 1].max() + 1
    xx1, xx2 = np.meshgrid(np.arange(x1_min, x1_max, resolution),
    np.arange(x2_min, x2_max, resolution))
    Z = classifier.predict(np.array([xx1.ravel(), xx2.ravel()]).T)
    Z = Z.reshape(xx1.shape)
    plt.contourf(xx1, xx2, Z, alpha=0.3, cmap=cmap)
    plt.xlim(xx1.min(), xx1.max())
    plt.ylim(xx2.min(), xx2.max())
    
    # plot class examples
    for idx, cl in enumerate(np.unique(y)):
        plt.scatter(x=X[y == cl, 0],
                    y=X[y == cl, 1],
                    alpha=0.8,
                    c=colors[idx],
                    marker=markers[idx],
                    edgecolor = 'w',
                    label=labels[cl])

# ucitaj podatke
df = pd.read_csv("LV5\penguins.csv")

# izostale vrijednosti po stupcima
print(df.isnull().sum())

# spol ima 11 izostalih vrijednosti; izbacit cemo ovaj stupac
df = df.drop(columns=['sex'])

# obrisi redove s izostalim vrijednostima
df.dropna(axis=0, inplace=True)

# kategoricka varijabla vrsta - kodiranje
df['species'].replace({'Adelie' : 0,
                        'Chinstrap' : 1,
                        'Gentoo': 2}, inplace = True)

print(df.info())

# izlazna velicina: species
output_variable = ['species']

# ulazne velicine: bill length, flipper_length
input_variables = ['bill_length_mm',
                    'flipper_length_mm']

X = df[input_variables].to_numpy()
y = df[output_variable].to_numpy()

# podjela train/test
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 123)


species_mapping = {'Adelie':0, 'Chinstrap':1, 'Gentoo':2}
df['species'] = df['species'].map(species_mapping)


X_train = X_train.astype(float)
X_test = X_test.astype(float)

# mapiraj y_train i y_test na integer koristeći dictionary
y_train = np.array([species_mapping[s] for s in y_train.ravel()]).astype(int)
y_test  = np.array([species_mapping[s] for s in y_test.ravel()]).astype(int)


#a)
# Broj primjera po klasama u train i test skupu
classes, train_counts = np.unique(y_train, return_counts=True)
classes, test_counts = np.unique(y_test, return_counts=True)

print("Train skup:", train_counts)
print("Test skup:", test_counts)

x = np.arange(len(classes)) 
width = 0.4

plt.figure()
plt.bar(x-width/2, train_counts, width, label='Train', color='blue')
plt.bar(x+width/2, test_counts, width, label='Test', color='red')

plt.xticks(x, classes)
plt.xlabel("Vrsta pingvina")
plt.ylabel("Broj primjera")
plt.title("Broj primjera po klasama")
plt.legend()
plt.show()

#b)


LogRegression_model = LogisticRegression()
LogRegression_model.fit(X_train, y_train)

#c)
print("\nIntercepti:", LogRegression_model .intercept_)
print("Koeficijenti:\n", LogRegression_model .coef_)

#d)

plot_decision_regions(X_train,y_train,LogRegression_model)

plt.show()

#e)

y_pred = LogRegression_model.predict(X_test)

print("\n--- Evaluacija na test skupu (2 feature-a) ---")
print("Matrica zabune:\n", confusion_matrix(y_test, y_pred))
print("Točnost:", accuracy_score(y_test, y_pred))
print("\nClassification report:\n", classification_report(y_test, y_pred))


#f)
input_vars_full = ['bill_length_mm', 'flipper_length_mm', 'bill_depth_mm', 'body_mass_g']



