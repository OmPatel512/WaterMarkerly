from tkinter import *
from PIL import Image, ImageFont, ImageDraw

# Global Variables
ImagePath = "C:Users\Om Patel\OneDrive\Pictures\CourseImage-2x.jpg"
ImageFontt = ImageFont.truetype("arial.ttf", 15)

# Taking Image to be edited as Input.
image = Image.open(ImagePath)
d = ImageDraw.Draw(image)
d.text((1900,1000),"@OmPatel",font=ImageFontt,anchor="rs")


# image.show()

# GUI
window = Tk()
window.title("WaterMarkerly")
window.minsize(500, 400)

file_path_label = Label(text="Image Path: ", font=("Arial",12, "bold"))
file_path_label.grid(row=0, column=0)

file_path_textbox = Entry()
file_path_textbox.grid(row=0, column=1)

cpyrght_text_label = Label(text="Copyright Text: ", font=("Arial",12, "bold"))
cpyrght_text_label.grid(row=2, column=0)

cpyrght_textbox = Entry()
cpyrght_textbox.grid(row=2, column=1)

window.mainloop()