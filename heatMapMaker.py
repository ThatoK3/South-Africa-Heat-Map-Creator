
from math import ceil
import time
import numpy as np
from pil import Image, ImageEnhance
import plotly.graph_objects as go
import cv2


start_time = time.time()

img_frame   = Image.open('Map-Frame.png')
img_EC      = Image.open('EC.png')
img_FS      = Image.open('FS.png')
img_GP      = Image.open('GP.png')
img_KZN     = Image.open('KZN.png')
img_LMP     = Image.open('LMP.png')
img_MP      = Image.open('MP.png')
img_NC      = Image.open('NC.png')
img_NW      = Image.open('NW.png')
img_WC      = Image.open('WC.png')
img_LESOTHO = Image.open('LESOTHO.png')


def imageresize(image,basewidth):
    img = image
    wpercent = (basewidth / float(img.size[0]))
    hsize = int((float(img.size[1]) * float(wpercent)))
    Rzimg = img.resize((basewidth, hsize), Image.ANTIALIAS)
    return Rzimg

def colorchange(image, x, frac):
    c = image
    w, h = c.size
    cnt = 0
    # White
    if x==-1:
        for px in c.getdata():
            c.putpixel((int(cnt % w), int(cnt / w)), (255, 255, 255, px[3]))
            cnt += 1  
    # Black
    elif x == -2:
            for px in c.getdata():
                c.putpixel((int(cnt % w), int(cnt / w)), (0, 0, 0, px[3]))
                cnt += 1 
    # Iteration
    elif x>0:
        if x<37:
            for px in c.getdata():
                c.putpixel((int(cnt % w), int(cnt / w)), ((ceil((x+204)*1.055*(1-frac))), (ceil((x)*0.997*(1-frac))), (ceil((x)*0.150*(1-frac))), px[3]))
                cnt += 1
        #Error
        elif x>36:
            print('x value out of range')
            
    # Error
    else:
        print('x value must be an integer less than 37')
               
    return c


# Resize loaded images
width = 6000
img_frame   = imageresize(img_frame   ,width)
img_EC      = imageresize(img_EC      ,width)
img_FS      = imageresize(img_FS      ,width)
img_GP      = imageresize(img_GP      ,width)
img_KZN     = imageresize(img_KZN     ,width)
img_LMP     = imageresize(img_LMP     ,width)
img_MP      = imageresize(img_MP      ,width)
img_NC      = imageresize(img_NC      ,width)
img_NW      = imageresize(img_NW      ,width)
img_WC      = imageresize(img_WC      ,width)
img_LESOTHO = imageresize(img_LESOTHO ,width)

n1  = 0.84
n2  = 0.756
n3  = 0.672
n4  = 0.588
n5  = 0.504
n6  = 0.420
n7  = 0.336
n8  = 0.252
n9  = 0.168
n10 = 0.084
xn  = 36

img_frame   = colorchange(img_frame,   -2  ,  n1)
img_EC      = colorchange(img_EC,      xn,   n1)
img_FS      = colorchange(img_FS,      xn,   n2)
img_GP      = colorchange(img_GP,      xn,   n3)
img_KZN     = colorchange(img_KZN,     xn,   n4)
img_LMP     = colorchange(img_LMP,     xn,   n5)
img_MP      = colorchange(img_MP,      xn,   n6)
img_NC      = colorchange(img_NC,      xn,   n7) 
img_NW      = colorchange(img_NW,      xn,   n8)
img_WC      = colorchange(img_WC,      xn,   n9)
img_LESOTHO = colorchange(img_LESOTHO, -1,   n10)

images = img_frame , img_FS , img_GP , img_KZN , img_LMP , img_MP , img_NC , img_NW , img_WC , img_LESOTHO , img_EC


    

        
    

fin_image  = []

for i in range(1,11):
    img_frame = Image.composite(img_frame, images[i], img_frame)
    fin_image.append(img_frame)

fin_image[9].save('Map.png')

    


print ("My program took", time.time() - start_time, "to run")

