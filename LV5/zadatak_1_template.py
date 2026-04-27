import numpy as np
import matplotlib
import matplotlib.pyplot as plt
from sklearn.linear_model import LogisticRegression

from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score,precision_score,recall_score
from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay 


X, y = make_classification(n_samples=200, n_features=2, n_redundant=0, n_informative=2,
                            random_state=213, n_clusters_per_class=1, class_sep=1)

# train test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=5)


#a)
plt.figure()
plt.scatter(X_train[:,0],X_train[:,1],c=y_train,cmap="bwr")
plt.scatter(X_test[:,0],X_test[:,1],c=y_test,cmap="bwr",marker="x")
plt.xlabel("x1")
plt.ylabel("x2")
plt.title("Binarni klasifikacijski problem")
plt.show()

#b)
LogRegression_model = LogisticRegression()
LogRegression_model.fit(X_train, y_train)

#c)
theta0 = LogRegression_model.intercept_[0]
theta1, theta2 = LogRegression_model.coef_[0]

print("Parametri modela:")
print("theta0 =", theta0)
print("theta1 =", theta1)
print("theta2 =", theta2)

x1 = np.linspace(X_train[:, 0].min(), X_train[:, 0].max(), 100)
x2 = (-theta0 - theta1 * x1) / theta2
plt.figure()
plt.scatter(X_train[:,0], X_train[:,1],c=y_train, cmap='bwr')
plt.plot(x1,x2,color='black', label='Granica odluke')
plt.xlabel("x1")
plt.ylabel("x2")
plt.show()

#d)

y_pred = LogRegression_model.predict(X_test)
cm = confusion_matrix(y_test, y_pred)
acc = accuracy_score(y_test, y_pred)
prec = precision_score(y_test, y_pred)
rec = recall_score(y_test, y_pred)

print("\nMatrica zabune:")
print(cm)

print("\nTočnost:", acc)
print("Preciznost:", prec)
print("Odziv:", rec)

#e)
correct=y_pred==y_test
plt.figure()
plt.scatter(X_test[correct,0],X_test[correct,1],color="green",label="Tocno")
plt.scatter(X_test[~correct,0],X_test[~correct,1],color="black",label="Tocno")
plt.xlabel("x1")
plt.ylabel("x2")
plt.show()
