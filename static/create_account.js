document.addEventListener("DOMContentLoaded", () => {
    // https://stackoverflow.com/questions/7410063/how-can-i-listen-to-the-form-submit-event-in-javascript

    const form = document.getElementById("vat-code-form");

    form.addEventListener("submit", (event) => {
        event.preventDefault();

        vatCode = document.getElementById("vat_code").value;

        const url = "/api/create_account";

        // https://flask.palletsprojects.com/en/stable/patterns/javascript/
        let data = new FormData();

        data.append("vatCode", vatCode);
        
        fetch(url, {
            method: "POST",
            body: data
        })
        .then(res => res.text())
        .then(body => {
            if (body === '201') {
                alert("Account created successfully");
            }
            else {
                alert("Error during create account");
            }
        })
    })
})