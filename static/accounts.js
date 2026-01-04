document.addEventListener("DOMContentLoaded", () => {
    // document.getElementById("back-arrow").addEventListener("click", () => {
    //     history.back()
    // })

    const accountsToDelete = document.getElementsByClassName("delete-account");

    // https://stackoverflow.com/questions/3871547/iterating-over-result-of-getelementsbyclassname-using-array-foreach
    
    Array.prototype.forEach.call(accountsToDelete, (account) => {
        account.addEventListener('click', () => {
            // https://stackoverflow.com/questions/61851069/accessing-data-attributes-with-javascript
            
            let vatCode = account.dataset.vat;
            
            const url = "/api/delete_account/" + vatCode;
            
            fetch(url, {
                method: "DELETE",
            })
            .then(res => res.text())
            .then(body => {
                if (body === '204') {
                    location.reload();
                }
                else {
                    alert("Error during delete account");
                }
            })
        })
    });
})