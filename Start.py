import argparse
import json
import datetime

def add_note(title = "null", message = "null"):
    if title == "null":
        title = input("Введите заголовок заметки: ")
    if message == "null":
        message = input("Введите текст заметки: ")
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    note = {"id": len(notes) + 1, "title": title, "message": message, "timestamp": timestamp}
    notes.append(note)
    save_notes()

def read_notes():
    date_filter = input("Введите дату для фильтрации (YYYY-MM-DD): ")
    filtered_notes = [note for note in notes if note["timestamp"].startswith(date_filter)]
    if len(filtered_notes) == 0:
        print("Заметок не найдено")
    else:
        for note in filtered_notes:
            print(f"{note['id']}. {note['title']} ({note['timestamp']})\n{note['message']}\n")
def list_notes():
    for note in notes:
        print(f"{note['id']}. {note['title']} ({note['timestamp']})\n{note['message']}\n")
def edit_note():
    note_id = int(input("Введите ID заметки для редактирования: "))
    note = next((note for note in notes if note["id"] == note_id), None)
    if note is None:
        print("Заметка не найдена")
    else:
        title = input(f"Введите новый заголовок заметки (было: {note['title']}): ")
        message = input(f"Введите новый текст заметки (было: {note['message']}): ")
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        note["title"] = title
        note["message"] = message
        note["timestamp"] = timestamp
        save_notes()

def delete_note():
    note_id = int(input("Введите ID заметки для удаления: "))
    note = next((note for note in notes if note["id"] == note_id), None)
    if note is None:
        print("Заметка не найдена")
    else:
        notes.remove(note)
        save_notes()

def save_notes():
    with open("notes.json", "w") as f:
        json.dump(notes, f)

def load_notes():
    try:
        with open("notes.json", "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return []

def main():
    parser = argparse.ArgumentParser(description="Консольное приложение заметки")
    parser.add_argument("command", choices=["add", "read", "edit", "delete", "list"], help="Команда для выполнения")
    parser.add_argument("--title", help="Заголовок заметки")
    parser.add_argument("--message", help="Текст заметки")
    args = parser.parse_args()

    global notes
    notes = load_notes()

    if args.command == "add":
        add_note(args.title, args.message)
    elif args.command == "read":
        read_notes()
    elif args.command == "list":
        list_notes()
    elif args.command == "edit":
        edit_note()
    elif args.command == "delete":
        delete_note()

if __name__ == "__main__":
    main()