import json

class ContactManager:

    def __init__(self, file="data.json"):
        self.file = file
        self.contacts = []

    def load_contacts(self):
        try:
            with open(self.file, "r") as f:
                self.contacts = json.load(f)
        except (FileNotFoundError, json.JSONDecodeError):
            self.contacts = []
            print(f"File {self.file} does not exist or JSON data corrupt.")
        return self.contacts

    def add_contact(self, contact):
        self.contacts.append(contact)
        with open(self.file, "w") as f:
            json.dump(self.contacts, f, indent=4)

    def update_contact(self, contact_to_update):
        for i, contact in enumerate(self.contacts):
            if contact["id"] == contact_to_update["id"]:
                self.contacts[i] = contact_to_update
                with open(self.file, "w") as f:
                    json.dump(self.contacts, f, indent=4)
                return
        print(f"No contact found with ID {contact_to_update['id']}.")

    def delete_contact(self, id_to_delete):
        for i, contact in enumerate(self.contacts):
            if contact["id"] == id_to_delete:
                del self.contacts[i]
                with open(self.file, "w") as f:
                    json.dump(self.contacts, f, indent=4)
                return
        print(f"No contact found with ID {id_to_delete}.")