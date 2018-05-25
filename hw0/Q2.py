# coding=gbk

from PIL import Image

# 读取图片处理rgb

im = Image.open("westbrook.jpg")
pix = im.load() # 像素矩阵{每个点的pixel组成的矩阵}
width = im.size[0]
height = im.size[1]
im2 = Image.new("RGB", (width, height))  # 创建新图片

for x in range(width):
    for y in range(height):
        r, g, b = pix[x, y] # 每个点(x,y)的pixel对应着一个三元组(r,g,b)
        # print(r, g, b)
        r,g,b = int(r//2), int(g//2), int(b//2)
        im2.putpixel((x, y), (r, g, b))  # 将rgb转化为像素

# im2.show()   #也可用im.save('flag.jpg')保存下来
im2.save('Q2.jpg')
