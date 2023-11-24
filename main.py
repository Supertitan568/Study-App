import tkinter as tk
import flashcard as fc

def get_created_flashcards():
    flashcards = list()
    flashcards.append([fc.flashcard("Who is my favorite girl in the world", "My girlfriend"), fc.flashcard("What do I want to do", "Graduate"), fc.flashcard("What is my favorite language", "The C Language")])
    flashcards.append([fc.flashcard("What am I going to do today", "sleep"), fc.flashcard("What should I do today", "Code"), fc.flashcard("What do I want to drink", "coffee")])
    flashcards.append([fc.flashcard("Who is my favorite cat", "soot"), fc.flashcard("What should I buy", "A cat tree"), fc.flashcard("What does my cat need", "cat nip")])

    return flashcards

def create_flashcard_selection_menu(window, flashcard_decks):
    for widget in window.place_slaves():
        widget.destroy()
    
    l = tk.Label(window, text="Select a deck")
    l.place(relx=0.1, rely=0.0, relwidth=0.8, relheight=0.2)

    selection_box = tk.Listbox(window, selectmode=tk.SINGLE)
    selection_box.place(relx=0.1, rely=0.2, relwidth=0.8, relheight=0.6)

    for i, deck in enumerate(flashcard_decks):
        selection_box.insert(i + 1, "Deck" + str(i + 1))

    submit_button = tk.Button(window, text="Study Deck", command=lambda: fc.main(window, flashcard_decks[(selection_box.curselection())[0]]))
    submit_button.place(relx=0.3, rely=0.9, relheight=0.1, relwidth=0.4 )

    

def create_main_menu():
    window = tk.Tk()
    window.title("Study App")
    window.geometry("600x400")

    flashcards = get_created_flashcards()

    create_button = tk.Button(window, text="Create Deck")
    create_button.place(relx=0.1, rely=0.1, relwidth=0.2, relheight=0.6)

    delete_button = tk.Button(window, text="Delete Deck")
    delete_button.place(relx=0.4, rely=0.1, relwidth=0.2, relheight=0.6)

    study_button = tk.Button(window, text="Study Deck", command=lambda: create_flashcard_selection_menu(window, flashcards))
    study_button.place(relx=0.7, rely=0.1, relwidth=0.2, relheight=0.6)

    window.mainloop()

create_main_menu()