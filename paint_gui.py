from tkinter import *
from colorthief import ColorThief
from PIL import ImageTk,ImageDraw,ImageFilter,ImageFont ,ImageEnhance
from tkinter import colorchooser
from PIL import Image
from tkinter import filedialog
from tkinter import messagebox
import pyglet
import PIL
pyglet.font.add_file('fonts/SourceCodePro-Regular.ttf')
pyglet.font.add_file('fonts/Sacramento-Regular.ttf')
pyglet.font.add_file('fonts/Roboto-Regular.ttf')
pyglet.font.add_file('fonts/Lobster-Regular.ttf')
pyglet.font.add_file('fonts/Rowdies-Regular.ttf')
pyglet.font.add_file('fonts/Cookie-Regular.ttf')
pyglet.font.add_file('fonts/ShadowsIntoLight-Regular.ttf')
color="black"
#start
root=Tk()
def _from_rgb(rgb):
    return "#%02x%02x%02x" % rgb
root.title(" Proton ")
root.iconbitmap("image_editor.ico")
root.configure(bg="lightblue")
imagename='imagegame1.png'
imgname=filedialog.askopenfilename(initialdir="/Desktop/python codes",title="open images",filetypes=(("png files","*.png"),("jpg files","*.jpg"),))
imagename=imgname
glb_img_name=imagename
color_thief = ColorThief(glb_img_name)
dominant_color = color_thief.get_color(quality=1)
original_name_of_the_image=glb_img_name
copy=Image.open(imagename)
owidth,oheight=copy.size
toolbo=[]
for i in range(10):
    toolbo.append(0)
frameactive=1
#this is to compress image to dispaly
def width_height(owidth,oheight):
    while((oheight>680 )):
        owidth,oheight=int(owidth/1.1),int(oheight/1.1)
    while((owidth>930 )):
        owidth,oheight=int(owidth/1.1),int(oheight/1.1)
    return owidth,oheight
width,height=width_height(owidth,oheight)
def chose():
    global color
    global mybutton
    global toolbo
    global frameactive
    mycolor=colorchooser.askcolor()[1]
    if(mycolor):
        color= mycolor
    mybutton=Button(toolbo[frameactive],text="   ",command=chose,fg=color,bg=color).grid(row=1,column=1)
def eraser():
    global color
    global what
    global erase
    global toolbo
    global frameactive
    global pai
    what="erase"
    erase=Button(toolbo[frameactive],text="Erase",command=eraser,bg="black",fg="white").grid(row=1,column=2)
    pai=Button(toolbo[frameactive],text="paint",command=pain,bg="white",fg="black").grid(row=1,column=4)
def eraser2():
    global color
    global what
    global erase
    global toolbo
    global frameactive
    global pai
    global brux,bruy
    what="erase" 
def pain():
    global what
    global erase
    global toolbo
    global image1
    global frameactive
    global pai
    what="paint"
    erase=Button(toolbo[frameactive],text="Erase",command=eraser,bg="white",fg="black").grid(row=1,column=2)
    pai=Button(toolbo[frameactive],text="paint",command=pain,bg="black",fg="white").grid(row=1,column=4)
what="nothing"
def save1():
    global imagename
    global glb_img_name
    global toolbo
    global b1,b2,b3,b4,b5,b6,b7,b8,b9,b10,b11,b12,b13,b14
    global but1,but2,but3,but4,but5,but6,but7,but8,but9,but10,but11,but12,but13
    global button,button1,button2,button3,button4,button5,button6,button7,button8,button9,button10,button11,button12
    filename="processed/edited2.png"
    image1.save(filename,quality=200)
    glb_img_name="processed/edited2.png"
    save_fun()
count=0
images=[]
cs=[]
save_panniya_cha=0
brux,bruy=0,0
firstah=0
xx1,yy1=53,78
def brushsize(value):
    global brux,bruy
    brux,bruy=int(value),int(value)
def paint(event):
    global color
    global what
    global c1
    global x1,x2,y1,y2
    global count
    global img2
    global currentimg
    global firstah
    global myimg
    global brux,bruy
    global brux1,bruy1
    global width,height
    global image2
    global images
    global draw
    global imagename
    global imgpresent
    global glb_img_name
    global c
    global img3
    global currentla_enna_font
    global xx,yy
    global xx1,yy1
    global textsize
    global Image1
    global fcolor
    global word
    global texton
    if(what=="paint"):
        imgpresent=0
        x1,y1=(event.x)-1-int(brux/2),(event.y)-1-int(bruy/2)
        x2,y2=(event.x)+brux-int(brux/2),(event.y)+bruy-int(bruy/2)
        c1=c.create_rectangle(x1,y1,x2,y2,fill=color,outline=color,width=5)
        draw.rectangle([x1-2,y1-2,x2+2.5,y2+2.5],fill=color,width=5)
    elif(what=="erase"):
        imgpresent=0
        filename="processed/edited_using.png"
        image1.save(filename,quality=200)
        x1,y1=(event.x)-1-int(brux/2),(event.y)-1-int(bruy/2)
        x2,y2=(event.x)+brux-int(brux/2),(event.y)+bruy-int(bruy/2)
        image2 = Image.open(glb_img_name).resize((width,height),Image.ANTIALIAS)
        image2copy=image2.copy()
        crop_rectangle = (x1, y1,x2+brux , y2+bruy)
        cropped_im = image2.crop(crop_rectangle)
        image1.paste(cropped_im, (x1, y1))
        myimg=ImageTk.PhotoImage(Image.open("processed/edited_using.png").resize((width,height),Image.ANTIALIAS))
        c.create_image(0,0,anchor=NW,image=myimg)
        c.grid(row=0,column=0)
        draw=ImageDraw.Draw(image1)
        firstah+=1
    elif(what=="crop"):
        imgpresent=0
        x1,y1=(event.x)-1-int(brux1/2),(event.y)-1-int(bruy1/2)
        x2,y2=(event.x)+brux1-int(brux1/2),(event.y)+bruy1-int(bruy1/2)
        c.create_image(0,0,anchor=NW,image=myimg)
        c1=c.create_rectangle(x1,y1,x2,y2,fill=None,outline="black",width=5)
    elif(what=="imageon"):
        if(imgpresent):
            img = Image.open(glb_img_name)
            myimg=ImageTk.PhotoImage(img.resize((width,height),Image.ANTIALIAS))
            c.create_image(0,0,anchor=NW,image=myimg)
            xx1,yy1=event.x,event.y
            img3=c.create_image(xx1,yy1,image=img2)
            c.grid(row=0,column=0)
    if(what=="texton"):
        if(texton):
            img = Image.open(glb_img_name)
            myimg=ImageTk.PhotoImage(img.resize((width,height),Image.ANTIALIAS))
            c.create_image(0,0,anchor=NW,image=myimg)
            xx,yy=event.x,event.y
            img3=c.create_text(xx,yy,text=word,fill=fcolor,font=(currentla_enna_font,textsize))
            c.grid(row=0,column=0)
myimg=ImageTk.PhotoImage(Image.open(glb_img_name).resize((width,height),Image.ANTIALIAS))
c=Canvas(root,width=width,height=height,bg="lightgreen")
c.grid(row=0,column=0)
c.create_image(0,0,anchor=NW,image=myimg)
image1=PIL.Image.open(glb_img_name).resize((width,height),Image.ANTIALIAS)
image2=ImageTk.PhotoImage(Image.open(glb_img_name))
draw=ImageDraw.Draw(image1)
c.grid(row=0,column=0)
c.bind('<B1-Motion>',paint)
toolbo[frameactive]=Frame(root,relief=RIDGE,bd=3)
sav=Button(toolbo[frameactive],text="Save",command=save1)
sav.grid(row=1,column=0,padx=5)
mybutton=Button(toolbo[frameactive],text="   ",bg="black",fg="black",command=chose).grid(row=1,column=1,padx=10,pady=10)
erase=Button(toolbo[frameactive],text="Erase",command=eraser).grid(row=1,column=2,padx=5,pady=10)
pai=Button(toolbo[frameactive],text="Paint",command=pain).grid(row=1,column=4,padx=5,pady=10)
reset=Button(toolbo[frameactive],text="Reset").grid(row=1,column=5,padx=5,pady=10)
sca=Scale(toolbo[frameactive],from_=0,to=100,orient=HORIZONTAL,command=brushsize,length=200)
sca.grid(row=2,column=0,columnspan=6)
toolbo[frameactive].grid(row=0,column=1,pady=10,padx=10)
#filters
img = Image.open(glb_img_name).resize((width,height),Image.ANTIALIAS).convert("RGB")
pixels =img.load()
def grey(height,width,img):
    pixels =img.load()
    for py in range(height):
        for px in range(width):
            r,g,b = img.getpixel((px,py))
            pixels[px,py] = (b,b,b)
    return img
