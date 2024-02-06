import keyboard
import time
import tkinter as tk
from tkinter import *
from tkinter import filedialog
from PIL import ImageGrab, Image, ImageTk
global img

def obliczwymiary(img):
    x = img.width
    y = img.height
    
    while x>480 and y>480:
        x=x//2
        y=y//2
        print(x)
        print(y)
        print("-")
    return int(x), int(y)

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
            
            window = tk.Tk()
            window.attributes('-topmost', True)
            window.title("Save?")
            btnsave = tk.Button(window, text="Save | Zapisz", command=lambda: save(img,window,tk))
            btnsave.grid(row=0, column=0)
            time.sleep(0.2)
            img = ImageGrab.grabclipboard()
            szerokosc, wysokosc = obliczwymiary(img)
            
            canvas = Canvas(
                window,
                width = szerokosc, 
                height = wysokosc+50
                )   

            canvas.grid(row=1, column=0)
            
            imgg = ImageTk.PhotoImage(img.resize((szerokosc,wysokosc),Image.Resampling.LANCZOS))
            canvas.create_image(0,0,anchor=NW,image=imgg) 
            
            window.mainloop()
    except Exception as e:
        print("Core error: "+str(e))