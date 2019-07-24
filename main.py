import os
import base64

from flask import Flask, render_template, request, redirect, url_for, session
from model import Donation, Donor


app = Flask(__name__)
app.secret_key = b'SECRET_KEY=KjJPe35tQKY2YLRzm7vhm3aJdqqh8YHR'




@app.route('/')
def home():
    return redirect(url_for('all'))

@app.route('/donations/')
def all():
    donations = Donation.select()
    return render_template('donations.jinja2', donations=donations)

@app.route('/donate', methods=['POST', 'GET'])
def donate():
    "add donation to database"
    donors = Donor.select()

    if request.method == 'POST':
        donor = request.form['donor']
        donation = int(request.form['donation'])
        donor_donation_input = Donor.select().where(Donor.name == donor).get()
        Donation(donor=donor_donation_input, value=donation).save()
        return redirect(url_for('all'))
    return render_template('donate.jinja2', donors=donors)


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 6738))
    app.run(host='0.0.0.0', port=port)