def red(height,width,img):
    pixels =img.load()
    for py in range(height):
        for px in range(width):
            r,g,b = img.getpixel((px,py))
            pixels[px,py] = (r,0,0)
    return img
def blue(height,width,img):
    pixels =img.load()
    for py in range(height):
        for px in range(width):
            r,g,b = img.getpixel((px,py))
            pixels[px,py] = (g,r,b)
    return img
def green(height,width,img):
    pixels =img.load()
    for py in range(height):
        for px in range(width):
            r,g,b = img.getpixel((px,py))
            pixels[px,py] = (r,b,r)
    return img
def cus1(height,width,img):
    pixels =img.load()
    for py in range(height):
        for px in range(width):
            r,g,b = img.getpixel((px,py))
            pixels[px,py] = (b,g,r)
    return img
def cus2(height,width,img):
    pixels =img.load()
    for py in range(height):
        for px in range(width):
            r,g,b = img.getpixel((px,py))
            pixels[px,py] = (b,b,r)
    return img
def cus3(height,width,img):
    pixels =img.load()
    for py in range(height):
        for px in range(width):
            r,g,b = img.getpixel((px,py))
            pixels[px,py] = (g,g,b)
    return img
def cus4(height,width,img):
    pixels =img.load()
    for py in range(height):
        for px in range(width):
            r,g,b = img.getpixel((px,py))
            pixels[px,py] = (r,b,g)
    return img
def cus5(img):
    img = img.filter(ImageFilter.BLUR)
    return img
def cus6(img):
    img = img.filter(ImageFilter.CONTOUR)
    return img
def cus7(img):
    img = img.filter(ImageFilter.EMBOSS)
    return img
def cus8(img):
    img = img.filter(ImageFilter.EDGE_ENHANCE)
    return img
def cus9(height,width,img):
    pixels =img.load()
    def cepia(r,g,b):
        newr=int((r*.393)+(g*.769)+(b*.189))
        newg=int((r*.349)+(g*.686)+(b*.168))
        newb=int((r*.272)+(g*.534)+(b*.131))
        return newr,newg,newb
    for py in range(height):
        for px in range(width):
            r,g,b = img.getpixel((px,py))
            r,g,b=cepia(r,g,b)
            pixels[px,py] = (r,b,g)
    return img
def f1():
    global c
    global myimg
    global mimg
    global imagename
    global glb_img_name
    global image1
    global width,height
    b1=Image.open(glb_img_name).resize((width,height),Image.ANTIALIAS).convert("RGB")
    width,height =b1.size
    mimg=grey(height,width,b1)
    but1=ImageTk.PhotoImage(mimg)
    myimg=but1
    image1=b1
    c.create_image(0,0,anchor=NW,image=myimg)
    c.grid(row=0,column=0)
def f2():
    global c
    global myimg
    global mimg
    global imagename
    global glb_img_name
    global image1
    global width,height
    b1=Image.open(glb_img_name).resize((width,height),Image.ANTIALIAS).convert("RGB")
    width,height =b1.size
    mimg=red(height,width,b1)
    but1=ImageTk.PhotoImage(mimg)
    myimg=but1
    image1=b1
    c.create_image(0,0,anchor=NW,image=myimg)
    c.grid(row=0,column=0)
def f3():
    global c
    global myimg
    global mimg
    global imagename
    global glb_img_name
    global image1
    global width,height
    b1=Image.open(glb_img_name).resize((width,height),Image.ANTIALIAS).convert("RGB")
    width,height =b1.size
    mimg=blue(height,width,b1)
    but1=ImageTk.PhotoImage(mimg)
    myimg=but1
    image1=b1
    c.create_image(0,0,anchor=NW,image=myimg)
    c.grid(row=0,column=0)
def f4():
    global c
    global myimg
    global mimg
    global imagename
    global glb_img_name
    global image1
    global width,height
    b1=Image.open(glb_img_name).resize((width,height),Image.ANTIALIAS).convert("RGB")
    width,height =b1.size
    mimg=green(height,width,b1)
    but1=ImageTk.PhotoImage(mimg)
    myimg=but1
    image1=b1
    c.create_image(0,0,anchor=NW,image=myimg)
    c.grid(row=0,column=0)
def f5():
    global c
    global myimg
    global mimg
    global imagename
    global glb_img_name
    global image1
    global width,height
    b1=Image.open(glb_img_name).resize((width,height),Image.ANTIALIAS).convert("RGB")
    width,height =b1.size
    mimg=cus1(height,width,b1)
    but1=ImageTk.PhotoImage(mimg)
    myimg=but1
    image1=b1
    c.create_image(0,0,anchor=NW,image=myimg)
    c.grid(row=0,column=0)
def f6():
    global c
    global myimg
    global mimg
    global imagename
    global glb_img_name
    global width,height
    b1=Image.open(glb_img_name).resize((width,height),Image.ANTIALIAS).convert("RGB")
    width,height =b1.size
    mimg=cus2(height,width,b1)
    but1=ImageTk.PhotoImage(mimg)
    myimg=but1
    image1=b1
    c.create_image(0,0,anchor=NW,image=myimg)
    c.grid(row=0,column=0)
def f7():
    global c
    global myimg
    global mimg
    global imagename
    global glb_img_name
    global image1
    global width,height
    b1=Image.open(glb_img_name).resize((width,height),Image.ANTIALIAS).convert("RGB")
    width,height =b1.size
    mimg=cus3(height,width,b1)
    but1=ImageTk.PhotoImage(mimg)
    myimg=but1
    image1=b1
    c.create_image(0,0,anchor=NW,image=myimg)
    c.grid(row=0,column=0)
def f8():
    global c
    global myimg
    global mimg
    global imagename
    global glb_img_name
    global image1
    global width,height
    b1=Image.open(glb_img_name).resize((width,height),Image.ANTIALIAS).convert("RGB")
    width,height =b1.size
    mimg=cus4(height,width,b1)
    but1=ImageTk.PhotoImage(mimg)
    myimg=but1
    image1=b1
    c.create_image(0,0,anchor=NW,image=myimg)
    c.grid(row=0,column=0)
def f9():
    global c
    global myimg
    global mimg
    global imagename
    global glb_img_name
    global image1
    global width,height
    b1=Image.open(glb_img_name).resize((width,height),Image.ANTIALIAS).convert("RGB")
    b1 = b1.filter(ImageFilter.BLUR)
    mimg=b1
    but1=ImageTk.PhotoImage(b1)
    myimg=but1
    image1=b1
    c.create_image(0,0,anchor=NW,image=myimg)
    c.grid(row=0,column=0)
def f10():
    global c
    global myimg
    global mimg
    global imagename
    global glb_img_name
    global image1
    global width,height
    b1=Image.open(glb_img_name).resize((width,height),Image.ANTIALIAS).convert("RGB")
    b1 = b1.filter(ImageFilter.CONTOUR)
    mimg=b1
    but1=ImageTk.PhotoImage(b1)
    myimg=but1
    image1=b1
    c.create_image(0,0,anchor=NW,image=myimg)
    c.grid(row=0,column=0)
