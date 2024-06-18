import tkinter as tk
from PIL import Image, ImageDraw


class MainGui:
    def __init__(self, root):
        self.root = root
        self.root.title("Jacob's Digit Classifier")
        self.canvas_size = 280
        self.image_size = 28

        self.canvas = tk.Canvas(root, width=self.canvas_size, height=self.canvas_size, bg="white")

        self.image = Image.new("L", (self.canvas_size, self.canvas_size), 255)
        self.draw = ImageDraw.Draw(self.image)

        # Bind mouse events to the Canvas
        self.canvas.bind("<B1-Motion>", self.paint)


        # Lets make a classify button to export the drawing and pass it into the CNN
        self.classify_button = tk.Button(root, text="Classify", command=self.classify_image)
        self.classify_button.pack()

    def paint(self, event):
        x1, y1 = (event.x-1), (event.y-1)
        x2, y2 = (event.x+1), (event.y+1)
        self.canvas.create_oval(x1, y1, x2, y2, fill="black", width=5)
        self.draw.ellipse([x1, y1, x2, y2], fill="black")

    def classify_image(self):
        # convert

