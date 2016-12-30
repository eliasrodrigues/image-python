import skimage.io as io
from skimage.color import rgb2gray 

#Open the Original Image
img = io.imread('assassins-creed-original.jpg')

#Apply the Grayscale Filter to the Image
img_grayscale = rgb2gray(img)

#Save the new Grayscale Image
io.imsave('assassins-creed-grayscale.jpg',img_grayscale)