def f11():
    global c
    global myimg
    global mimg
    global imagename
    global glb_img_name
    global image1
    global width,height
    b1=Image.open(glb_img_name).resize((width,height),Image.ANTIALIAS).convert("RGB")
    b1 = b1.filter(ImageFilter.EMBOSS)
    mimg=b1
    but1=ImageTk.PhotoImage(b1)
    myimg=but1
    image1=b1
    c.create_image(0,0,anchor=NW,image=myimg)
    c.grid(row=0,column=0)
def f12():
    global c
    global myimg
    global mimg
    global imagename
    global glb_img_name
    global image1
    global width,height
    b1=Image.open(glb_img_name).resize((width,height),Image.ANTIALIAS).convert("RGB")
    b1 = b1.filter(ImageFilter.EDGE_ENHANCE)
    mimg=b1
    but1=ImageTk.PhotoImage(b1)
    myimg=but1
    image1=b1
    c.create_image(0,0,anchor=NW,image=myimg)
    c.grid(row=0,column=0)
def ori():
    global c
    global myimg
    global mimg
    global imagename
    global image1
    global glb_img_name
    global width,height
    b1=Image.open(glb_img_name).resize((width,height),Image.ANTIALIAS).convert("RGB")
    mimg=b1
    image1=b1
    but1=ImageTk.PhotoImage(b1)
    myimg=but1
    c.create_image(0,0,anchor=NW,image=myimg)
    c.grid(row=0,column=0)
myimg=ImageTk.PhotoImage(img)
c.create_image(0,0,anchor=NW,image=myimg)
c.grid(row=0,column=0)
toolbo[2]=Frame(root,relief=RIDGE,bd=3)
b1=Image.open(glb_img_name).resize((70,70),Image.ANTIALIAS).convert("RGB")
b2=Image.open(glb_img_name).resize((70,70),Image.ANTIALIAS).convert("RGB")
b3=Image.open(glb_img_name).resize((70,70),Image.ANTIALIAS).convert("RGB")
b4=Image.open(glb_img_name).resize((70,70),Image.ANTIALIAS).convert("RGB")
b5=Image.open(glb_img_name).resize((70,70),Image.ANTIALIAS).convert("RGB")
b6=Image.open(glb_img_name).resize((70,70),Image.ANTIALIAS).convert("RGB")
b7=Image.open(glb_img_name).resize((70,70),Image.ANTIALIAS).convert("RGB")
b8=Image.open(glb_img_name).resize((70,70),Image.ANTIALIAS).convert("RGB")
b9=Image.open(glb_img_name).resize((70,70),Image.ANTIALIAS).convert("RGB")
b10=Image.open(glb_img_name).resize((70,70),Image.ANTIALIAS).convert("RGB")
b11=Image.open(glb_img_name).resize((70,70),Image.ANTIALIAS).convert("RGB")
b12=Image.open(glb_img_name).resize((70,70),Image.ANTIALIAS).convert("RGB")
b13=Image.open(glb_img_name).resize((70,70),Image.ANTIALIAS).convert("RGB")
b14=Image.open(glb_img_name).resize((70,70),Image.ANTIALIAS).convert("RGB")
but1=ImageTk.PhotoImage(grey(70,70,b1))
but2=ImageTk.PhotoImage(red(70,70,b2))
but3=ImageTk.PhotoImage(blue(70,70,b3))
but4=ImageTk.PhotoImage(green(70,70,b4))
but5=ImageTk.PhotoImage(cus1(70,70,b5))
but6=ImageTk.PhotoImage(cus2(70,70,b6))
but7=ImageTk.PhotoImage(cus3(70,70,b7))
but8=ImageTk.PhotoImage(cus4(70,70,b8))
but9=ImageTk.PhotoImage(cus5(b9))
but10=ImageTk.PhotoImage(cus6(b10))
but11=ImageTk.PhotoImage(cus7(b11))
but12=ImageTk.PhotoImage(cus8(b12))
but13=ImageTk.PhotoImage(b13)
button=Button(toolbo[2],image=but1,command=f1,borderwidth=0).grid(row=1,column=0,padx=2,pady=2)
button1=Button(toolbo[2],image=but2,command=f2,borderwidth=0).grid(row=1,column=1,padx=2,pady=2)
button2=Button(toolbo[2],image=but3,command=f3,borderwidth=0).grid(row=1,column=2,padx=2,pady=2)
button3=Button(toolbo[2],image=but4,command=f4,borderwidth=0).grid(row=1,column=3,padx=2,pady=2)
button4=Button(toolbo[2],image=but5,command=f5,borderwidth=0).grid(row=2,column=0,padx=2,pady=2)
button5=Button(toolbo[2],image=but6,command=f6,borderwidth=0).grid(row=2,column=1,padx=2,pady=2)
button6=Button(toolbo[2],image=but7,command=f7,borderwidth=0).grid(row=2,column=2,padx=2,pady=2)
button7=Button(toolbo[2],image=but8,command=f8,borderwidth=0).grid(row=2,column=3,padx=2,pady=2)
button8=Button(toolbo[2],image=but9,command=f9,borderwidth=0).grid(row=3,column=0,padx=2,pady=2)
button9=Button(toolbo[2],image=but10,command=f10,borderwidth=0).grid(row=3,column=1,padx=2,pady=2)
button10=Button(toolbo[2],image=but11,command=f11,borderwidth=0).grid(row=3,column=2,padx=2,pady=2)
button11=Button(toolbo[2],image=but12,command=f12,borderwidth=0).grid(row=3,column=3,padx=2,pady=2)
def save_fun():
    global mimg
    global glb_img_name
    global c
    global image1
    global toolbo
    global draw
    global b1,b2,b3,b4,b5,b6,b7,b8,b9,b10,b11,b12,b13,b14
    global but1,but2,but3,but4,but5,but6,but7,but8,but9,but10,but11,but12,but13
    global button,button1,button2,button3,button4,button5,button6,button7,button8,button9,button10,button11,button12
    mimg.save("processed/edited2.png",quality=200)
    glb_img_name="processed/edited2.png"
    mimg=Image.open(glb_img_name)
    image1=mimg
    draw=ImageDraw.Draw(image1)
    myimg=ImageTk.PhotoImage(img)
    c.create_image(0,0,anchor=NW,image=myimg)
    c.grid(row=0,column=0)
    b1=Image.open(glb_img_name).resize((70,70),Image.ANTIALIAS).convert("RGB")
    b2=Image.open(glb_img_name).resize((70,70),Image.ANTIALIAS).convert("RGB")
    b3=Image.open(glb_img_name).resize((70,70),Image.ANTIALIAS).convert("RGB")
    b4=Image.open(glb_img_name).resize((70,70),Image.ANTIALIAS).convert("RGB")
    b5=Image.open(glb_img_name).resize((70,70),Image.ANTIALIAS).convert("RGB")
    b6=Image.open(glb_img_name).resize((70,70),Image.ANTIALIAS).convert("RGB")
    b7=Image.open(glb_img_name).resize((70,70),Image.ANTIALIAS).convert("RGB")
    b8=Image.open(glb_img_name).resize((70,70),Image.ANTIALIAS).convert("RGB")
    b9=Image.open(glb_img_name).resize((70,70),Image.ANTIALIAS).convert("RGB")
    b10=Image.open(glb_img_name).resize((70,70),Image.ANTIALIAS).convert("RGB")
    b11=Image.open(glb_img_name).resize((70,70),Image.ANTIALIAS).convert("RGB")
    b12=Image.open(glb_img_name).resize((70,70),Image.ANTIALIAS).convert("RGB")
    b13=Image.open(glb_img_name).resize((70,70),Image.ANTIALIAS).convert("RGB")
    b14=Image.open(glb_img_name).resize((70,70),Image.ANTIALIAS).convert("RGB")
    but1=ImageTk.PhotoImage(grey(70,70,b1))
    but2=ImageTk.PhotoImage(red(70,70,b2))
    but3=ImageTk.PhotoImage(blue(70,70,b3))
    but4=ImageTk.PhotoImage(green(70,70,b4))
    but5=ImageTk.PhotoImage(cus1(70,70,b5))
    but6=ImageTk.PhotoImage(cus2(70,70,b6))
    but7=ImageTk.PhotoImage(cus3(70,70,b7))
    but8=ImageTk.PhotoImage(cus4(70,70,b8))
    but9=ImageTk.PhotoImage(cus5(b9))
    but10=ImageTk.PhotoImage(cus6(b10))
    but11=ImageTk.PhotoImage(cus7(b11))
    but12=ImageTk.PhotoImage(cus8(b12))
    but13=ImageTk.PhotoImage(b13)
    button=Button(toolbo[2],image=but1,command=f1,borderwidth=0).grid(row=1,column=0,padx=2,pady=2)
    button1=Button(toolbo[2],image=but2,command=f2,borderwidth=0).grid(row=1,column=1,padx=2,pady=2)
    button2=Button(toolbo[2],image=but3,command=f3,borderwidth=0).grid(row=1,column=2,padx=2,pady=2)
    button3=Button(toolbo[2],image=but4,command=f4,borderwidth=0).grid(row=1,column=3,padx=2,pady=2)
    button4=Button(toolbo[2],image=but5,command=f5,borderwidth=0).grid(row=2,column=0,padx=2,pady=2)
    button5=Button(toolbo[2],image=but6,command=f6,borderwidth=0).grid(row=2,column=1,padx=2,pady=2)
    button6=Button(toolbo[2],image=but7,command=f7,borderwidth=0).grid(row=2,column=2,padx=2,pady=2)
    button7=Button(toolbo[2],image=but8,command=f8,borderwidth=0).grid(row=2,column=3,padx=2,pady=2)
    button8=Button(toolbo[2],image=but9,command=f9,borderwidth=0).grid(row=3,column=0,padx=2,pady=2)
    button9=Button(toolbo[2],image=but10,command=f10,borderwidth=0).grid(row=3,column=1,padx=2,pady=2)
    button10=Button(toolbo[2],image=but11,command=f11,borderwidth=0).grid(row=3,column=2,padx=2,pady=2)
    button11=Button(toolbo[2],image=but12,command=f12,borderwidth=0).grid(row=3,column=3,padx=2,pady=2)
