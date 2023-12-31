import tkinter as tk

class flashcard:
    def __init__(self, front, back):
        self.front = front
        self.back = back

def next_button_callback():
    global flashcard_index
    global front
    global flashcards

    if(front):
        textbox.config(text=flashcards[flashcard_index].back)
        front= False
    else:
        flashcard_index += 1
        if flashcard_index >= len(flashcards):
            exit()
        textbox.config(text=flashcards[flashcard_index].front)
        front = True

def prev_button_callback():
    global flashcard_index
    global front
    global flashcards

    if not front:
        textbox.config(text=flashcards[flashcard_index].front)
        front= True
    else:
        flashcard_index -= 1
        if flashcard_index >= len(flashcards):
            exit()
        textbox.config(text=flashcards[flashcard_index].back)
        front = False

def main(window, flashcard_deck):
    global front
    global flashcards
    global flashcard_index
    global textbox
    
    flashcards = flashcard_deck

    for widget in window.place_slaves():
        widget.destroy()
    
    front = True
    flashcard_index = 0

    next_button = tk.Button(window, text = "Next", command=next_button_callback)
    next_button.place(relx = 1, x =-2, y = 2, anchor = tk.NE)
 
    prev_button = tk.Button(window, text = "Previous", command=prev_button_callback)
    prev_button.place(anchor = tk.NW)
 
    textbox = tk.Label(text=flashcards[flashcard_index].front)
    textbox.place(relx = 0.5, rely = 0.5, anchor = tk.CENTER)
