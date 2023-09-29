import BehemothBrawl
from tkinter import *
from Variables import *

root = Tk()
root.title("Behemoth Brawl")
Screen_Width = root.winfo_screenwidth()
Screen_Height = root.winfo_screenheight()
root.state('zoomed')
Pvp = 0


def StartPvp():
    root.withdraw()
    BehemothBrawl.main()
    exit()


root.configure(width=Screen_Width, height=Screen_Height, background="#E0B0FF")

title = Label(root, text="Behemoth Brawl", font=("Helvetica", 40), bg="#E0B0FF")

pvc = Button(root, text="Player vs Computer", width=20, fg="white", bg="black", command=lambda: StartPvp())

ExitApp = Button(root, text="Exit Game", width=20, fg="white", bg="black", command=exit)

Instructions = Label(root, text=InstructionText, font=("Helvetica", 20), bg="#E0B0FF")

title.pack(pady=40)
pvc.pack(pady=10)
ExitApp.pack(pady=10)
Instructions.pack(pady=80)

root.mainloop()
