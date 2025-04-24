import tkinter as tk
from PIL import Image, ImageTk
import requests
from io import BytesIO

# def cat_button():
#     img = Image.open("cat_1.jpg")
#     img_tk = ImageTk.PhotoImage(img)

#     image_label.config(image=img_tk)
#     image_label.image = img_tk


def clear():

    image_label.config(image=None)
    image_label.image = None


def get_cat_image():
    url = "https://api.thecatapi.com/v1/images/search"
    response = requests.get(url)
    res = response.json()
    cat_url = res[0]["url"]
    cat_response = requests.get(cat_url)
    cat_image = BytesIO(cat_response.content)
    img = Image.open(cat_image)
    # img = img.resize((800, 600))
    img.thumbnail((800, 600))
    img_tk = ImageTk.PhotoImage(img)

    image_label.config(image=img_tk)
    image_label.image = img_tk


root = tk.Tk()
root.title("Cat-viewer")
root.geometry("1000x800")

button = tk.Button(root, text="猫ちゃんを表示するボタン", command=get_cat_image)
button.pack(pady=50)

button2 = tk.Button(root, text="clear", command=clear)
button2.pack()

image_label = tk.Label(root)
image_label.pack()

root.mainloop()
