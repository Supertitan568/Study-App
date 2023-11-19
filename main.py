import tkinter as tk

class flashcard:
    def __init__(self, front, back):
        self.front = front
        self.back = back

front = True
flashcards = [flashcard("Who is my favorite girl in the world", "My girlfriend"), flashcard("What do I want to do", "Graduate"), flashcard("What is my favorite language", "The C Language")]
flashcard_index = 0

def keypress(event):
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

window = tk.Tk()
flashcard_text = flashcards[flashcard_index].front
textbox = tk.Label(text=flashcards[flashcard_index].front)
window.bind("<Key>", keypress)

textbox.pack()
window.mainloop()

