import tkinter as tk
front = True

class flashcard:
    def __init__(self, front, back):
        self.front = front
        self.back = back

def keypress(event):
    if(front):
        textbox.config(text=first_flashcard.back)
    else:
        exit()
first_flashcard = flashcard("Who is my favorite girl in the world", "My girlfriend")
window = tk.Tk()
textbox = tk.Label(text=first_flashcard.front)
window.bind("<Key>", keypress)

textbox.pack()
window.mainloop()