def ori():
    global c
    global myimg
    global mimg
    global imagename
    global image1
    global glb_img_name
    global width,height
    b1=Image.open(glb_img_name).resize((width,height),Image.ANTIALIAS).convert("RGB")
    mimg=b1
    image1=b1
    but1=ImageTk.PhotoImage(b1)
    myimg=but1
    c.create_image(0,0,anchor=NW,image=myimg)
    c.grid(row=0,column=0)
    save_fun()
def glbreset():
    global c
    global myimg
    global mimg
    global imagename
    global image1
    global original_name_of_the_image
    global glb_img_name
    global ori
    global width,height
    global save_panniya_cha

    save_panniya_cha=0
    glb_img_name=original_name_of_the_image

    color_thief = ColorThief(glb_img_name)
    dominant_color = color_thief.get_color(quality=1)
    ds=_from_rgb((dominant_color))
    c.config(bg=ds)
    root.config(bg=ds)

    copy=Image.open(glb_img_name)
    owidth,oheight=copy.size
    width,height=width_height(owidth,oheight)
    b1=Image.open(glb_img_name).resize((width,height),Image.ANTIALIAS).convert("RGB")
    mimg=b1
    image1=b1
    but1=ImageTk.PhotoImage(b1)
    myimg=but1
    c.config(width=width,height=height)
    c.create_image(0,0,anchor=NW,image=myimg)
    c.grid(row=0,column=0)
    removeimgon()
    removetext()
    save1()
    save_fun()
    reset_something()
reset=Button(toolbo[1],text="Reset",command=ori).grid(row=1,column=5,padx=5)
save=Button(toolbo[2],text="Apply",command=save_fun).grid(row=4,column=0,pady=5,padx=5)
reset=Button(toolbo[2],text="Reset",command=ori).grid(row=4,column=1,padx=5,pady=5)
erase=Button(toolbo[2],text="Erase",command=eraser2).grid(row=4,column=2,padx=5,pady=5)
sca2=Scale(toolbo[2],from_=0,to=100,orient=VERTICAL,command=brushsize,length=200)
sca2.grid(row=1,column=7,rowspan=4)

#image_on_image
myimg=ImageTk.PhotoImage(Image.open(glb_img_name))
mimg=Image.open(glb_img_name)
img = Image.open(glb_img_name)
imgpresent=0
def img_on():
    global imgname
    global img2
    global b1
    global img3
    global sca
    global glbsize
    global mimg
    global c
    global what
    global imgpresent
    global currentimg
    global img_on_width,img_on_height
    global glb_img_name
    imgpresent=1
    try:
        mimg=Image.open(glb_img_name)
        img = Image.open(glb_img_name)
        myimg=ImageTk.PhotoImage(img)
        imgname=filedialog.askopenfilename(initialdir="/Desktop/python codes",title="open images",filetypes=(("png files","*.png"),("jpg files","*.jpg"),))
        if(imgname!=""):
            img2=Image.open(imgname)
            img_on_width,img_on_height=img2.size
            currentimg=imgname
            b1=Image.open(currentimg).resize((int(img_on_width*(glbsize/100)+img_on_width*(1/100)),int(img_on_height*(glbsize/100)+img_on_height*(1/100))),Image.ANTIALIAS)
            img2=ImageTk.PhotoImage(b1)
            img5=ImageTk.PhotoImage(b1)
            img3=c.create_image(10,10,anchor=NW,image=img2)
            what="imageon"
        else:
           imgpresent=0
    except:
        if(what=="imageon" and imgpresent==0):
            imgpresent=1
        else:
            imgpresent=0
xx=0
yy=0
c=Canvas(root,width=width,height=height,bg="white")
c.grid(row=0,column=0)
myimg=ImageTk.PhotoImage(img.resize((width,height),Image.ANTIALIAS))
c.create_image(0,0,anchor=NW,image=myimg)
c.grid(row=0,column=0)
c.bind('<B1-Motion>',paint)
glbsize=10
x=10
y=10
img_on_width,img_on_height=0,0
def removeimgon():
    global c
    global myimg
    global mimg
    global imagename
    global image1
    global imgpresent
    global img_on_width,img_on_height
    global glb_img_name
    global width,height
    b1=Image.open(glb_img_name).resize((width,height),Image.ANTIALIAS).convert("RGB")
    imgpresent=0
    mimg=b1
    image1=b1
    but1=ImageTk.PhotoImage(b1)
    myimg=but1
    c.create_image(0,0,anchor=NW,image=myimg)
    c.grid(row=0,column=0)
    save_fun()
def trans_paste(fg_img,bg_img,alpha=1.0,box=(0,0)):
    fg_img_trans = Image.new("RGBA",fg_img.size)
    fg_img_trans = Image.blend(fg_img_trans,fg_img,alpha)
    bg_img.paste(fg_img_trans,box,fg_img_trans)
    return bg_img   
