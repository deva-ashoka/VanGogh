import Tkinter, Tkconstants, tkFileDialog
from Tkinter import *
from PIL import ImageTk, Image
from color2 import colorFrame

root = Tk()
prompt = StringVar()
root.title("VANGOGH")
label = Label(root, fg="dark green")
label.pack()

frame = Frame(root,background='white')
frame.pack()

# Function definition

# first create the canvas
canvas = Canvas(height=500,width=500,)
canvas.pack()

def chooseImage():
	global filepath
	filepath = tkFileDialog.askopenfilename()
	print(filepath)
	Image1()
	global coloredFilePath
	coloredFilePath = colorFrame(filepath)

def Image1():																																																																																																																																																																																																																																																																																																																																																																																																																																																																																		
    canvas.delete("all")
    i = Image.open(filepath)
    basewidth = 500
    wpercent = (basewidth/float(i.size[0]))
    hsize = int((float(i.size[1])*float(wpercent)))
    i = i.resize((basewidth, hsize), Image.ANTIALIAS)
    image1 = ImageTk.PhotoImage(i)
    canvas.create_image(0,0,anchor='nw',image=image1)
    canvas.image = image1

def Image2():
    canvas.delete("all")
    i = Image.open(coloredFilePath)
    basewidth = 500
    wpercent = (basewidth/float(i.size[0]))
    hsize = int((float(i.size[1])*float(wpercent)))
    i = i.resize((basewidth, hsize), Image.ANTIALIAS)
    image1 = ImageTk.PhotoImage(i)

    canvas.create_image(0,0,anchor='nw',image=image1)
    canvas.image = image1


conversationbutton = Button(frame, text='SHOW COLOR',width=25,fg="green",command = Image2)
conversationbutton.pack(side = RIGHT)

stopbutton = Button(frame, text='SHOW B/W',width=25,fg="black",command = Image1)
stopbutton.pack(side = RIGHT)

colorbutton = Button(frame, text='BROWSE',width=25,fg="black",command = chooseImage)
colorbutton.pack(side = RIGHT)

i = Image.open("VanGogh.jpg") 
image1 = ImageTk.PhotoImage(i)


canvas.create_image(0,0,anchor='nw',image=image1)
canvas.image = image1

root.mainloop()
