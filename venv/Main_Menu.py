from tkinter import *

win = Tk()
win.title("Behemoth Brawl")
Screen_Width = win.winfo_screenwidth()
Screen_Height = win.winfo_screenheight()

def output():
    print("This worked!")

win.configure(width = Screen_Width, height = Screen_Height, background = "#E0B0FF")

pvp = Button(text = "Player vs Player", fg = "white", bg = "black", command = output)


pvp.pack()

win.mainloop()
