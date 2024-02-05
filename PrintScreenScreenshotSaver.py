import keyboard
import time
import tkinter as tk
from tkinter import *
from tkinter import filedialog
from PIL import ImageGrab, Image, ImageTk
global img

def save(img, window, tk):
    #print(img)
    sciezka = filedialog.asksaveasfilename(filetypes=[("PNG","*.png")], defaultextension = "*.png")
    try:
        img.save(sciezka)
        tk.messagebox.showinfo('Done!','Saved image to '+sciezka)
    except:
        tk.messagebox.showerror('Error!','Failed to save image')
    window.destroy()

while True:
    try:
        przycisk = str(keyboard.read_key())
        if przycisk == "print screen":
            time.sleep(0.2)
            img = ImageGrab.grabclipboard()
            window = tk.Tk()
            window.attributes('-topmost', True)
            window.title("Save?")
            btnsave = tk.Button(window, text="Save | Zapisz", command=lambda: save(img,window,tk))
            btnsave.grid(row=0, column=0)
            canvas = Canvas(
                window,
                width = 500, 
                height = 500
                )   

            canvas.grid(row=1, column=0)
            imgg = ImageTk.PhotoImage(ImageGrab.grabclipboard().resize((500,500),Image.Resampling.LANCZOS))
   
            canvas.create_image(0,0,anchor=NW,image=imgg) 
        
            window.mainloop()
    except:
        print("Core error")
