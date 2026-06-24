import json
import os

class ContactBook:
    def __init__(self, filename="contacts.json"):
        self.filename = filename
        self.contacts = self.load_contacts()

    def load_contacts(self):
        if os.path.exists(self.filename):
            with open(self.filename, 'r') as file:
                return json.load(file)
        return []

    def save_contacts(self):
        with open(self.filename, 'w') as file:
            json.dump(self.contacts, file, indent=4)

    def add_contact(self, name, phone, email, address):
        self.contacts.append({
            "name": name,
            "phone": phone,
            "email": email,
            "address": address
        })
        self.save_contacts()
        print(f"Contact '{name}' saved!")

    # ... (other methods like search and delete would also call self.save_contacts())