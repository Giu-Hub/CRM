document.addEventListener("DOMContentLoaded", () => {
    const vatCode = document.getElementById("vat_code");

    vatCode.addEventListener("keypress", (event) => {
        if (event.key == "Enter") {
            fetch()
        }
    })
})