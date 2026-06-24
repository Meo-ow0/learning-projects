Contact Book
I build this contact book application which allow users to list people and search them through names or phone numbers. 
This saved in Json file so data will not disappear when you close tab.

Features
Add Contacts: Save name, phone, email, and address.

Search: Quickly filter your contact list by name or number.

Persistent Storage: Everything is saved to contacts.json automatically.

interface for a clean, friendly look.

Setup
You'll need Flask installed to run this.

Organize your folders:

app.py (The main logic)

/static/style.css

How it works
This app uses a simple request-response cycle. When you submit the "Add" form, the server processes that data and writes it to a file. When you search, it filters that same file in real-time.

Built With
Python/Flask: The backbone of the server logic.

JSON: Used as a lightweight database to store your contacts permanently.

HTML/CSS: For the user interface 