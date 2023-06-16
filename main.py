import tkinter
from PIL import Image, ImageFont, ImageDraw

# Global Variables
ImagePath = "C:Users\Om Patel\OneDrive\Pictures\CourseImage-2x.jpg"
ImageFontt = ImageFont.truetype("arial.ttf", 15)

# Taking Image to be edited as Input.
image = Image.open(ImagePath)
d = ImageDraw.Draw(image)
d.text((1900,1000),"@OmPatel",font=ImageFontt,anchor="rs")


image.show()