def save4():
    global xx1,yy1
    global currentimg
    global image
    global glbsize
    global mimg
    global image1
    global img_on_width,img_on_height
    global x1,y1
    global imgpresent
    global c
    global glb_img_name
    global height,width
    if(imgpresent):
        Image1 = Image.open(glb_img_name).resize((width,height),Image.ANTIALIAS)
        Image1copy = Image1.copy()
        mask_im=Image.open(currentimg).convert('L').resize((glbsize,glbsize),Image.ANTIALIAS)
        mask_im2=Image.open(glb_img_name).resize((width,height),Image.ANTIALIAS).convert('L')
        Image2 = Image.open(currentimg).resize((int(img_on_width*(glbsize/100)+img_on_width*(1/100)),int(img_on_height*(glbsize/100)+img_on_height*(1/100))),Image.ANTIALIAS)
        width1,height1=Image2.size
        width2=width1/2
        height2=height1/2
        Image2copy = Image2.copy()
        Image1copy.paste(Image2, (int(xx1-width2),int( yy1-height2)))
        try:
            bg_img = Image.open(glb_img_name)
            fg_img = Image.open(currentimg).resize((int(img_on_width*(glbsize/100)+img_on_width*(1/100)),int(img_on_height*(glbsize/100)+img_on_height*(1/100))),Image.ANTIALIAS)
            p = trans_paste(fg_img,bg_img,1.0,(int(xx1-width2),int( yy1-height2)))
            p.save('processed/edited2.png',quality=200)
        except:
            Image1copy.save('processed/edited2.png',quality=200)
        glb_img_name="processed/edited2.png"
        imgpresent=0
        img = Image.open(glb_img_name).resize((width,height),Image.ANTIALIAS)
        myimg=ImageTk.PhotoImage(img)
        c.create_image(0,0,anchor=NW,image=myimg)
        c.grid(row=0,column=0)
        glb_img_name="processed/edited2.png"
        mimg=Image.open(glb_img_name).resize((width,height),Image.ANTIALIAS)
        save_fun()
        removeimgon()
    else:
        Image1 = Image.open(glb_img_name)
        Image1.save('processed/edited2.png',quality=100)
        glb_img_name='processed/edited2.png'
def moves1(event):
    global myimg
    global img3
    global currentimg
    global img2
    global glbsize
    global glb_img_name
    global xx,yy
    global imgpresent
    global what
    what="nothing"
    if(imgpresent):
        img = Image.open(glb_img_name)
        myimg=ImageTk.PhotoImage(img)
        c.create_image(0,0,anchor=NW,image=myimg)
        xx,yy=event.x,event.y
        img3=c.create_image(xx,yy,image=img2)
        c.grid(row=0,column=0)
def image_size(val):
    global glbsize
    glbsize=int(val)
    global c
    global xx,yy
    global xx1,yy1
    global img_on_width,img_on_height
    global currentimg
    global img2
    global imgpresent
    if(imgpresent):
        b1=Image.open(currentimg).resize((int(img_on_width*(glbsize/100)+img_on_width*(1/100)),int(img_on_height*(glbsize/100)+img_on_height*(1/100))),Image.ANTIALIAS)
        img2=ImageTk.PhotoImage(b1)
        img3=c.create_image(53,78,anchor=NW,image=img2)
        c.grid(row=0,column=0)
toolbo[3]=Frame(root,relief=RIDGE,bd=3)
sa=Button(toolbo[3],text="ADD",command=save4).grid(row=0,column=0,padx=10,pady=10)
scaf=Scale(toolbo[3],from_=0,to=150,orient=HORIZONTAL,command=image_size,length=200)
scaf.set(10)
scaf.grid(row=2,column=0,padx=10,columnspan=3)
but=Button(toolbo[3],text="Open Image",command=img_on).grid(row=0,column=1,padx=10,pady=10)
re=Button(toolbo[3],text="Reset",command=removeimgon).grid(row=0,column=2,padx=10,pady=10)

#Adjust
brightness_level=0
contrast_level=0
saturation_level=0
sharpness_level=0
toolbo[5]=Frame(root,relief=RIDGE,bd=3)
def fxs(bri):
    global brightness_level
    global contrast_level
    global saturation_level
    global sharpness_level
    global c
    global myimg
    global mimg
    global imagename
    global glb_img_name
    global image1
    global width,height
    b1=Image.open(glb_img_name).resize((width,height),Image.ANTIALIAS)
    brightness_level=bri
    enhancer = ImageEnhance.Brightness(b1)
    image=enhancer.enhance(3*(int(brightness_level)/100)+1)
    enhancer = ImageEnhance.Contrast(image)
    image=enhancer.enhance(3*(int(contrast_level)/100)+1)    
    enhancer = ImageEnhance.Color(image)
    image=enhancer.enhance(8*(int(saturation_level)/100)+1)
    enhancer = ImageEnhance.Sharpness(image)
    image=enhancer.enhance(4*(int(sharpness_level)/100)+1)
    b1=Image.open(glb_img_name).resize((width,height),Image.ANTIALIAS).convert("RGB")
    width,height =b1.size
    mimg=image
    but1=ImageTk.PhotoImage(mimg)
    myimg=but1
    image1=b1
    c.create_image(0,0,anchor=NW,image=myimg)
    c.grid(row=0,column=0)
def fxs1(bri):
    global brightness_level
    global contrast_level
    global saturation_level
    global sharpness_level
    global c
    global myimg
    global mimg
    global imagename
    global glb_img_name
    global image1
    global width,height
    b1=Image.open(glb_img_name).resize((width,height),Image.ANTIALIAS)
    contrast_level=bri
    enhancer = ImageEnhance.Brightness(b1)
    image=enhancer.enhance(3*(int(brightness_level)/100)+1)
    enhancer = ImageEnhance.Contrast(image)
    image=enhancer.enhance(3*(int(contrast_level)/100)+1)    
    enhancer = ImageEnhance.Color(image)
    image=enhancer.enhance(8*(int(saturation_level)/100)+1)
    enhancer = ImageEnhance.Sharpness(image)
    image=enhancer.enhance(4*(int(sharpness_level)/100)+1)
    b1=Image.open(glb_img_name).resize((width,height),Image.ANTIALIAS).convert("RGB")
    width,height =b1.size
    mimg=image
    but1=ImageTk.PhotoImage(mimg)
    myimg=but1
    image1=b1
    c.create_image(0,0,anchor=NW,image=myimg)
    c.grid(row=0,column=0)
def fxs2(bri):
    global brightness_level
    global contrast_level
    global saturation_level
    global sharpness_level
    global c
    global myimg
    global mimg
    global imagename
    global glb_img_name
    global image1
    global width,height
    b1=Image.open(glb_img_name).resize((width,height),Image.ANTIALIAS)
    saturation_level=bri
    enhancer = ImageEnhance.Brightness(b1)
    image=enhancer.enhance(3*(int(brightness_level)/100)+1)
    enhancer = ImageEnhance.Contrast(image)
    image=enhancer.enhance(3*(int(contrast_level)/100)+1)    
    enhancer = ImageEnhance.Color(image)
    image=enhancer.enhance(8*(int(saturation_level)/100)+1)
    enhancer = ImageEnhance.Sharpness(image)
    image=enhancer.enhance(4*(int(sharpness_level)/100)+1)
    b1=Image.open(glb_img_name).resize((width,height),Image.ANTIALIAS).convert("RGB")
    width,height =b1.size
    mimg=image
    but1=ImageTk.PhotoImage(mimg)
    myimg=but1
    image1=b1
    c.create_image(0,0,anchor=NW,image=myimg)
    c.grid(row=0,column=0)
def fxs3(bri):
    global brightness_level
    global contrast_level
    global saturation_level
    global sharpness_level
    global c
    global myimg
    global mimg
    global imagename
    global glb_img_name
    global image1
    global width,height
    b1=Image.open(glb_img_name).resize((width,height),Image.ANTIALIAS)
    sharpness_level=bri
    enhancer = ImageEnhance.Brightness(b1)
    image=enhancer.enhance(3*(int(brightness_level)/100)+1)
    enhancer = ImageEnhance.Contrast(image)
    image=enhancer.enhance(3*(int(contrast_level)/100)+1)    
    enhancer = ImageEnhance.Color(image)
    image=enhancer.enhance(8*(int(saturation_level)/100)+1)
    enhancer = ImageEnhance.Sharpness(image)
    image=enhancer.enhance(4*(int(sharpness_level)/100)+1)
    b1=Image.open(glb_img_name).resize((width,height),Image.ANTIALIAS).convert("RGB")
    width,height =b1.size
    mimg=image
    but1=ImageTk.PhotoImage(mimg)
    myimg=but1
    image1=b1
    c.create_image(0,0,anchor=NW,image=myimg)
    c.grid(row=0,column=0)
