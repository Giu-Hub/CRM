document.addEventListener("DOMContentLoaded", () => {
    // https://stackoverflow.com/questions/7410063/how-can-i-listen-to-the-form-submit-event-in-javascript

    const form = document.getElementById("vat-code-form");

    form.addEventListener("submit", () => {
        const url = "http://localhost:5000/api/create_account"

        // https://flask.palletsprojects.com/en/stable/patterns/javascript/
        let data = new FormData()

        data.append("vatCode", "1515151")
        
        fetch(url)
        .then(res => res.json())
    })
})