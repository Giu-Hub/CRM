from flask import Flask, render_template, request
from markupsafe import escape
from queries import insert_account, insert_contact, get_accounts, get_contacts, view_contact_by_vatcode, delete_account, get_contact, get_account_details, get_count_accounts, get_count_contacts
import requests
import json

app = Flask(__name__)

@app.route("/")
def index():
    counter_accounts = get_count_accounts()
    counter_contacts = get_count_contacts()

    counters = {
        "contacts": counter_contacts,
        "accounts": counter_accounts,
    }

    return render_template("index.html", counters=counters)

@app.route("/accounts")
def view_accounts():
    accounts = get_accounts()

    return render_template("accounts.html", accounts=accounts)

@app.route("/view_account/<string:vat_code>")
def view_account_by_vat_code(vat_code):
    account = get_account_details(vat_code)

    return render_template("view_account_by_vat_code.html", account=account)

@app.route("/api/create_contact", methods=["POST"])
def handle_creating_contact():
    firstName = request.form["firstName"]
    lastName = request.form["lastName"]
    taxCode = request.form["taxCode"]
    email = request.form["email"]
    phone = request.form["phone"]
    vatCode = request.form["vatCode"]

    fields = {
        "firstName": firstName,
        "lastName": lastName,
        "taxCode": taxCode,
        "email": email,
        "phone": phone,
        "vatCode": vatCode,
    }
    statusCode = insert_contact(fields)

    return statusCode

@app.route("/create_account")
def create_account():
    return render_template("create_account.html")

@app.route("/api/create_account", methods=["POST"])
def handle_creating_account():
    vatCode = request.form["vatCode"]

    # https://stackoverflow.com/questions/20199126/reading-json-from-a-file
    with open("credentials.json") as file:
        credentials = json.load(file)

    url = f"https://test.company.openapi.com/IT-start/{vatCode}"

    headers = {
        "Authorization": f"Bearer {credentials['token']}",
        "Accept": "application/json"
    }
    response = requests.get(
        url = url,
        headers = headers
    )

    response_json = response.json()

    data = response_json.get("data")[0]

    fields = dict()

    fields["vatCode"] = data.get("vatCode")
    fields["companyName"] = data.get("companyName")
    fields["streetName"] = data.get("address").get("registeredOffice").get("streetName")
    fields["region"] = data.get("address").get("registeredOffice").get("region").get("description")

    statusCode = insert_account(fields)

    return statusCode

@app.route("/api/delete_account/<string:vat_code>", methods=["DELETE"])
def handle_deleting_account(vat_code):
    statusCode = delete_account(vat_code)

    return '204'

@app.route("/contacts")
def view_contacts():
    contacts = get_contacts()

    return render_template("contacts.html", contacts=contacts)

@app.route("/view_details_contact/<string:tax_code>")
def view_details_contact(tax_code):
    contact = get_contact(tax_code)
    print(contact)

    return render_template("view_details_contact.html", contact=contact)

@app.route("/create_contact/<string:vat_code>")
def create_contact(vat_code):
    return render_template("create_contact.html", vat_code=vat_code)

@app.route("/contacts/<string:vat_code>")
def view_contacts_by_vat_code(vat_code):
    contacts = view_contact_by_vatcode(vat_code)
    
    return render_template("contacts.html", contacts=contacts)

if __name__ == "__main__":
    app.run(debug = True)