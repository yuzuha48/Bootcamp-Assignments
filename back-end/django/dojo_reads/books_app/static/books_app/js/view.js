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
                    let rating = data.rating;
                    if (rating == 1) {
                        rating = 'one_star';
                    }
                    if (rating == 2) {
                        rating = 'two_stars';
                    }
                    if (rating == 3){
                        rating = 'three_stars';
                    }
                    if (rating == 4){
                        rating = 'four_stars';
                    }
                    if (rating == 5) {
                        rating = 'five_stars';
                    }

                    const reviewsContainer = document.getElementById('reviews');
                    const contentToAdd = `<div class='one_review'>
                    <div class='rating'>
                    <p>Rating:</p>
                    <img src="/static/books_app/images/${rating}.png" alt="${rating}">
                    </div>
                    <div class='review'>
                    <p>${data.user} says: ${data.review}</p>
                    </div>
                    <div class='details'>
                    <p>Posted on ${data.created_at}</p>
                    <a href="/books/delete/${data.book_id}">Delete this review</a>
                    </div>
                    </div>`;

                    reviewsContainer.insertAdjacentHTML('afterbegin', contentToAdd);

                    review_elem.value = "";
                    rating_elem.value = "";
                }
            })
            .catch(error => {
                console.error('Error: ', error);
            });
            return false;
        }
    });
};