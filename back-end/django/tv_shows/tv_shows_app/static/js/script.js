document.getElementById('createUserForm').addEventListener('submit', function (e) {
    e.preventDefault();
    const errorMessageElemnet = document.getElementById('errorMessage');
    errorMessageElemnet.innerText = '';
    const formData = new FormData(this)

    fetch('/create', {
        method: 'POST', 
        body: formData,
    })
    .then(response => response.json())
    .then(data => {
        if (data.error_message) {
            errorMessageElemnet.innerText = data.error_message
        }
    })
    .catch(error => {
        console.error('Error: ', error)
    });
});

document.getElementById('updateUserForm').addEventListener('submit', function (e) {
    e.preventDefault();
    const errorMessageElemnet = document.getElementById('errorMessage');
    errorMessageElemnet.innerText = '';
    const showIdElement = document.querySelector('#show_id');
    const showID = showIdElement.value; 
    const formData = new FormData(this)
    console.log(errorMessageElemnet)

    fetch(`/shows/${showID}/update`, {
        method: 'POST', 
        body: formData,
    })
    .then(response => response.json())
    .then(data => {
        if (data.error_message) {
            errorMessageElemnet.innerText = data.error_message
        }
    })
    .catch(error => {
        console.error('Error: ', error)
    });
});