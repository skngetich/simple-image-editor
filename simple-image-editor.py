#import modules
from PIL import Image,ImageTk,ImageFilter
from tkinter import Label, Tk,Button,filedialog,Frame

#Constants
FILE_TYPES =[("JPG image",'*.jpg'),("PNG image","*.png")]
WINDOW_MIN_WIDTH = 400
WINDOW_MIN_HEIGHT = 400

root = Tk()
root.minsize(width=WINDOW_MIN_WIDTH, height=WINDOW_MIN_HEIGHT)
root.geometry("500x600")
root.title("Simple Image Editor")

#Frames
filter_frame = Frame(root,padx=10,pady=10,width=WINDOW_MIN_WIDTH,height=100,bd=3)
img_frame = Frame(root,padx=10,pady=10,width=WINDOW_MIN_WIDTH,height=400,bd=3)
upload_frame = Frame(root,padx=10,pady=10,width=WINDOW_MIN_WIDTH,height=100,bd=3)


# Return tuple of the resize image based on the image aspect ration
def resize_photo_aspect_ratio(width,height,MAX_WIDTH=500,MAX_HEIGHT=500):
  resize_ratio= min(MAX_WIDTH/width, MAX_HEIGHT/height)
  return (round(width*resize_ratio),round(height*resize_ratio))

def upload_file():
  global img,e1
  # User selects image from the file dialog
  filename = filedialog.askopenfilename(filetypes=FILE_TYPES)

  img = Image.open(filename)
  width,height = img.size
  img = img.resize(resize_photo_aspect_ratio(width,height),Image.ANTIALIAS)
  imgphoto = ImageTk.PhotoImage(img)

  e1 = Label(img_frame,image=imgphoto)
  e1.grid(row=1,column=0)
  e1.image = imgphoto

  filter_frame.pack()
  upload_frame.pack_forget()
  img_frame.pack()


l1= Label(upload_frame,text="Upload a JPG file or PNG file")
l1.grid(row=0,column=0)

Button(upload_frame,text="Upload File",width=20, command=upload_file).grid(row=1,column=0)

def grayscale_photo():
  imgfilter=ImageTk.PhotoImage( img.filter(ImageFilter.CONTOUR))
  e1.configure(image=imgfilter)
  e1.image=imgfilter

def blur_photo():
  imgfilter=ImageTk.PhotoImage( img.filter(ImageFilter.BLUR))
  e1.configure(image=imgfilter)
  e1.image=imgfilter

def enhance_edge_photo():
  imgfilter=ImageTk.PhotoImage( img.filter(ImageFilter.EDGE_ENHANCE))
  e1.configure(image=imgfilter)
  e1.image=imgfilter

def reset_photo():
  original_image=ImageTk.PhotoImage(img)
  e1.configure(image=original_image)
  e1.image=original_image


Button(img_frame,text="Reset",width=20,command=reset_photo).grid(row=0,column=0)
Button(filter_frame,text="Cartoon",width=20,command=grayscale_photo).grid(row=0,column=1)
Button(filter_frame,text="Blur",width=20,command=blur_photo).grid(row=0,column=2)
Button(filter_frame,text="Enhance Edge",width=20,command=enhance_edge_photo).grid(row=0,column=3)




upload_frame.pack()

root.mainloop()
