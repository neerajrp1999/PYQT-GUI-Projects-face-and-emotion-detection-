from tkinter import *
from PIL import ImageTk,Image

root = Tk()
root.title("Face Detection in Machine Learning")
frame = LabelFrame(root, text="Detection Techniques..!", padx=100,pady=100,borderwidth=10)
frame.pack(fill=BOTH,padx=100,pady=100)

# img=ImageTk.PhotoImage(Image.open("face1.jpg"))
# frame=Frame(image=img)
# frame.pack()

def face1():
    import show1
    myLabel = Label(root, text="Detected single face image!", font=("Arial", 16, "bold"))
    myLabel.pack()

def face2():
    import show2

def face3():
    import show3

def face4():
    import show4

b1=Button(frame, text="Single Image", fg="Red",command=face1,padx=50,pady=100,borderwidth=3)
b1.grid(row=0, column=0) 
b2=Button(frame, text="Multiple Image", fg="Green",command=face2,padx=50,pady=100,borderwidth=3)
b2.grid(row=0, column=1)
b3=Button(frame, text="Video Clip", fg="Yellow",command=face3,padx=50,pady=100,borderwidth=3)
b3.grid(row=0, column=2)
b4=Button(frame, text="Webcam Detection", fg="Blue",command=face4,padx=50,pady=100,borderwidth=3)
b4.grid(row=0, column=3)


button_quit=Button(root, text="Exit Program", command=root.quit)
button_quit.pack()

root.mainloop()


