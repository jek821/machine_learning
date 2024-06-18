import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageDraw
import tensorflow as tf
import numpy as np


class MainGui:
    def __init__(self, root):
        self.model = tf.keras.models.load_model('best.keras')
        self.root = root
        self.root.title("Jacob's Digit Classifier")
        self.canvas_size = 200  # Larger canvas size
        self.image_size = 28  # Image size for classification

        self.canvas = tk.Canvas(root, width=self.canvas_size, height=self.canvas_size, bg="white")
        self.canvas.pack()

        self.image = Image.new("L", (self.canvas_size, self.canvas_size), 255)
        self.draw = ImageDraw.Draw(self.image)

        # Bind mouse events to the Canvas
        self.canvas.bind("<B1-Motion>", self.paint)

        # Classify button
        self.classify_button = tk.Button(root, text="Classify", command=self.classify_image)
        self.classify_button.pack()

        # Clear button
        self.clear_button = tk.Button(root, text="Clear", command=self.clear_canvas)
        self.clear_button.pack()

    def paint(self, event):
        x1, y1 = (event.x - 5), (event.y - 5)
        x2, y2 = (event.x + 5), (event.y + 5)
        self.canvas.create_oval(x1, y1, x2, y2, fill="black", width=10)
        self.draw.ellipse([x1, y1, x2, y2], fill="black")

    def preprocess_image(self, image):
        img = image.resize((self.image_size, self.image_size))
        img_arr = tf.keras.preprocessing.image.img_to_array(img)
        img_arr = img_arr.astype("float32")
        img_arr = 255 - img_arr
        img_arr = img_arr / 255
        img_arr = img_arr.reshape(1, self.image_size, self.image_size, 1)
        return img_arr

    def classify_image(self):
        # Convert the drawn image to grayscale
        img = self.image.convert('L')
        # Preprocess the drawn image
        img_arr = self.preprocess_image(img)

        # Classify the image
        prediction = self.model.predict(img_arr)
        predicted_class = np.argmax(prediction)

        # Display the result
        tk.messagebox.showinfo("Classification Result", f"The predicted digit is: {predicted_class}")

    def clear_canvas(self):
        self.canvas.delete("all")
        self.image = Image.new("L", (self.canvas_size, self.canvas_size), 255)
        self.draw = ImageDraw.Draw(self.image)


if __name__ == "__main__":
    root = tk.Tk()
    app = MainGui(root)
    root.mainloop()