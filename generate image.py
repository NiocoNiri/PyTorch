import numpy as np
from PIL import Image

# Создадим пример матрицы (серое изображение 100x100 от 0 до 255)
matrix = np.zeros((8, 8), dtype=np.uint8)


# Преобразуем матрицу в изображение
img = Image.fromarray(matrix)
matrix[2:] = 255
print(matrix)

# Или покажем на экране
img.show()
