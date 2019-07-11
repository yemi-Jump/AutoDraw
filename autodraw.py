import turtle
import cv2
import numpy as np
from matplotlib import pyplot as plt
import matplotlib.cm as cm
import json
import pandas as pd
from math import sqrt
from collections import Iterable


img = cv2.imread('images/starry.jpg', 0) # 0 puts it into grayscale
print(img.shape)

scale_percent = 75 # 75% of original size
width = int(img.shape[1] * scale_percent / 100)
height = int(img.shape[0] * scale_percent / 100)
dim = (width, height)

resized = cv2.resize(img, dim)
print("Resized: ", resized.shape)

cv2.imshow('image', resized) # window name 'image'

edges = cv2.Canny(resized,100,200, L2gradient=True) # L2g makes more accurate
cv2.imwrite("images/edge.png", edges)

plt.subplot(121),plt.imshow(resized, cmap='gray')
plt.title('Original Image'), plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(edges,cmap='gray')
plt.title('Edge Image'), plt.xticks([]), plt.yticks([])

plt.show()
cv2.waitKey(0) # maintain output window untill user presses a key


cnt, hierarchy = cv2.findContours(edges, cv2.RETR_LIST,cv2.CHAIN_APPROX_SIMPLE)

cnt_array = np.array(cnt)
contour = cnt_array.tolist()

# makes list un-nested or 1-dimensional
def flatten(contour):
    for item in contour:
        if isinstance(item, Iterable) and not isinstance(item, str):
            for x in flatten(item):
                yield x
        else:
            yield item

# used to flip y axis
def reflect(lst):
    res = list(lst) # Copy the list
    # Iterate through the indexes instead of the elements
    for i in range(len(res)):
        if i % 2 != 0:
            res[i] = res[i]*-1
    return res


flat_cnt = (list(flatten(contour)))
new_list = reflect(flat_cnt) # flip on the y axis
flat_new = (list(flatten(new_list)))
print(flat_new)

tuple_new = list(zip(flat_new[::2], flat_new[1::2]))
print(tuple_new)


with open("output.txt", "w") as f:
    f.write(str(tuple_new))
