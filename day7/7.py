
# Pillow    操作图像

#安装： pip install pillow

from PIL import Image , ImageFilter

path = "C:\\Users\\Administrator\\Desktop\\"

im = Image.open(path+"vcode.jpg")

w,h = im.size

print(w,h)

# # 缩放到50%:
im.thumbnail((w//2, h//2))
w,h = im.size

print(w,h)

# 把缩放后的图像用jpeg格式保存:
# im.save(path+"vcode2.jpeg","jpeg")

# 其他功能如切片、旋转、滤镜、输出文字、调色板等一应俱全。


# 应用模糊滤镜:
im2 = im.filter(ImageFilter.BLUR)
# im2.save(path+'blur.jpg', 'jpeg')

# PIL的ImageDraw提供了一系列绘图方法，让我们可以直接绘图。比如要生成字母验证码图片：

from PIL import   ImageDraw, ImageFont
import random

def rndChar():
    return chr( random.randint(65,90) )

def rndColor():
    return ( random.randint(64,255) , random.randint(64,255), random.randint(64,255) )

def rndColor2():
    return ( random.randint(32,127),random.randint(32,127),random.randint(32,127) )

width = 60*4
heigth = 60
image = Image.new('RGB',(width,heigth), (255,255,255) )

font = ImageFont.truetype('C:\\Windows\\Fonts\\STXIHEI.TTF',36)

draw = ImageDraw.Draw(image)

for x in range(width):
    for y in range(heigth):
        draw.point( (x,y),fill=rndColor() )


for i in  range(4):
    draw.text( (60*i + 10,10), rndChar(),font=font ,fill=rndColor2() )

image = image.filter(ImageFilter.BLUR)

image.save(path+"code.jpg")