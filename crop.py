from PIL import Image
import time
import os
import sys

fnd = False

while not fnd:
    img_path = input("enter image name/path :- ")
    try:
        img = Image.open(img_path)
        fnd = True
    except Exception as e:
        print("image not found")

width, height = img.size

w_len = int(input("enter the width of cropped images :- "))
h_len = int(input("enter the height of cropped images :- "))

folder = False

while not folder:
    title = input("enter the base name :- ")
    try:
        os.mkdir(title)
        folder = True
    except FileExistsError:
        print("Error 001 enter new file name :- ")

n = 0

os.system('cls')

for i in range(0, width, w_len):
    for j in range(0, height, h_len):
        n+=1
        crp_img = img.crop((i, j, i+w_len, j+h_len))
        path = title + "/" + title + "_" + str(n) +".png"
        crp_img.save(path)
        if n%4 == 0:
            sys.stdout.write('\rloading |')
        if n%4 == 1:
            sys.stdout.write('\rloading /')
        if n%4 == 2:
            sys.stdout.write('\rloading -')
        if n%4 == 3:
            sys.stdout.write('\rloading \\')
        time.sleep(0.1)

sys.stdout.write('\r!! Done !!')
time.sleep(5)
