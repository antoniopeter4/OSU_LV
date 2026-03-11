import numpy as np
import matplotlib.pyplot as plt

img=plt.imread("road.jpg")
plt.subplot(2,3,1)
plt.imshow(img)
plt.title("Original")


img_brightness=img+ 55
img_light=np.clip(img_brightness, 0, 255)
plt.subplot(2,3,2)
plt.imshow(img_brightness)
plt.axis("off")
plt.title("Brightness")


h, w, _ = img.shape
druga_cetvrtina = img[:, w//4:w//2]
plt.subplot(2,3,3)
plt.imshow(druga_cetvrtina)
plt.axis("off")
plt.title("Second quater")



rotirana = np.rot90(img, -1) 
plt.subplot(2,3,4) 
plt.imshow(rotirana)
plt.axis("off")
plt.title("Rotated")



zrcaljena = np.fliplr(img)
plt.subplot(2,3,5)
plt.imshow(zrcaljena)
plt.axis("off")
plt.title("Mirrored")

plt.show()

