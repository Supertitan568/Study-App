from flashcard import flashcard

def parse_flashcard_file():
    flashcard_file = open(r"saved_decks.txt", 'r')
    flashcard_decks = list()
    for line in flashcard_file:
        line = line.rstrip()
        if line == "new deck":
            flashcard_decks.append(list())
            continue

        parsed_line = line.split(',')
        new_flashcard = flashcard(parsed_line[0], parsed_line[1])
        flashcard_decks[-1].append(new_flashcard)

    flashcard_file.close()

    return flashcard_decks

def append_new_flashcard_deck(new_flashcard_deck):
    flashcard_file = open(r"saved_decks.txt", 'a')
    flashcard_file.write("new deck\n")

    for card in new_flashcard_deck:
        line = card.front + ',' + card.back + '\n'
        flashcard_file.write(line)

    flashcard_file.close()
