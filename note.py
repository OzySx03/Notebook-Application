def menu():
    print("Notebook Application")
    print("1. List Notes")
    print("2. Add Note")
    print("3. Edit Note")
    print("4. Delete Note")
    print("5. Exit")

def list_notes():
    try:
        with open("notes.txt", "r") as file:
            notes = file.readlines()
        if notes:
            print("Notes:")
            for i, note in enumerate(notes, start=1):
                print(f"{i}. {note.strip()}")
        else:
            print("No notes have been added yet.")
    except FileNotFoundError:
        print("No notes have been added yet.")

def add_note():
    note = input("Enter the note you want to add: ")
    with open("notes.txt", "a") as file:
        file.write(note + "\n")
    print("Note successfully added.")

def edit_note():
    list_notes()
    try:
        note_index = int(input("Enter the number of the note you want to edit: ")) - 1
        with open("notes.txt", "r") as file:
            notes = file.readlines()
        if 0 <= note_index < len(notes):
            new_note = input("Enter the new note: ")
            notes[note_index] = new_note + "\n"
            with open("notes.txt", "w") as file:
                file.writelines(notes)
            print("Note successfully edited.")
        else:
            print("Invalid note number.")
    except ValueError:
        print("Invalid input. Please enter a number.")

def delete_note():
    list_notes()
    try:
        note_index = int(input("Enter the number of the note you want to delete: ")) - 1
        with open("notes.txt", "r") as file:
            notes = file.readlines()
        if 0 <= note_index < len(notes):
            deleted_note = notes.pop(note_index)
            with open("notes.txt", "w") as file:
                file.writelines(notes)
            print(f"'{deleted_note.strip()}' successfully deleted.")
        else:
            print("Invalid note number.")
    except ValueError:
        print("Invalid input. Please enter a number.")

while True:
    menu()
    choice = input("Make your choice (1/2/3/4/5): ")

    if choice == "1":
        list_notes()
    elif choice == "2":
        add_note()
    elif choice == "3":
        edit_note()
    elif choice == "4":
        delete_note()
    elif choice == "5":
        print("Notebook application is closing. Have a good day!")
        break
    else:
        print("Invalid option. Please try again.")
