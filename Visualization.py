import matplotlib.pyplot as plt
import imageio

pic = imageio.imread('/content/teddy image.jpg')
plt.figure(figsize= (10,10))
plt.imshow(pic)

print('Type of the image : ' , type(pic))
print('Shape of the image : {}'.format(pic.shape))
print('Image Hight {}'.format(pic.shape[0]))
print('Image Width {}'.format(pic.shape[1]))
print('Dimension of Image {}'.format(pic.ndim))  #RGB=3dim

# try to below this colour changes
plt.title('G channel')
plt.ylabel('Height {}'.format(pic.shape[0]))
plt.xlabel('Width {}'.format(pic.shape[1]))

plt.imshow(pic[ : , : , 1])
plt.show()

#generating negative pixel
negative = 255- pic # neg = (L-1) - img
#negative=255-negative (negative image convert to colour)
plt.figure(figsize= (6,6))
plt.imshow(negative)
plt.axis('off')

#gamma correctionfor brightness
import imageio
import matplotlib.pyplot as plt

# Gamma encoding
pic=imageio.imread('/content/teddy image.jpg')
gamma=0.1     # Gamma < 1 ~ Dark ; Gamma > 1 ~ Bright

gamma_correction=((pic/255)**(1/gamma))
plt.figure(figsize=(5,5))
plt.imshow(gamma_correction)
plt.axis('off')


