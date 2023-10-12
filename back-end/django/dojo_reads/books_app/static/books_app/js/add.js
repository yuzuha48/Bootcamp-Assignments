const createForm = document.getElementById('createForm')

if (createForm) {
    createForm.addEventListener('submit', function(event) {
        event.preventDefault();

        const title_elem = document.getElementById('title')
        const author_elem = document.getElementById('author')
        const review_elem = document.getElementById('review')
        const rating_elem = document.getElementById('rating')

        let isValid = true;
        
        const errorContainer = document.getElementById('createErrors')
        if (errorContainer.firstChild != null) {
            while (errorContainer.firstChild) {
                errorContainer.removeChild(errorContainer.firstChild)
            }
        }
        
        errorContainer.classList.remove('alert')
        errorContainer.classList.remove('alert-danger')

        const errors = {}

        if (title_elem !== null && title_elem !== undefined) {
            const title = title_elem.value;
            if (title.length < 2) {
                errors['title'] = 'Title should be at least 2 characters.';
            }
        }
        else {
            errors['title'] = 'Title should be at least 2 characters.';
        }

        if (author_elem !== null && author_elem !== undefined) {
            const author = author_elem.value;
            if (author.length < 2) {
                errors['author'] = "Author's name should be at least 2 characters.";
            }
        }
        else {
            errors['author'] = "Author's name should be at least 2 characters.";
        }

        if (review_elem !== null && review_elem !== undefined) {
            const review = review_elem.value;
            if (review.length < 15) {
                errors['review'] = "Review should be at least 15 characters.";
            }
        }
        else {
            errors['review'] = "Review should be at least 15 characters.";
        }

        if (rating_elem !== null && rating_elem !== undefined) {
            const rating = rating_elem.value;
            if (!rating) {
                errors['rating'] = "Please select a rating.";
            }
        }
        else {
            errors['rating'] = "Please select a rating.";
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

            fetch('http://127.0.0.1:8000/books/create', {
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
                    window.location.href = `http://127.0.0.1:8000/books/${data.book_id}`
                }
            })
            .catch(error => {
                console.error('Error: ', error)
            });
            return false;
        }
    });
};