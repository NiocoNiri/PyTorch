from PIL import Image
import torch
import numpy as np
img =  Image.open('image 2.png')

matrix = np.array(img)   
matrix[0,0] = 0
matrix[0,1] = 0
matrix[0,2] = 0
x = torch.tensor(matrix)
x = x.permute(1, 0, 2)
matrix = np.array(x)
print(x)
zxc = Image.fromarray(matrix)
zxc.show()