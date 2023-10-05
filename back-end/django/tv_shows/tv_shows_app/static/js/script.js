const createForm = document.getElementById('createForm'); 
if (createForm) {
    createForm.addEventListener('submit', function (event) {
        event.preventDefault();

        const errorContainer = document.getElementById('errors')
        while (errorContainer.firstChild) {
            errorContainer.removeChild(errorContainer.firstChild)
        }

        errorContainer.classList.remove('alert')
        errorContainer.classList.remove('alert-danger')

        const formData = new FormData(this)
    
        fetch(`http://127.0.0.1:8000/shows/create`, {
            method: 'POST', 
            body: formData,
        })
        .then(response => response.json())
        .then(data => {
            if (!data.success) {
                if (data.error_message) {
                    for (var key in data.error_message) {
                        var newMessage = document.createElement('p')
                        newMessage.innerText = data.error_message[key]
                        errorContainer.appendChild(newMessage)
                    }
                    errorContainer.classList.add('alert')
                    errorContainer.classList.add('alert-danger')
                }
            }
            else {
                window.location.href = `http://127.0.0.1:8000/shows/${data.show_id}`
            }
        })
        .catch(error => {
            console.error('Error: ', error)
        });
        return false;
    });
};

const updateForm = document.getElementById('updateForm'); 
const showIdElement = document.querySelector('#show_id');
if (updateForm) {
    updateForm.addEventListener('submit', function (event) {
        event.preventDefault();

        const errorContainer = document.getElementById('errors')
        while (errorContainer.firstChild) {
            errorContainer.removeChild(errorContainer.firstChild)
        }

        errorContainer.classList.remove('alert')
        errorContainer.classList.remove('alert-danger')

        const showID = showIdElement.innerText; 
        const formData = new FormData(this)
    
        fetch(`http://127.0.0.1:8000/shows/${showID}/update`, {
            method: 'POST', 
            body: formData,
        })
        .then(response => response.json())
        .then(data => {
            if (!data.success) {
                if (data.error_message) {
                    for (var key in data.error_message) {
                        var newMessage = document.createElement('p')
                        newMessage.innerText = data.error_message[key]
                        errorContainer.appendChild(newMessage)
                    }
                    errorContainer.classList.add('alert')
                    errorContainer.classList.add('alert-danger')
                }
            }
            else {
                window.location.href = `http://127.0.0.1:8000/shows/${showID}`
            }
        })
        .catch(error => {
            console.error('Error: ', error)
        });
        return false;
    });
};
