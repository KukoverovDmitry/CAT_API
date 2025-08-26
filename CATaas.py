from tkinter import *
from PIL import Image, ImageTk
import requests
from io import BytesIO

def load_image(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        image_data = BytesIO(response.content)
        img = Image.open(image_data)
        return ImageTk.PhotoImage(img)
    except Exception as error:
        print(f"Ошибка {error}")
        return None

def set_image(url):
    img = load_image(url)

    if img:
        label.configure(image=img)
        label.image = img


window = Tk()
window.title("Cataas")
window.geometry("600x480")


label = Label()
label.pack()
update_button = Button(text="Обновить", command= set_image)
update_button.pack()


url = "https://cataas.com/cat"
img = load_image(url)

if img:
    label.configure(image=img)
    label.image = img

set_image (url)

window.mainloop()

