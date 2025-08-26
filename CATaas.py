from tkinter import *
from PIL import Image, ImageTk
import requests
from io import BytesIO



window = Tk()
window.title("Cataas")
window.geometry("600x480")


label = Label()
label.pack()


url = "http://cataas.com/cat   "
img = load_image(url)

if img:
    label.configure(image=img)
    label.image = img


window.mainloop()

