const yesDelete = document.getElementById('yesDelete')
const noDelete = document.getElementById('noDelete')
const courseId = document.querySelector('#course_id').innerText

if (yesDelete) {
    yesDelete.addEventListener('click', function (e){
        e.preventDefault(); 

        fetch(`http://127.0.0.1:8000/courses/destroy/${courseId}`)
        .then(response => response.json())
        .then(data => {
            if (data.success) {
                window.location.href = 'http://127.0.0.1:8000/courses'
            }
        })
        .catch(error => {
            console.error('Error: ', error)
        });
        return false;
    });
};

if (noDelete) {
    noDelete.addEventListener('click', function (e) {
        e.preventDefault();
        window.location.href = 'http://127.0.0.1:8000/courses'
    });
};