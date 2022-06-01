#import modules
from turtle import width
from PIL import Image,ImageTk
from tkinter import Label, Tk,Button,filedialog

#Constants
FILE_TYPES =[("JPG image",'*.jpg'),("PNG image","*.png")]
WINDOW_MIN_WIDTH = 300
WINDOW_MIN_HEIGHT = 300

root = Tk()

root.minsize(width=WINDOW_MIN_WIDTH, height=WINDOW_MIN_HEIGHT)
root.geometry("500x500")
root.title("The Main Window")


# Return tuple of the resize image based on the image aspect ration
def resize_photo_aspect_ratio(width,height,MAX_WIDTH=500,MAX_HEIGHT=500):
  resize_ratio= min(MAX_WIDTH/width, MAX_HEIGHT/height)
  return (round(width*resize_ratio),round(height*resize_ratio))

def upload_file():
  # User selects image from the file dialog
  filename = filedialog.askopenfilename(filetypes=FILE_TYPES)

  img = Image.open(filename)
  width,height = img.size
  img = img.resize(resize_photo_aspect_ratio(width,height),Image.ANTIALIAS)
  img = ImageTk.PhotoImage(img)

  e1 = Label(root,image=img,width=400,height=300)
  e1.grid(row=3,column=1)
  e1.image = img

l1= Label(root,text="Upload a JPG file or PNG file")
l1.grid(row=1,column=1)
uploadBtn = Button(root,text="Upload File",width=20, command=upload_file).grid(row=2,column=1)







root.mainloop()
