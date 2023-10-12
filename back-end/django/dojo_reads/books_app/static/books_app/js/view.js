const createForm = document.getElementById('createForm');

if (createForm) {
    createForm.addEventListener('submit', function(event) {
        event.preventDefault();

        const review_elem = document.getElementById('review');
        const rating_elem = document.getElementById('rating');

        let isValid = true;
        
        const errorContainer = document.getElementById('createErrors');
        if (errorContainer.firstChild != null) {
            while (errorContainer.firstChild) {
                errorContainer.removeChild(errorContainer.firstChild);
            }
        }
        
        errorContainer.classList.remove('alert');
        errorContainer.classList.remove('alert-danger');

        const errors = {};

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
            const formData = new FormData(this);

            fetch('http://127.0.0.1:8000/books/create_review', {
                method: 'POST', 
                body: formData
            })
            .then(response => response.json())
            .then(data => {
                if (!data.success) {
                    if (data.error_messages) {
                        const newMessage = document.createElement('p');
                        newMessage.innerText = data.error_messages['message'];
                        errorContainer.appendChild(newMessage);
                        errorContainer.classList.add('alert');
                        errorContainer.classList.add('alert-danger');
                    }
                }
                else {
                    location.href = `http://127.0.0.1:8000/books/${data.book_id}`
                }
            })
            .catch(error => {
                console.error('Error: ', error);
            });
            return false;
        }
    });
};


const allReviews = document.querySelectorAll('.one_review');

allReviews.forEach(function(review) {
    const deleteReview = review.querySelector('.deleteReview'); 

    if (deleteReview) {
        deleteReview.addEventListener('click', function(event) {
            event.preventDefault();

            const reviewId = review.querySelector('.reviewId').innerText;

            fetch(`http://127.0.0.1:8000/books/delete/${reviewId}`)
            .then(response => response.json())
            .then(data => {
                if (data.success) {
                    review.remove();
                }
            })
            .catch(error => {
                console.error('Error: ', error);
            });
        });
    };
});