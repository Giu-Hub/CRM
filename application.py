from flask import Flask, render_template, request
from markupsafe import escape
from queries import insert_account, get_accounts
import requests
import json

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/accounts")
def view_accounts():
    accounts = get_accounts()

    return render_template("accounts.html", accounts=accounts)

# @app.route("/view_account/<string:vat_code>")
# def view_account_by_vat_code(vat_code):
#     account_retrieved = {
#         "name": "Paolo Coppola",
#         "vat_code": vat_code
#     }
    
#     return render_template("view_account_by_vat_code.html", account=account_retrieved)

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

@app.route("/contacts")
def view_contacts():
    return render_template("contacts.html")

@app.route("/create_contact/<string:vat_code>")
def create_contact(vat_code):
    return render_template("create_contact.html", vat_code=vat_code)

@app.route("/contacts/<string:vat_code>")
def view_contacts_by_vat_code(vat_code):
    # Query Get Contact

    # Leva escape
    # Aggiungi render_template
    # Vedi contacts.html e contacts.css
    
    return escape(vat_code)

if __name__ == "__main__":
    app.run(debug = True)