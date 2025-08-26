from tkinter import *
from PIL import Image, ImageTk
import requests
from io import BytesIO

def load_image():
    try:
        response = requests.get(url)
        response.raise_for_status()
        image_data = BytesIO(response.content)
        img = Image.open(image_data)
        return ImageTk.PhotoImage(img)
    except Exception as error:
        print(f"Ошибка {error}")
        return None





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

