from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Sample data structure to store contacts
contacts = [
    {
        'id': 1,
        'name': 'Ranjith GS',
        'phone': '7204962837',
        'email': 'ranjithgs.edu.1437@gmail.com',
        'address': 'Chintamani,Chikkaballapura(Dist)-563125,Karnataka'
    },
    {
        'id': 2,
        'name': 'Bhargavi GS',
        'phone': '9874565123',
        'email': 'bhargavigs.edu.1437@gmail.com',
        'address': 'Chintamani,Chikkaballapura(Dist)-563125,Karnataka'
    }
]

def get_contact_by_id(contact_id):
    return next((contact for contact in contacts if contact['id'] == contact_id), None)

@app.route('/')
def index():
    return render_template('index.html', contacts=contacts)

@app.route('/add_contact', methods=['GET', 'POST'])
def add_contact():
    if request.method == 'POST':
        new_contact = {
            'id': len(contacts) + 1,
            'name': request.form['name'],
            'phone': request.form['phone'],
            'email': request.form['email'],
            'address': request.form['address']
        }
        contacts.append(new_contact)
        return redirect(url_for('index'))
    return render_template('add_contact.html')

@app.route('/search', methods=['POST'])
def search():
    search_term = request.form['search_term'].lower()
    search_results = [contact for contact in contacts
                      if search_term in contact['name'].lower() or search_term in contact['phone']]
    return render_template('index.html', contacts=search_results, search_term=search_term)

@app.route('/update_contact/<int:contact_id>', methods=['GET', 'POST'])
def update_contact(contact_id):
    contact = get_contact_by_id(contact_id)
    if request.method == 'POST':
        contact['name'] = request.form['name']
        contact['phone'] = request.form['phone']
        contact['email'] = request.form['email']
        contact['address'] = request.form['address']
        return redirect(url_for('index'))
    return render_template('update_contact.html', contact=contact)

@app.route('/delete_contact/<int:contact_id>')
def delete_contact(contact_id):
    contact = get_contact_by_id(contact_id)
    if contact:
        contacts.remove(contact)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
