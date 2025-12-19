document.addEventListener("DOMContentLoaded", () => {
    const vatCode = document.getElementById("vat_code");

    vatCode.addEventListener("keypress", (event) => {
        if (event.key == "Enter") {
            fetch("https://webhook.site/9e4cb56f-46c0-4ede-8b78-03f45150a2d8")
        }
    })
})