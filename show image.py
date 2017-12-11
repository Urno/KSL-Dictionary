#이미지 등록
import matplotlib.pyplot as plt
from matplotlib.image import imread

img = imread('C:\project2/20171205_183049_283.jpg') # 이미지 읽어오기
plt.imshow(img)
plt.show()
