#!/usr/bin/env python
# −*− coding: UTF−8 −*−
#
# Author:   Jove Yu <yushijun110@gmail.com>
#
import os, Image, urllib

dir="./tmp/"

def init():
    """初始化"""
    for f in os.listdir(dir):
        os.remove(dir+f)

def downcode(url):
    """下载图片"""
    file(dir+'tmp.jpg',"wb").write(urllib.urlopen(url).read())
    Image.open(dir+'tmp.jpg').convert('RGB').save(dir+'tmp.jpg')

def movecode(f):
    """本地打开图片并移动到指定目录"""
    img=Image.open(f)
    img.save(dir+'tmp.jpg')

def grey():
    """灰度化"""
    img=Image.open(dir+'tmp.jpg')
    img.convert('L').save(dir+'1.jpg')

def binary():
    """二值化"""
    img = Image.open(dir+'tmp.jpg')
    #img = img.convert('1')
    pixdata = img.load()
    for y in range(img.size[1]):
        for x in range(img.size[0]):
            if pixdata[x, y][0] < 90:
                pixdata[x, y] = (0, 0, 0, 255)
    for y in range(img.size[1]):
        for x in range(img.size[0]):
            if pixdata[x, y][1] < 136:
                pixdata[x, y] = (0, 0, 0, 255)
    for y in range(img.size[1]):
        for x in range(img.size[0]):
            if pixdata[x, y][2] > 0:
                pixdata[x, y] = (255, 255, 255, 255)
    img.save(dir+'2.jpg')

def denoisepoint(n):
    """去噪点"""
    direct=[[1,1],[1,0],[1,-1],[0,-1],
            [-1,-1],[-1,0],[-1,1],[0,1]]
    num=0 #操作数量
    point=0 #噪点量
    img=Image.open(dir+'2.jpg')
    pix=img.load()
    size=img.size
    for y in range(size[1]):
        for x in range(size[0]):
            num+=1
            if pix[x,y][0]<n:
                nearpoint=0
                for (a,b) in direct:
                    if (x+a>=0 and x+a<=size[0]-1)and(y+b>=0 and y+b<=size[1]-1):
                    #如果遇到边界外的点不处理
                        if pix[x+a,y+b][0]<n:
                            nearpoint+=1
                if nearpoint==0:
                    pix[x,y]=(255, 255, 255, 255)
                    point+=1
    img.save(dir+'3.jpg')
    return (num,point)

def devide(n):
    """分割图像"""
    #n 分割的阀值
    img=Image.open(dir+'3.jpg')
    flagx=[0 for x in range(img.size[0])]
    result=[]
    pix=img.load()
    #横坐标上的像素分布
    for x in range(img.size[0]):
        for y in range(img.size[1]):
            if pix[x,y][0]<90:
                flagx[x]+=1
    print flagx
    for i in range(img.size[0]):
        if flagx[i]>n and flagx[i-1]<=n:
            tmp=i
        if flagx[i-1]>n and flagx[i]<=n:
            #纵坐标上的分布
            flagy=[0 for x in range(img.size[1])]
            for y in range(img.size[1]):
                for x in range(i+1)[tmp:]:
                    if pix[x,y][0]<90:
                        flagy[y]+=1
            print flagy
            ttmp=0
            #有待改善
            bug=1
            for j in range(img.size[1]):
                if flagy[j]>n and flagy[j-1]<=n:
                    ttmp=j
                if flagy[j-1]>n and flagy[j]<=n:
                    result.append([tmp,i,ttmp,j])
                    bug=0
            if bug==1:
                result.append([tmp,i,ttmp,img.size[1]])
    #print result
    i=1
    for [x1,x2,y1,y2] in result:
        img.crop((x1,y1,x2,y2)).save(dir+'char%d.jpg'%i)
        i+=1
    return i-1

def enlargechar():
    """放大字符"""
    for i in range(6)[1:]:
        if i!=5 or os.path.exists(dir+'char5.jpg'):
            img=Image.open(dir+'char%d.jpg'%i)
            img.resize((60,60),Image.NEAREST).save(dir+'char%d-big.jpg'%i)

def recognize(n):
    """识别单个字符"""
    fontMods=[]
    fontdir="./font/"
    for file in os.listdir(fontdir):
        if file.endswith('.jpg'):
            fontMods.append((file[:1],Image.open(fontdir+file)))
    target=Image.open(dir+'char%d-big.jpg'%n)
    points = []
    for mod in fontMods:
        diffs = 0
        for yi in range(60):
            for xi in range(60):
                if mod[1].getpixel((xi, yi)) != target.getpixel((xi, yi)):
                    diffs += 1
        points.append((diffs, mod[0]))
    points.sort()
    return points[0][1]

def fontsave(n,str):
    """字符存入字库"""
    fontdir='./font/'
    img=Image.open(dir+'char%d-big.jpg'%n)
    i=1
    while(os.path.exists(fontdir+str+'-%d.jpg'%i)):
        i+=1
    img.save(fontdir+str+'-%d.jpg'%i)


def enlargeimage(f):
    """放大图片显示"""
    img=Image.open(dir+f)
    big=img.resize((400,175),Image.NEAREST)
    big.save(dir+'big.jpg')


def test():
    img=Image.open(dir+'3.jpg')
    pix=img.load()
    for y in range(img.size[1]):
        for x in range(img.size[0]):
            if pix[x,y]>(90,90,90):
                pix[x,y]=(255,255,255,255)
            else:
                pix[x,y]=(0,0,0,0)
    img.show()
    img.save(dir+'test.jpg')



if __name__ == '__main__':
    fontsave(1,'1')
