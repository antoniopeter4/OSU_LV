import numpy as np
import keras
from matplotlib import pyplot as plt
from PIL import Image

# učitaj model
model = keras.models.load_model("mnist_model1.h5")

# učitaj sliku
img = Image.open("LV8/test_4.png").convert("L")  # grayscale

# promijeni veličinu na 28x28
img = img.resize((28, 28))

# pretvori u numpy array
img_array = np.array(img)

# invertiranje (ako je pozadina bijela, a broj crn)
img_array = 255 - img_array

# skaliranje [0,1]
img_array = img_array.astype("float32") / 255

# dodaj dimenzije (1, 28, 28, 1)
img_array = np.expand_dims(img_array, axis=0)
img_array = np.expand_dims(img_array, axis=-1)

# predikcija
prediction = model.predict(img_array)
predicted_class = np.argmax(prediction)

print("Predviđena znamenka:", predicted_class)

# prikaži sliku
plt.imshow(img_array[0].reshape(28,28), cmap="gray")
plt.title(f"Predikcija: {predicted_class}")
plt.show()
