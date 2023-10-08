const registerForm = document.getElementById('registerForm');

if (registerForm) {
    registerForm.addEventListener('submit', function(event) {
        event.preventDefault();

        const first_name_elem = document.getElementById('first_name');
        const last_name_elem = document.getElementById('last_name');
        const email_elem = document.getElementById('email');
        const birthday_elem = document.getElementById('birthday');
        const password_elem = document.getElementById('password');
        const confirm_pw_elem = document.getElementById('confirm_pw');
        const current_date = new Date();
        let isValid = true;
        
        const errorContainer = document.getElementById('registerErrors');
        while (errorContainer.firstChild) {
            errorContainer.removeChild(errorContainer.firstChild);
        }

        errorContainer.classList.remove('alert');
        errorContainer.classList.remove('alert-danger');

        const errors = {}

        if (first_name_elem !== null && first_name_elem !== undefined) {
            const first_name = first_name_elem.value;
            if (first_name.length < 2) {
                errors['first_name'] = 'First name should be at least 2 characters.';
            }
        }
        else {
            errors['first_name'] = 'First name should be at least 2 characters.';
        }

        if (last_name_elem !== null && last_name_elem !== undefined) {
            const last_name = last_name_elem.value;
            if (last_name.length < 2) {
                errors['last_name'] = 'Last name should be at least 2 characters.';
            }
        }
        else {
            errors['last_name'] = 'Last name should be at least 2 characters.';
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

        if (birthday_elem !== null && birthday_elem !== undefined) {
            const birthday = new Date(birthday_elem.value);
            if (!birthday || birthday > current_date) {
                errors['birthday'] = 'Please enter a valid birthday.';
            }
        }
        else {
            errors['birthday'] = 'Please enter a valid birthday.';
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
                    window.location.href = 'http://127.0.0.1:8000/wall';
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
                    window.location.href = 'http://127.0.0.1:8000/wall'
                }
            })
            .catch(error => {
                console.error('Error: ', error)
            });
            return false;
        };
    });
};


const messageForm = document.getElementById('messageForm')

if (messageForm) {
    messageForm.addEventListener('submit', function(event) {
        event.preventDefault();

        const message_elem = document.getElementById('message');
        let isValid = true;
        
        const errorContainer = document.getElementById('messageErrors')
        if (errorContainer.firstChild != null) {
            while (errorContainer.firstChild) {
                errorContainer.removeChild(errorContainer.firstChild)
            }
        }
        
        errorContainer.classList.remove('alert')
        errorContainer.classList.remove('alert-danger')

        const errors = {}

        if (message_elem !== null && message_elem !== undefined) {
            const message = message_elem.value;
            if (message.length < 15) {
                errors['message'] = 'Message should be at least 15 characters.';
            }
        }
        else {
            errors['message'] = 'Message should be at least 15 characters.';
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

            fetch('http://127.0.0.1:8000/post_message', {
                method: 'POST', 
                body: formData
            })
            .then(response => response.json())
            .then(data => {
                if (!data.success) {
                    if (data.error_messages) {
                        const newMessage = document.createElement('p')
                        newMessage.innerText = data.error_messages['message']
                        errorContainer.appendChild(newMessage)
                        errorContainer.classList.add('alert')
                        errorContainer.classList.add('alert-danger')
                    }
                }
                else {
                    window.location.href = 'http://127.0.0.1:8000/wall'
                }
            })
            .catch(error => {
                console.error('Error: ', error)
            });
            return false;
        }
    });
};


const messageAndComments = document.querySelectorAll('.post_and_comments');

messageAndComments.forEach(function(message) {
    const commentForm = message.querySelector('.commentForm');

    commentForm.addEventListener('submit', function(event) {
        event.preventDefault();
        
        const messageId = message.querySelector('.messageId').innerText;
        const commentsContainer = message.querySelector('.commentsContainer');
    
        const options = {
            month: 'short',
            day: 'numeric',
            year: 'numeric', 
            hour: '2-digit', 
            minute: '2-digit'
        }

        const currentForm = this;
        const commentText = currentForm.querySelector('.comment');
        const formData = new FormData(currentForm);
    
        fetch(`http://127.0.0.1:8000/comment/${messageId}`, {
            method: 'POST', 
            body: formData
        })
        .then(response => response.json())
        .then(data => {
            const created_at_date = new Date(data.created_at); 
            const created_at = created_at_date.toLocaleString('en-us', options)
                .replace(/PM/, 'p.m.')
                .replace(/AM/, 'a.m.');

            commentsContainer.innerHTML += `<div class="one_comment">
            <div class="commentId hidden">${data.id}}</div>
            <div class="comment_content">
            <h6>${data.first_name} ${data.last_name} - ${created_at}</h6>
            <p>${data.comment}</p>
            </div>
            <div class="delete_comment">
            <button class="deleteCommentButton">delete</button>
            </div>
            </div>`;
            commentText.value = '';
        })
        .catch(error => {
            console.error('Error: ', error);
        });
    });
});


messageAndComments.forEach(function(message) { 
    const deleteButton = message.querySelector('.deleteButton');

    if (deleteButton) {
        deleteButton.addEventListener('click', function(event) {
            event.preventDefault();
            
            const messageId = message.querySelector('.messageId').innerText;
            const errorContainer = message.querySelector('.deleteError');

            if (errorContainer.firstChild != null) {
                errorContainer.removeChild(errorContainer.firstChild);
            }
            
            errorContainer.classList.remove('alert');
            errorContainer.classList.remove('alert-danger');
        
            fetch(`http://127.0.0.1:8000/destroy/${messageId}`)
            .then(response => response.json())
            .then(data => {
                if (!data.success) {
                    if (data.error_messages) {
                        const newMessage = document.createElement('p');
                        newMessage.innerText = data.error_messages['delete'];
                        errorContainer.appendChild(newMessage);
                        errorContainer.classList.add('alert');
                        errorContainer.classList.add('alert-danger');
                    }
                }
                else {
                    message.innerHTML = '';
                }
            })
            .catch(error => {
                console.error('Error: ', error);
            });
            return false;
        });
    };
});

messageAndComments.forEach(function(message) { 

    const comments = message.querySelectorAll('.one_comment')

    comments.forEach(function(comment) {
        const deleteButton = comment.querySelector('.deleteCommentButton');

        if (deleteButton) {
            deleteButton.addEventListener('click', function(event) {
                event.preventDefault();
                
                const commentId = comment.querySelector('.commentId').innerText;
            
                fetch(`http://127.0.0.1:8000/destroy_comment/${commentId}`)
                .then(response => response.json())
                .then(data => {
                    if (data.success) {
                        comment.innerHTML = '';
                    }
                })
                .catch(error => {
                    console.error('Error: ', error);
                });
                return false;
            });
        };
    })


});

