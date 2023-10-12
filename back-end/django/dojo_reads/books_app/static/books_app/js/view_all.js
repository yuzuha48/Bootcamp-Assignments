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
                    location.href = 'http://127.0.0.1:8000/books'
                }
            })
            .catch(error => {
                console.error('Error: ', error);
            });
        });
    };
});