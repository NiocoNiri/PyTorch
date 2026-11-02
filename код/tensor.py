from unittest import result

import numpy as np
import torch
from pathlib import Path
from PIL import Image
import torchvision.transforms.functional as F
import torchvision.transforms as T


def open_image():
    while True:
        path = input("введите путь до файла ")
        try:
            img = Image.open(path)
            break
        except FileNotFoundError:
            print("пожалуйста введите коректный путь")

    tensor = torch.from_numpy(np.array(img)).float()
    return tensor


def cb_image(tensor):
    gray = 0.299 * tensor[:, :, 0] + 0.587 * tensor[:, :, 1] + 0.114 * tensor[:, :, 2]
    result = Image.fromarray(gray.clamp(0, 255).round().to(torch.uint8).numpy())
    result.show()
    gray_rgb = gray.unsqueeze(-1).repeat(1, 1, 3)
    return gray_rgb


def cont_image(tensor):
    while True:
        try:
            contr = float(input("введите силу контраста "))
            break
        except ValueError:
            print("введите число ")
    tensor = tensor.permute(2, 0, 1) / 255
    cont = F.adjust_contrast(tensor, contr)
    cont = cont.permute(1, 2, 0) * 255
    result = Image.fromarray(cont.clamp(0, 255).round().to(torch.uint8).numpy())
    result.show()
    return cont


def invert_image(tensor):
    inverted_tensor = 255 - tensor
    result = Image.fromarray(
        inverted_tensor.clamp(0, 255).round().to(torch.uint8).numpy()
    )
    result.show()
    return inverted_tensor


def save_image(tensor):
    a = input("имя изображения ")
    img = Image.fromarray(tensor.clamp(0, 255).round().to(torch.uint8).numpy())
    img.save(Path(__file__).parent / a, "PNG")


def main():
    tensor = None
    while True:
        print(
            "Редактор изображений",
            "\n",
            "1 - добавить изображение",
            "\n",
            "2 - первести в чб",
            "\n",
            "3 - увеличить контраст",
            "\n",
            "4 - инвентировать",
            "\n",
            "5 - сохранить изображение",
            "\n",
            "6 - выход",
        )
        a = int(input("Выберете функцию "))
        if a == 1:
            tensor = open_image()
            print("изображение добавлено")
        elif a == 2 and tensor is not None:
            tensor = cb_image(tensor)
        elif a == 3 and tensor is not None:
            tensor = cont_image(tensor)
        elif a == 4 and tensor is not None:
            tensor = invert_image(tensor)
        elif a == 5 and tensor is not None:
            save_image(tensor)
        elif a == 6:
            print("спасибо")
            break
        else:
            print("сначала загрузите изображение")


main()

# learning/pytorch/код/images.jpg
# /home/nioconiri/Projects/learning/pytorch/код/images.jpg
