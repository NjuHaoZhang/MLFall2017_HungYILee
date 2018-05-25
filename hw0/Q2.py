# coding=gbk

from PIL import Image

# ��ȡͼƬ����rgb

im = Image.open("westbrook.jpg")
pix = im.load() # ���ؾ���{ÿ�����pixel��ɵľ���}
width = im.size[0]
height = im.size[1]
im2 = Image.new("RGB", (width, height))  # ������ͼƬ

for x in range(width):
    for y in range(height):
        r, g, b = pix[x, y] # ÿ����(x,y)��pixel��Ӧ��һ����Ԫ��(r,g,b)
        # print(r, g, b)
        r,g,b = int(r//2), int(g//2), int(b//2)
        im2.putpixel((x, y), (r, g, b))  # ��rgbת��Ϊ����

# im2.show()   #Ҳ����im.save('flag.jpg')��������
im2.save('Q2.jpg')
