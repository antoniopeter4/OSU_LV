import numpy as np
from tensorflow import keras
from matplotlib import pyplot as plt

# broj klasa
num_classes = 10

# 1. ucitaj spremljeni model iz zadatka 1
model = keras.models.load_model("mnist_model1.h5")

# 2. ucitaj MNIST podatke
(x_train, y_train), (x_test, y_test) = keras.datasets.mnist.load_data()

# 3. priprema testnih slika na isti nacin kao u zadatku 1
x_test_s = x_test.astype("float32") / 255.0
x_test_s = np.expand_dims(x_test_s, -1)   # oblik: (N, 28, 28, 1)

# 4. predikcija modela
y_pred = model.predict(x_test_s)
y_pred_classes = np.argmax(y_pred, axis=1)

# 5. pronadi pogresno klasificirane primjere
wrong_idx = np.where(y_pred_classes != y_test)[0]

print(f"Ukupno pogresno klasificiranih slika: {len(wrong_idx)}")

# 6. prikazi nekoliko pogresno klasificiranih slika
n = 10  # broj slika za prikaz
plt.figure(figsize=(15, 6))

for i in range(min(n, len(wrong_idx))):
    idx = wrong_idx[i]

    plt.subplot(2, 5, i + 1)
    plt.imshow(x_test[idx], cmap="gray")
    plt.title(f"Stvarna: {y_test[idx]}\nPredviđena: {y_pred_classes[idx]}")
    plt.axis("off")

plt.suptitle("Loše klasificirane slike iz testnog skupa")
plt.tight_layout()
plt.show()