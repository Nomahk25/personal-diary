import os
from datetime import datetime
import getpass

PASSWORD = "diary123"

def authenticate():
    print("🔒 Personal Diary Login")
    attempts = 3
    while attempts > 0:
        entered = getpass.getpass("Enter password: ")
        if entered == PASSWORD:
            print("✅ Access granted.\n")
            return True
        else:
            attempts -= 1
            print(f"❌ Wrong password. {attempts} attempts left.\n")
    return False

def write_entry():
    date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    entry = input("Write your diary entry:\n> ")
    with open("diary.txt", "a") as file:
        file.write(f"\n[{date}]\n{entry}\n" + "-"*40 + "\n")
    print("📝 Entry saved.")

def view_entries():
    if os.path.exists("diary.txt"):
        print("\n📖 Your Diary Entries:\n")
        with open("diary.txt", "r") as file:
            print(file.read())
    else:
        print("No entries found yet.")

def menu():
    while True:
        print("\n📓 Personal Diary Menu")
        print("1. Write a new entry")
        print("2. View diary")
        print("3. Exit")

        choice = input("Choose an option (1/2/3): ")
        if choice == '1':
            write_entry()
        elif choice == '2':
            view_entries()
        elif choice == '3':
            print("👋 Exiting diary.")
            break
        else:
            print("Invalid option. Try again.")

if __name__ == "__main__":
    if authenticate():
        menu()
    else:
        print("🚫 Access denied.")
