from PIL import Image
import torch
import numpy
img =  Image.open('image.jpg.jpg')

matrix = numpy.array(img)
x = torch.tensor(matrix)

print(x)