from tkinter import *
from tkinter  import filedialog
from rembg import remove
import cv2

scr = Tk()
scr.geometry("300x200")
scr.resizable(0,0)
scr.title("RemoverBackGround")

def choose_photo():
    global file
    file = filedialog.askopenfilename()

def remove_bg():
     input_path = str(file)
     output_path = "removed.jpg"

     input = cv2.imread(input_path)
     output = remove(input)

     cv2.imwrite(output_path, output)
     cv2.imshow(output_path, output)

lb1 = Label(scr, text="please choose picture", font="100", fg="black").pack(side=TOP)
bt1 = Button(scr, text="choose picture", font="60", bg="blue", fg="white", command=choose_photo).pack()

bt2 = Button(scr, text="Remove BackGround", font="70", bg="white", fg="blue",command=remove_bg).place(x=50,y=110)


scr.mainloop()