def reset_something():
    global brightness_level
    global contrast_level
    global saturation_level
    global sharpness_level
    global brux1,bruy1
    global brux,bruy
    global scalio
    global scalio1
    global scalio2
    global scalio3
    global sca,sca2,sca4,sca5
    brux1,bruy1=10,10
    brux,bruy=0,0
    brightness_level=0
    contrast_level=0
    saturation_level=0
    sharpness_level=0
    scalio.set(0)
    scalio1.set(0)
    scalio2.set(0)
    scalio3.set(0)
    sca.set(0)
    sca2.set(0)
    sca4.set(10)
    sca5.set(10)
def fun_fun():
    save_fun()
    reset_something()
la=Label(toolbo[5],text="Brightness").grid(row=3,column=1)
la=Label(toolbo[5],text="Contrast").grid(row=5,column=1)
la=Label(toolbo[5],text="Saturation").grid(row=7,column=1)
la=Label(toolbo[5],text="Sharpness").grid(row=9,column=1)
sa=Button(toolbo[5],text="SAVE",command=fun_fun).grid(row=10,column=1,padx=5)
scalio=Scale(toolbo[5],from_=0,to=100,orient=HORIZONTAL,command=fxs,length=200)
scalio.grid(row=2,column=1,padx=10)
scalio1=Scale(toolbo[5],from_=0,to=100,orient=HORIZONTAL,command=fxs1,length=200)
scalio1.grid(row=4,column=1,padx=10)
scalio2=Scale(toolbo[5],from_=0,to=100,orient=HORIZONTAL,command=fxs2,length=200)
scalio2.grid(row=6,column=1,padx=10)
scalio3=Scale(toolbo[5],from_=0,to=100,orient=HORIZONTAL,command=fxs3,length=200)
scalio3.grid(row=8,column=1,padx=10)
#text_on_image
xx=53
yy=78
textsize=10
currentla_enna_font="Sacramento"
myimg=ImageTk.PhotoImage(Image.open(glb_img_name))
mimg=Image.open(glb_img_name)
img = Image.open(glb_img_name).convert("RGB")
c=Canvas(root,width=width,height=height,bg="white")
c.grid(row=0,column=0)
texton=0
fcolor="red"
names=("Sacramento","Source Code Pro","Roboto","Lobster","Cookie","Shadows Into Light")
fontnames=["Sacramento-Regular.ttf","SourceCodePro-Regular.ttf","Roboto-Regular.ttf","Lobster-Regular.ttf","Cookie-Regular.ttf","ShadowsIntoLight-Regular"]
currentfont=0
def removetext():
    global c
    global xx,yy
    global currentimg
    global word
    global img3
    global fcolor
    global height
    global currentla_enna_font
    global width
    global myimg
    global img
    global fheight,fwidth
    global texton
    global what
    global textsize
    word=e.get()
    img = Image.open(glb_img_name)
    myimg=ImageTk.PhotoImage(img.resize((width,height),Image.ANTIALIAS))
    c.create_image(0,0,anchor=NW,image=myimg)
    img3=c.create_text(xx,yy,text="",fill=fcolor,font=(currentla_enna_font,textsize))
    bounds = c.bbox(img3)
    fwidth =( bounds[2] - bounds[0])/2
    fheight = (bounds[3] - bounds[1])/2
    texton=0
    c.grid(row=0,column=0)
def chose2():
    global fcolor
    global mybutton
    global bot
    global texton
    global what
    global c
    global xx,yy
    global currentimg
    global word
    global img3
    global height
    global fheight,fwidth
    global width
    global myimg
    global currentla_enna_font
    global img
    global textsize
    mycolor=colorchooser.askcolor()[1]
    if(mycolor):
        fcolor= mycolor
    mybutton=Button(toolbo[4],text="  ",command=chose2,fg=fcolor,bg=fcolor).grid(row=1,column=3)
    if(texton):
        word=e.get()
        img = Image.open(glb_img_name)
        myimg=ImageTk.PhotoImage(img.resize((width,height),Image.ANTIALIAS))
        c.create_image(0,0,anchor=NW,image=myimg)
        img3=c.create_text(xx,yy,text=word,fill=fcolor,font=(currentla_enna_font,textsize))
        bounds = c.bbox(img3)
        fwidth =( bounds[2] - bounds[0])/2
        fheight = (bounds[3] - bounds[1])/2
        c.grid(row=0,column=0)
def textsizechange(val):
    global c
    global xx,yy
    global currentimg
    global word
    global img3
    global what
    global fcolor
    global currentla_enna_font
    global textsize
    global height
    global texton
    global fheight,fwidth
    global width
    global myimg
    global sca
    global img
    if(texton):
        word=e.get()
        img = Image.open(glb_img_name)
        myimg=ImageTk.PhotoImage(img.resize((width,height),Image.ANTIALIAS))
        c.create_image(0,0,anchor=NW,image=myimg)
        textsize=int(val)
        img3=c.create_text(xx,yy,text=word,fill=fcolor,font=(currentla_enna_font,textsize))
        bounds = c.bbox(img3)
        fwidth =( bounds[2] - bounds[0])/2
        fheight = (bounds[3] - bounds[1])/2
        c.grid(row=0,column=0)
def text1():
    global c
    global xx,yy
    global currentimg
    global word
    global img3
    global fcolor
    global height
    global fheight,fwidth
    global currentla_enna_font
    global width
    global myimg
    global img
    global texton
    global what
    global textsize
    global what
    what="texton"
    word=e.get()
    img = Image.open(glb_img_name)
    myimg=ImageTk.PhotoImage(img.resize((width,height),Image.ANTIALIAS))
    c.create_image(0,0,anchor=NW,image=myimg)
    img3=c.create_text(xx,yy,text=word,fill=fcolor,font=(currentla_enna_font,textsize))
    bounds = c.bbox(img3)
    fwidth =( bounds[2] - bounds[0])/2
    fheight = (bounds[3] - bounds[1])/2
    texton=1
    c.grid(row=0,column=0)
def save3():
    global xx,yy
    global height,width
    global fheight,fwidth
    global word
    global fcolor
    global textsize
    global currentla_enna_font
    global fontnames
    global Image1
    global img,mimg,c
    global mimg
    global e
    global texton
    global glb_img_name
    if(xx==0 and yy==0):
        xx,yy=58,73
    font=ImageFont.load_default()
    if(texton):
        Image1 = Image.open(glb_img_name).resize((width,height),Image.ANTIALIAS)
        draw = ImageDraw.Draw(Image1)
        fnt = ImageFont. truetype(fontnames[names.index(currentla_enna_font)],textsize+int(textsize*34.83/100))
        draw.text((1+xx-fwidth,0.7+yy-fheight), word, fill=fcolor,font=fnt)
        mimg=Image1
        Image1.save("processed/edited2.png",quality=200)
        glb_img_name="processed/edited2.png"
        img = Image.open(glb_img_name).resize((width,height),Image.ANTIALIAS)
        myimg=ImageTk.PhotoImage(img)
        c.create_image(0,0,anchor=NW,image=myimg)
        texton=0
        save_fun()
        removetext()
def moves(event):
    global myimg
    global img3
    global currentla_enna_font
    global xx,yy
    global height
    global textsize
    global width
    global what
    global Image1
    global original_name
    global fcolor
    global word
    global texton
    if(what=="texton"):
        if(texton):
            img = Image.open(glb_img_name)
            myimg=ImageTk.PhotoImage(img.resize((width,height),Image.ANTIALIAS))
            c.create_image(0,0,anchor=NW,image=myimg)
            xx,yy=event.x,event.y
            img3=c.create_text(xx,yy,text=word,fill=fcolor,font=(currentla_enna_font,textsize))
            c.grid(row=0,column=0)
