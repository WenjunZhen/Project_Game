import matplotlib.image as mpimg 
from matplotlib import pyplot as plt
import numpy as np

floor = mpimg.imread('floor.jpg', format = "jpg").copy()
Map = mpimg.imread('blank.jpg', format = "jpg").copy()
fig, ax = plt.subplots(1)

len_floor, wid_floor = floor.shape
for i in range(14):
    for j in range(14):
        Map[i*len_floor:(i+1)*len_floor,j*wid_floor:(j+1)*wid_floor] = floor
plt.imshow(Map)
