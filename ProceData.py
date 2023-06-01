from PIL import Image
img1=Image.open('D:/img1.jpg')
d=img1.size
print("照片的宽度为{}".format(d[0]))
print("照片的高度为{}".format(d[1]))
for y in range(d[0]):
    for x in range(d[1]):
        RGB=img1.getpixel((y,x))
        