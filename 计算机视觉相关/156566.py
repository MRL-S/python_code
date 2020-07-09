# from PIL import Image
# import matplotlib.pyplot as plt
# import numpy as np
# import tensorflow as tf
# # img = Image.open("lena.tiff")
# # img_r,img_g,img_b = img.split()
# # plt.figure(figsize=(10,10))

# # plt.subplot(221)
# # plt.axis("off")
# # plt.imshow(img_r,cmap="gray")
# # plt.title("R",fontsize=20)

# # plt.subplot(222)
# # plt.axis("off")
# # plt.imshow(img_g,cmap="gray")
# # plt.title("G",fontsize=20)

# # plt.subplot(223)
# # plt.axis("off")
# # plt.imshow(img_b,cmap="gray")
# # plt.title("B",fontsize=20)

# # img_rgb = Image.merge("RGB",[img_r,img_g,img_b])
# # plt.subplot(224)
# # plt.axis("off")
# # plt.imshow(img_rgb)
# # plt.title("RGB",fontsize=20)
# # plt.show()
# # img_gray = img.convert("L")
# # arr_img_gray = np.array(img_gray)
# # arr_img_new = 255-arr_img_gray

# # plt.figure(figsize=(10,5))

# # plt.subplot(121)
# # plt.axis("off")
# # plt.imshow(arr_img_gray,cmap="gray")

# # plt.subplot(122)
# # plt.axis("off")
# # plt.imshow(arr_img_new,cmap="gray")
# # plt.show()
# # plt.figure(figsize=(10,5))
# # plt.subplot(121)
# # plt.imshow(img)

# # plt.subplot(122)
# # plt.imshow(img.crop((100,100,400,400)))
# # plt.show()
# mnist = tf.keras.datasets.mnist
# (train_x,train_y),(test_x,test_y) = mnist.load_data()
# plt.axis("off")
# plt.imshow(train_x[0],cmap="gray")
# plt.show()
import tensorflow as tf

t1 = tf.constant([[1, 2, 3], [4, 5, 6]])

t2 = tf.constant([[7, 8, 9], [10, 11, 12]])

t = tf.stack((t1, t2), axis=-1)

print(t.shape)