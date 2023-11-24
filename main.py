import tkinter as tk
import flashcard as fc
import flashcard_file_handler as ffh

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

def flashcard_addition_callback(new_flashcard_deck, text):
    global front
    global l
    print(front)
    if front:
        side = "Back"
        front = False
        new_flashcard_deck[-1].front = text
    else:
        side = "Front"
        front = True
        new_flashcard_deck[-1].back = text
        new_flashcard_deck.append(fc.flashcard("", ""))

    l.config(text=("Flashcard " + str(len(new_flashcard_deck)) + " " + side))

def flashcard_creation_callback(new_flashcard_deck):
    ffh.append_new_flashcard_deck(new_flashcard_deck)
    exit()

def create_flashcard_creation_menu(window):
    global front
    global l

    for widget in window.place_slaves():
        widget.destroy()

    front = True
    new_flashcard_deck = list()
    new_flashcard_deck.append(fc.flashcard("", ""))
    l = tk.Label(window, text="Flashcard 1 Front")
    l.place(relx=0.1, rely=0.0, relwidth=0.8, relheight=0.2)

    textbox = tk.Entry(window)
    textbox.place(relx=0.1, rely=0.2, relwidth=0.8, relheight=0.6)

    submit_button = tk.Button(window, text="Ok", command=lambda: flashcard_addition_callback(new_flashcard_deck, textbox.get()))
    submit_button.place(relx=0.3, rely=0.9, relheight=0.1, relwidth=0.2 )

    submit_button = tk.Button(window, text="Create Deck", command=lambda: flashcard_creation_callback(new_flashcard_deck))
    submit_button.place(relx=0.5, rely=0.9, relheight=0.1, relwidth=0.2 )

def flashcard_deletion_callback(flashcard_decks:list, deck_index):
    flashcard_decks.pop(deck_index)
    ffh.write_new_flashcard_decks(flashcard_decks)
    exit()

def create_flashcard_deletion_menu(window, flashcard_decks:list):
    for widget in window.place_slaves():
        widget.destroy()
    
    l = tk.Label(window, text="Select a deck")
    l.place(relx=0.1, rely=0.0, relwidth=0.8, relheight=0.2)

    selection_box = tk.Listbox(window, selectmode=tk.SINGLE)
    selection_box.place(relx=0.1, rely=0.2, relwidth=0.8, relheight=0.6)

    for i, deck in enumerate(flashcard_decks):
        selection_box.insert(i + 1, "Deck" + str(i + 1))

    submit_button = tk.Button(window, text="Delete Deck", command=lambda: flashcard_deletion_callback(flashcard_decks, (selection_box.curselection())[0]))
    submit_button.place(relx=0.3, rely=0.9, relheight=0.1, relwidth=0.4 )

def create_main_menu():
    window = tk.Tk()
    window.title("Study App")
    window.geometry("600x400")

    flashcards = ffh.parse_flashcard_file()

    create_button = tk.Button(window, text="Create Deck", command=lambda: create_flashcard_creation_menu(window))
    create_button.place(relx=0.1, rely=0.1, relwidth=0.2, relheight=0.6)

    delete_button = tk.Button(window, text="Delete Deck", command=lambda: create_flashcard_deletion_menu(window, flashcards))
    delete_button.place(relx=0.4, rely=0.1, relwidth=0.2, relheight=0.6)

    study_button = tk.Button(window, text="Study Deck", command=lambda: create_flashcard_selection_menu(window, flashcards))
    study_button.place(relx=0.7, rely=0.1, relwidth=0.2, relheight=0.6)

    window.mainloop()

create_main_menu()