def prlx():
    global currentfont
    global c
    global xx,yy
    global currentimg
    global word
    global img3
    global currentla_enna_font
    global fcolor
    global height
    global width
    global fheight,fwidth
    global myimg
    global img
    global texton
    global textsize
    nams=spi.get()
    currentfont=names.index(spi.get())
    spi.configure(font=(names[currentfont],13))
    word=e.get()
    currentla_enna_font=names[currentfont]
    if(texton):
        img = Image.open(glb_img_name)
        myimg=ImageTk.PhotoImage(img.resize((width,height),Image.ANTIALIAS))
        c.create_image(0,0,anchor=NW,image=myimg)
        img3=c.create_text(xx,yy,text=word,fill=fcolor,font=(names[currentfont],textsize))
        bounds = c.bbox(img3)
        fwidth =( bounds[2] - bounds[0])/2
        fheight = (bounds[3] - bounds[1])/2
        texton=1
        c.grid(row=0,column=0)
myimg=ImageTk.PhotoImage(img.resize((width,height),Image.ANTIALIAS))
c.create_image(0,0,anchor=NW,image=myimg)
c.grid(row=0,column=0)
c.bind("<B1-Motion>",paint)
toolbo[4]=Frame(root,relief=RIDGE,bd=3)
e=Entry(toolbo[4])
e.insert(0,"Sample text")
e.grid(row=1,column=0,padx=5,pady=10)
sa=Button(toolbo[4],text="SAVE",command=save3).grid(row=1,column=1,padx=5,pady=10)
ok=Button(toolbo[4],text="ADD",command=text1).grid(row=1,column=2,padx=5,pady=10)
mybutton=Button(toolbo[4],text="  ",command=chose2,bg=fcolor,fg=fcolor).grid(row=1,column=3,padx=5,pady=10)
spi=Spinbox(toolbo[4],values=names,width=15,font=(names[currentfont],13),command=prlx)
spi.grid(row=4,column=0,columnspan=4,pady=5)
sca8=Scale(toolbo[4],from_=0,to=100,orient=HORIZONTAL,command=textsizechange,length=200)
sca8.grid(row=5,column=0,columnspan=4)
removet=Button(toolbo[4],text="Remove text",command=removetext).grid(row=6,column=0,padx=5,columnspan=4)
def take_the_button():
    global toolbo
    global what
    what="nothing"
    erase=Button(toolbo[1],text="Erase",command=eraser,bg="white",fg="black").grid(row=1,column=2)
    pai=Button(toolbo[1],text="paint",command=pain,bg="white",fg="black").grid(row=1,column=4)

def retract():
    global c
    global width,height
    global countrotate
    countrotate=0
    c.config(width=width,height=height)
#changing layout functions
def one_frame():
    global toolbo
    global frameactive
    retract()
    toolbo[frameactive].grid_forget()
    frameactive=1
    toolbo[frameactive].grid(row=0,column=1,pady=10,padx=10)
    toolbo[frameactive].grid_propagate(0)
    removetext()
    removeimgon()
    reset_something()
def second_frame():
    global toolbo
    global frameactive
    retract()
    take_the_button()
    toolbo[frameactive].grid_forget()
    frameactive=2
    toolbo[frameactive].grid(row=0,column=1,padx=10,pady=10)
    toolbo[frameactive].grid_propagate(0)
    removetext()
    reset_something()
def third_frame():
    global toolbo
    global frameactive
    retract()
    take_the_button()
    toolbo[frameactive].grid_forget()
    frameactive=3
    toolbo[frameactive].grid(row=0,column=1,pady=10,padx=10)
    toolbo[frameactive].grid_propagate(0)
    removetext()
    removeimgon()
    reset_something()
def fourth_frame():
    global toolbo
    global frameactive
    retract()
    take_the_button()
    toolbo[frameactive].grid_forget()
    frameactive=4
    toolbo[frameactive].grid(row=0,column=1,pady=10,padx=10)
    toolbo[frameactive].grid_propagate(0)
    removeimgon()
    reset_something()
def fifth_frame():
    global toolbo
    global frameactive
    retract()
    take_the_button()
    toolbo[frameactive].grid_forget()
    frameactive=5
    toolbo[frameactive].grid(row=0,column=1,pady=10,padx=10)
    toolbo[frameactive].grid_propagate(0)
    reset_something()
    removeimgon()
def sixth_frame():
    global toolbo
    global frameactive
    global x1,x2,y1,y2
    global c
    global width,height
    global myimg
    global brux1,bruy1
    global what
    retract()
    take_the_button()
    toolbo[frameactive].grid_forget()
    frameactive=6
    toolbo[frameactive].grid(row=0,column=1,pady=10,padx=10)
    toolbo[frameactive].grid_propagate(0)
    removeimgon()
    what="crop"
    x1,y1=int(width/2)-1-int(10/2),(int(height/2))-1-int(10/2)
    x2,y2=(int(width/2))+10-int(10/2),(int(height/2))+10-int(10/2)
    c.create_image(0,0,anchor=NW,image=myimg)
    c1=c.create_rectangle(x1,y1,x2,y2,fill=None,outline="black",width=5)
    reset_something()
def seventh_frame():
    global toolbo
    global frameactive
    global c
    global myimg
    global brux1,bruy1
    global what
    c.delete("all")
    take_the_button()
    toolbo[frameactive].grid_forget()
    frameactive=7
    toolbo[frameactive].grid(row=0,column=1,pady=10,padx=10)
    toolbo[frameactive].grid_propagate(0)
    c.create_image(0,0,anchor=NW,image=myimg)
    removeimgon()
    reset_something()
#file menu functions
def select_another_image():
    global glb_img_name
    global width,height
    global c
    global original_name_of_the_image
    global countrotate
    countrotate=0
    imgagename=filedialog.askopenfilename(initialdir="/Desktop/python codes",title="open images",filetypes=(("png files","*.png"),("jpg files","*.jpg"),))
    if(imgagename==""):
        return
    glb_img_name=imgagename
    original_name_of_the_image=glb_img_name
    color_thief = ColorThief(glb_img_name)
    dominant_color = color_thief.get_color(quality=1)
    ds=_from_rgb((dominant_color))
    c.config(bg=ds)
    root.config(bg=ds) 
    copy=Image.open(imgagename)
    owidth,oheight=copy.size
    width,height=width_height(owidth,oheight)
    c.config(width=width,height=height)
    c.grid(row=0,column=0)
    ori()
def save_as():
    global image1
    global glb_img_name
    global save_panniya_cha
    global owidth,oheight
    name=filedialog.asksaveasfile(initialdir="/Desktop/python codes",title="open images",filetypes=(("png files","*.png"),("jpg files","*.jpg"),),defaultextension=".png")
    if(name!=None):
        image1.save(name.name,quality=200)
        glb_img_name=name.name
        save_panniya_cha=1
        ori()
#crop image
brux1=10
bruy1=10
def brushsize1(value):
    global brux1,bruy1
    global width,height
    global count
    global img2
    global currentimg
    global firstah
    global myimg
    global brux,bruy
    global width,height
    global image2
    global images
    global draw
    global imagename
    global imgpresent
    global glb_img_name
    global c
    global img3
    global currentla_enna_font
    global xx,yy
    global xx1,yy1
    global textsize
    global Image1
    global fcolor
    global word
    global texton
    global x1,x2,y1,y2
    brux1=int(width*(int(value)/100))
    x1,y1=int(width/2)-1-int(brux1/2),(int(height/2))-1-int(bruy1/2)
    x2,y2=(int(width/2))+brux1-int(brux1/2),(int(height/2))+bruy1-int(bruy1/2)
    c.create_image(0,0,anchor=NW,image=myimg)
    c1=c.create_rectangle(x1,y1,x2,y2,fill=None,outline="black",width=5)
def brushsize2(value):
    global brux1,bruy1
    global width,height
    global count
    global img2
    global currentimg
    global firstah
    global myimg
    global brux,bruy
    global width,height
    global image2
    global images
    global draw
    global imagename
    global imgpresent
    global glb_img_name
    global c
    global img3
    global currentla_enna_font
    global xx,yy
    global xx1,yy1
    global textsize
    global Image1
    global fcolor
    global word
    global texton
    global what
    global c1
    global x1,x2,y1,y2
    bruy1=int(height*(int(value)/100))
    x1,y1=int(width/2)-1-int(brux1/2),(int(height/2))-1-int(bruy1/2)
    x2,y2=(int(width/2))+brux1-int(brux1/2),(int(height/2))+bruy1-int(bruy1/2)
    c.create_image(0,0,anchor=NW,image=myimg)
    c1=c.create_rectangle(x1,y1,x2,y2,fill=None,outline="black",width=5)
