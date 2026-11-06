"""Contact Book using Dictionary
Features: add, search, update, delete, list contacts.
Topics: dict, list, tuple, set, JSON/CSV files, exception handling.
"""
import csv
import json

DATA_FILE = "contacts.json"
CSV_FILE = "contacts.csv"
FIELDS = ("name", "phone", "email")  # tuple: fixed field order


def load_contacts():
    """Load contacts dict from JSON file; return empty dict if none."""
    try:
        with open(DATA_FILE, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return {}
    except json.JSONDecodeError:
        print("Warning: contacts file is corrupted. Starting fresh.")
        return {}


def save_contacts(contacts):
    with open(DATA_FILE, "w") as f:
        json.dump(contacts, f, indent=4)


def export_csv(contacts):
    with open(CSV_FILE, "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=FIELDS)
        writer.writeheader()
        for name, info in contacts.items():
            writer.writerow({"name": name, **info})
    print(f"Exported {len(contacts)} contacts to {CSV_FILE}")


def add_contact(contacts):
    name = input("Name: ").strip()
    if not name:
        print("Name cannot be empty.")
        return
    if name.lower() in {n.lower() for n in contacts}:  # set for duplicate check
        print("Contact already exists. Use update instead.")
        return
    phone = input("Phone: ").strip()
    if not phone.isdigit():
        raise ValueError("Phone must contain digits only.")
    email = input("Email: ").strip()
    contacts[name] = {"phone": phone, "email": email}
    print(f"Added {name}.")


def find_name(contacts, query):
    """Case-insensitive exact match; returns the stored name or None."""
    for name in contacts:
        if name.lower() == query.lower():
            return name
    return None


def search_contact(contacts):
    query = input("Search (name or part of name): ").strip().lower()
    matches = [n for n in contacts if query in n.lower()]  # list
    if not matches:
        print("No contacts found.")
        return
    for n in matches:
        print(f"  {n} | {contacts[n]['phone']} | {contacts[n]['email']}")


def update_contact(contacts):
    name = find_name(contacts, input("Name to update: ").strip())
    if name is None:
        print("Contact not found.")
        return
    phone = input(f"New phone [{contacts[name]['phone']}]: ").strip()
    email = input(f"New email [{contacts[name]['email']}]: ").strip()
    if phone:
        if not phone.isdigit():
            raise ValueError("Phone must contain digits only.")
        contacts[name]["phone"] = phone
    if email:
        contacts[name]["email"] = email
    print(f"Updated {name}.")


def delete_contact(contacts):
    name = find_name(contacts, input("Name to delete: ").strip())
    if name is None:
        print("Contact not found.")
        return
    del contacts[name]
    print(f"Deleted {name}.")


def list_contacts(contacts):
    if not contacts:
        print("Contact book is empty.")
        return
    for name in sorted(contacts):
        print(f"  {name} | {contacts[name]['phone']} | {contacts[name]['email']}")


def main():
    contacts = load_contacts()
    menu = {
        "1": ("Add contact", add_contact),
        "2": ("Search contact", search_contact),
        "3": ("Update contact", update_contact),
        "4": ("Delete contact", delete_contact),
        "5": ("List all contacts", list_contacts),
    }
    while True:
        print("\n--- Contact Book ---")
        for key, (label, _) in menu.items():
            print(f"{key}. {label}")
        print("6. Export to CSV\n7. Save & Exit")
        choice = input("Choose: ").strip()
        try:
            if choice in menu:
                menu[choice][1](contacts)
            elif choice == "6":
                export_csv(contacts)
            elif choice == "7":
                save_contacts(contacts)
                print("Saved. Goodbye!")
                break
            else:
                print("Invalid choice.")
        except ValueError as e:
            print(f"Input error: {e}")
        except OSError as e:
            print(f"File error: {e}")


if __name__ == "__main__":
    main()
