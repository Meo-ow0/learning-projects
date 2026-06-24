from flask import Flask, render_template, render_template_string, request, redirect
import json
import os

app = Flask(__name__)
DATA_FILE = 'contacts.json'

def read_data():
    if not os.path.exists(DATA_FILE): return []
    with open(DATA_FILE, 'r') as f: return json.load(f)

def write_data(data):
    with open(DATA_FILE, 'w') as f: json.dump(data, f, indent=4)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        new_contact = {
            "name": request.form.get('name'),
            "phone": request.form.get('phone'),
            "email": request.form.get('email'),
            "address": request.form.get('address')
        }
        contacts = read_data()
        contacts.append(new_contact)
        write_data(contacts)
        return redirect('/')

    contacts = read_data()
    query = request.args.get('q', '').lower()
    if query:
        contacts = [c for c in contacts if query in c['name'].lower() or query in c['phone']]
    
    # We use render_template_string to keep it in one file for now
    return render_template_string(INDEX_HTML, contacts=contacts)

INDEX_HTML = """
<!DOCTYPE html>
<html>
<head>
    <link rel="stylesheet" href="{{ url_for('static', filename='style.css') }}">
</head>
<body>
    <div class="container">
        <h1>My Contacts</h1>
        <form method="POST">
            <input type="text" name="name" placeholder="Name" required>
            <input type="text" name="phone" placeholder="Phone" required>
            <input type="email" name="email" placeholder="Email">
            <input type="text" name="address" placeholder="Address">
            <button type="submit">Add Contact</button>
        </form>

        <form action="/" method="GET" style="margin-top:20px;">
            <input type="text" name="q" placeholder="Search by name...">
            <button type="submit">Search</button>
        </form>

        <table>
            <tr><th>Name</th><th>Phone</th><th>Email</th></tr>
            {% for contact in contacts %}
            <tr>
                <td>{{ contact.name }}</td>
                <td>{{ contact.phone }}</td>
                <td>{{ contact.email }}</td>
            </tr>
            {% endfor %}
        </table>
    </div>
</body>
</html>
"""

if __name__ == '__main__':
    app.run(debug=True)