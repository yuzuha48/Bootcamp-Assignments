const registerForm = document.getElementById('registerForm');

if (registerForm) {
    registerForm.addEventListener('submit', function(event) {
        event.preventDefault();

        const name_elem = document.getElementById('name');
        const alias_elem = document.getElementById('alias');
        const email_elem = document.getElementById('email');
        const password_elem = document.getElementById('password');
        const confirm_pw_elem = document.getElementById('confirm_pw');
        let isValid = true;
        
        const errorContainer = document.getElementById('registerErrors');
        while (errorContainer.firstChild) {
            errorContainer.removeChild(errorContainer.firstChild);
        }

        errorContainer.classList.remove('alert');
        errorContainer.classList.remove('alert-danger');

        const errors = {}

        if (name_elem !== null && name_elem !== undefined) {
            const name = name_elem.value;
            if (name.length < 2) {
                errors['name'] = 'Name should be at least 2 characters.';
            }
        }
        else {
            errors['name'] = 'Name should be at least 2 characters.';
        }

        if (alias_elem !== null && alias_elem !== undefined) {
            const alias = alias_elem.value;
            if (alias.length < 2) {
                errors['alias'] = 'Alias should be at least 2 characters.';
            }
        }
        else {
            errors['alias'] = 'Alias should be at least 2 characters.';
        }

        if (email_elem !== null && email_elem !== undefined) {
            const email = email_elem.value;
            if (!email || !email.match(/^[a-zA-Z0-9._-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,4}$/)) {
                errors['email'] = 'Invalid email address.';
            }
        }
        else {
            errors['email'] = 'Invalid email address.';
        }

        if (password_elem !== null && password_elem !== undefined) {
            var password = password_elem.value;
            if (password.length < 8) {
                errors['password'] = 'Password should be at least 8 characters.'
            }
        }
        else {
            errors['password'] = 'Password should be at least 8 characters.'
        }

        if (confirm_pw_elem !== null && confirm_pw_elem !== undefined) {
            const confirm_pw = confirm_pw_elem.value;
            if (password != confirm_pw) {
                errors['confirm_pw'] = 'Passwords do not match.';
            }
        }
        else {
            errors['confirm_pw'] = 'Passwords do not match.';
        }

        if (Object.keys(errors).length > 0) {
            isValid = false;
            for (let key in errors) {
                const newMessage = document.createElement('p');
                newMessage.innerText = errors[key];
                errorContainer.appendChild(newMessage);
            }
            errorContainer.classList.add('alert');
            errorContainer.classList.add('alert-danger');
        }

        if (isValid) {
            const formData = new FormData(this);
    
            fetch('http://127.0.0.1:8000/register', {
                method: 'POST', 
                body: formData
            })
            .then(response => response.json())
            .then(data => {
                if (!data.success) {
                    if (data.error_messages) {
                        for (let key in data.error_messages) {
                            const newMessage = document.createElement('p');
                            newMessage.innerText = data.error_messages[key];
                            errorContainer.appendChild(newMessage);
                        }
                        errorContainer.classList.add('alert');
                        errorContainer.classList.add('alert-danger');
                    }
                }
                else {
                    window.location.href = 'http://127.0.0.1:8000/books';
                }
            })
            .catch(error => {
                console.error('Error: ', error);
            });
            return false;
        };
    });
};


const loginForm = document.getElementById('loginForm')

if (loginForm) {
    loginForm.addEventListener('submit', function(event) {
        event.preventDefault();

        const email_elem = document.getElementById('login_email');
        const password_elem = document.getElementById('login_password');
        let isValid = true;
        
        const errorContainer = document.getElementById('loginErrors')
        while (errorContainer.firstChild) {
            errorContainer.removeChild(errorContainer.firstChild)
        }

        errorContainer.classList.remove('alert')
        errorContainer.classList.remove('alert-danger')

        const errors = {}

        if (email_elem !== null && email_elem !== undefined) {
            const email = email_elem.value;
            if (!email || !email.match(/^[a-zA-Z0-9._-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,4}$/)) {
                errors['email'] = 'Invalid email address.';
            }
        }
        else {
            errors['email'] = 'Invalid email address.';
        }

        if (password_elem !== null && password_elem !== undefined) {
            const password = password_elem.value;
            if (password.length < 1) {
                errors['password'] = 'Please enter your password.'
            }
        }
        else {
            errors['password'] = 'Please enter your password.'
        }

        if (Object.keys(errors).length > 0) {
            isValid = false;
            for (let key in errors) {
                const newMessage = document.createElement('p');
                newMessage.innerText = errors[key];
                errorContainer.appendChild(newMessage);
            }
            errorContainer.classList.add('alert');
            errorContainer.classList.add('alert-danger');
        }

        if (isValid) {
            const formData = new FormData(this)

            fetch('http://127.0.0.1:8000/login', {
                method: 'POST', 
                body: formData
            })
            .then(response => response.json())
            .then(data => {
                if (!data.success) {
                    if (data.error_messages) {
                        for (let key in data.error_messages) {
                            const newMessage = document.createElement('p')
                            newMessage.innerText = data.error_messages[key]
                            errorContainer.appendChild(newMessage)
                        }
                        errorContainer.classList.add('alert')
                        errorContainer.classList.add('alert-danger')
                    }
                }
                else {
                    window.location.href = 'http://127.0.0.1:8000/books'
                }
            })
            .catch(error => {
                console.error('Error: ', error)
            });
            return false;
        };
    });
};