def crops():
    global imagename
    global glb_img_name
    global toolbo
    global image1
    global width,height
    global x1,y1,x2,y2
    global brux1,bruy1
    global b1,b2,b3,b4,b5,b6,b7,b8,b9,b10,b11,b12,b13,b14
    global but1,but2,but3,but4,but5,but6,but7,but8,but9,but10,but11,but12,but13
    global button,button1,button2,button3,button4,button5,button6,button7,button8,button9,button10,button11,button12
    b1=Image.open(glb_img_name).resize((width,height),Image.ANTIALIAS)
    v1,k1,v2,k2=x1+1,y1+1,x2-1,y2-1
    if v1<0:
        v1=0
    if k1<0:
        k1=0
    if v2>width:
        v2=width
    if k2>height:
        k2=height
    crop_rectangle = (v1, k1,v2, k2)
    cropped_im = b1.crop(crop_rectangle)
    cropped_im.save("processed/croped.png",quality=200)
    glb_img_name="processed/croped.png"
    color_thief = ColorThief(glb_img_name)
    dominant_color = color_thief.get_color(quality=1)
    ds=_from_rgb((dominant_color))
    c.config(bg=ds)
    root.config(bg=ds) 
    copy=Image.open("processed/croped.png")
    width,height=copy.size
    c.grid_forget()
    c.config(width=width,height=height)
    c.grid(row=0,column=0)
    ori()
    reset_something()
toolbo[6]=Frame(root,relief=RIDGE,bd=3)
las=Label(toolbo[6],text="Width ").grid(row=2,column=0,padx=5)
sca4=Scale(toolbo[6],from_=0,to=100,orient=HORIZONTAL,command=brushsize1,length=200)
sca4.grid(row=1,column=0)
las=Label(toolbo[6],text="Height").grid(row=4,column=0,padx=5)
sca5=Scale(toolbo[6],from_=0,to=100,orient=HORIZONTAL,command=brushsize2,length=200)
sca5.grid(row=3,column=0)
bt=Button(toolbo[6],text="crop",command=crops).grid(row=5,column=0,pady=10)
#rotate_image
countrotate=0
fwidth,fheight=width,height
def save_rotate_img():
    global c
    global myimg
    global mimg
    global imagename
    global image1
    global glb_img_name
    global width,height
    global countrotate
    global fwidth,fheight
    b1=Image.open(glb_img_name)
    if countrotate==1:
        b1=b1.rotate(90,expand = 1)
    elif countrotate==2:
        b1=b1.rotate(180,expand = 1)
    elif countrotate==3:
        b1=b1.rotate(270,expand = 1)
    elif countrotate==0:
        b1=b1
    owidth,oheight=b1.size
    fwidth,fheight=width_height(owidth,oheight)
    b1=b1.resize((fwidth,fheight),Image.ANTIALIAS)
    mimg=b1
    image1=b1
    but1=ImageTk.PhotoImage(b1)
    myimg=but1
    b1.save("processed/rotated.png",quality=200)
    width,height=fwidth,fheight
    glb_img_name="processed/rotated.png"
    c.create_image(0,0,anchor=NW,image=myimg)
    c.grid(row=0,column=0)
    ori()
def rotate_img():
    global c
    global myimg
    global mimg
    global imagename
    global image1
    global glb_img_name
    global width,height
    global countrotate
    global fwidth,fheight
    copy=Image.open(glb_img_name)
    owidth,oheight=copy.size
    if countrotate==0:
        b1=copy.rotate(90,expand = 1)
    elif countrotate==1:
        b1=copy.rotate(180,expand = 1)
    elif countrotate==2:
        b1=copy.rotate(270,expand = 1)
    elif countrotate==3:
        b1=copy
    owidth,oheight=b1.size
    fwidth,fheight=width_height(owidth,oheight)
    countrotate+=1
    if countrotate==4:
        countrotate=0
    b1=b1.resize((fwidth,fheight),Image.ANTIALIAS)
    mimg=b1
    image1=b1
    but1=ImageTk.PhotoImage(b1)
    myimg=but1
    c.config(width=fwidth,height=fheight)
    c.create_image(0,0,anchor=NW,image=myimg)
    c.grid(row=0,column=0)
toolbo[7]=Frame(root,relief=RIDGE,bd=3)
anti=ImageTk.PhotoImage(Image.open("iconfinder_rotate-ccw_2561285.png").resize((30,30),Image.ANTIALIAS))
bt=Button(toolbo[7],image=anti,command=rotate_img).grid(row=5,column=0,pady=10,padx=10)
bt=Button(toolbo[7],text="Save",command=save_rotate_img).grid(row=5,column=1,pady=10,padx=10)
#color_picker
def colorpic(e):
    global glb_img_name
    global c
    global color
    global myimg
    global mimg
    global imagename
    global image1
    global texton
    global fcolor,fcolor
    global glb_img_name
    global width,height
    b1=Image.open(glb_img_name).resize((width,height),Image.ANTIALIAS).convert("RGB")
    pixs=b1.getpixel((e.x,e.y))
    ds=_from_rgb((pixs))
    color=ds
    fcolor=ds
    mybutton=Button(toolbo[1],text="   ",command=chose,fg=color,bg=color).grid(row=1,column=1)
    mybutton=Button(toolbo[4],text="  ",command=chose2,bg=color,fg=color).grid(row=1,column=3,padx=5,pady=10)
    
#menus
mymenu=Menu(root)
root.config(menu=mymenu)
adds=Menu(mymenu,tearoff=0)
add_img=Menu(mymenu,tearoff=0)
add_filters=Menu(mymenu,tearoff=0)
add_paint=Menu(mymenu,tearoff=0)
add_text=Menu(mymenu,tearoff=0)
add_adjust=Menu(mymenu,tearoff=0)
add_crop=Menu(mymenu,tearoff=0)
add_rotate=Menu(mymenu,tearoff=0)
mymenu.add_cascade(label="File", menu=adds)
adds.add_command(label="Save",command=save1)
adds.add_command(label="Save as",command=save_as)
adds.add_command(label="Select another image",command=select_another_image)
adds.add_command(label="Reset",command=glbreset)
mymenu.add_cascade(label="Paint", menu=add_paint)
mymenu.add_cascade(label="Image on Image", menu=add_img)
mymenu.add_cascade(label="Text on Image", menu=add_text)
mymenu.add_cascade(label="Filters", menu=add_filters)
mymenu.add_cascade(label="Adjust", menu=add_adjust)
mymenu.add_cascade(label="Crop", menu=add_crop)
mymenu.add_cascade(label="Rotate", menu=add_rotate)
add_img.add_command(label="Image on Image",command=third_frame)
add_text.add_command(label="Text",command=fourth_frame)
add_paint.add_command(label="Paint",command=one_frame)
add_filters.add_command(label="Filters",command=second_frame)
add_adjust.add_command(label="Adjust",command=fifth_frame)
add_crop.add_command(label="crop",command=sixth_frame)
add_rotate.add_command(label="Rotate",command=seventh_frame)
def on_closing():
    global save_panniya_cha
    if save_panniya_cha==0:
        check=messagebox.askyesnocancel("Quit", "Do you want to save before exiting?")
        if check==True:
            save_as()
            root.destroy()
        elif check==False:
            root.destroy()
        else:
            pass
    else:
        check=messagebox.askyesno("Quit", "Do you want to exit?")
        if check==True:
            root.destroy()
        else:
            pass
ds=_from_rgb((dominant_color))
c.config(bg=ds)
c.bind("<Button-3>",colorpic)
root.config(bg=ds)      
root.protocol("WM_DELETE_WINDOW", on_closing)
root.mainloop()
