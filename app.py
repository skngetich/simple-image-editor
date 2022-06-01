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
root.resizable(width=0, height=0)
root.title("Simple Image Editor")

filter_frame = Frame(root,bg="black",padx=10,pady=10,width=WINDOW_MIN_WIDTH,height=100,bd=4)
img_frame = Frame(root,bg="green",padx=10,pady=10,width=WINDOW_MIN_WIDTH,height=400,bd=4)
upload_frame = Frame(root,bg="yellow",padx=10,pady=10,width=WINDOW_MIN_WIDTH,height=100,bd=4)




# l1= Label(upload_frame,text="Upload a JPG file or PNG file")
# l1.grid(row=1,column=1)
# uploadBtn = Button(upload_frame,text="Upload File",width=20).grid(row=2,column=1)



Button(upload_frame,text="Cartoon",width=20).grid(row=0,column=0)
Button(img_frame,text="Blur",width=20).grid(row=0,column=0)
Button(img_frame,text="Blur",width=20).grid(row=0,column=1)
Button(img_frame,text="Blur",width=20).grid(row=0,column=2)
Button(upload_frame,text="Enhance Edge",width=20).grid(row=0,column=0)


filter_frame.pack()
img_frame.pack()
upload_frame.pack()



root.mainloop()
