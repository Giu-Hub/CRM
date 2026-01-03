document.addEventListener("DOMContentLoaded", () => {
    const form = document.getElementById("contact-container");

    form.addEventListener("submit", (event) => {
        event.preventDefault();

        firstName = document.getElementById("first-name").value;
        lastName = document.getElementById("last-name").value;
        taxCode = document.getElementById("tax-code").value;
        email = document.getElementById("email").value;
        phone = document.getElementById("phone").value;
        vatCode=document.getElementById("vat-code").value;

        // https://flask.palletsprojects.com/en/stable/patterns/javascript/
        
        const url = "/api/create_contact";
        let data = new FormData();

        data.append("firstName", firstName);
        data.append("lastName", lastName);
        data.append("taxCode", taxCode);
        data.append("email", email);
        data.append("phone", phone);
        data.append("vatCode",vatCode);
        
        fetch(url, {
            method: "POST",
            body: data
        })
        .then(res => res.text())
        .then(body => {
            if (body === '201') {
                alert("Contact created successfully");
            }
            else {
                alert("Error during create contact");
            }
        })
    })
})