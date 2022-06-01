#import modules
from PIL import Image,ImageTk,ImageFilter
from tkinter import Label, Tk,Button, Toplevel,filedialog,Frame

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
  img = img.resize(resize_photo_aspect_ratio(width,height),Image.Resampling.LANCZOS)
  imgphoto = ImageTk.PhotoImage(img)

  e1 = Label(img_frame,image=imgphoto)
  e1.grid(row=2,column=0)
  e1.image = imgphoto

  filter_frame.pack()
  upload_frame.pack_forget()
  img_frame.pack()


l1= Label(upload_frame,text="Upload a JPG file or PNG file")
l1.grid(row=0,column=0)

Button(upload_frame,text="Upload File",width=20, command=upload_file).grid(row=1,column=0)


def filter_photo(filter_type = None):
  global current_image
  if filter_type == 1:
    current_image=  img.filter(ImageFilter.CONTOUR)
  elif filter_type == 2:
    current_image=img.filter(ImageFilter.BLUR)
  elif filter_type == 3:
    current_image=img.filter(ImageFilter.EDGE_ENHANCE)
  else:
    current_image=img
  #Create a photo image to be displayed in the GUI
  photo = ImageTk.PhotoImage(current_image)
  e1.configure(image=photo)
  e1.image=photo


def reset_photo():
  original_image=ImageTk.PhotoImage(img)
  e1.configure(image=original_image)
  e1.image=original_image

def save_photo():
  file_url = filedialog.asksaveasfilename(filetypes = FILE_TYPES, defaultextension = FILE_TYPES)
  current_image.save(file_url)
  # #Success window
  top = Toplevel()
  top.geometry("200x200")
  Label(top,text="The file has been saved..Yaaay!!!").pack()


Button(img_frame,text="Reset Photo",width=20,command=lambda: filter_photo(filter_type=0)).grid(row=1,column=0)
Button(img_frame,text="Save Photo",width=20,command=save_photo).grid(row=0,column=0)

Button(filter_frame,text="Cartoon",width=20,command=lambda: filter_photo(filter_type=1)).grid(row=0,column=1)
Button(filter_frame,text="Blur",width=20,command=lambda: filter_photo(filter_type=2)).grid(row=0,column=2)
Button(filter_frame,text="Enhance Edge",width=20,command=lambda: filter_photo(filter_type=3)).grid(row=0,column=3)



upload_frame.pack()

root.mainloop()
