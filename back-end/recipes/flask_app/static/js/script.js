// function validateForm() {
//     let error = document.querySelector('.alert1');
//     error.textContent = " "

//     let first_name = document.getElementById("first_name").value;
//     let last_name = document.getElementById("last_name").value;
//     let email = document.getElementById("email").value;
//     let password = document.getElementById("password").value;
//     let confirmPassword = document.getElementById("confirm_password").value;

//     let isValid = true;
//     var emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;

//     if (first_name.length < 2 || last_name.length < 2 || email.length < 2) {
//         let error = document.querySelector('.alert1');
//         error.style.backgroundColor = '#dc3545';
//         let message = document.createElement('p');
//         message.textContent = 'First name, last name, and/or email must be at least 2 characters';
//         error.appendChild(message);
//         isValid = false;
//     }
//     if (password.length < 8) {
//         let error = document.querySelector('.alert1');
//         error.style.backgroundColor = '#dc3545';
//         let message = document.createElement('p');
//         message.textContent = 'Password must be at least 8 characters.';
//         error.appendChild(message);
//         isValid = false;
//     }
//     if (password != confirmPassword) {
//         let error = document.querySelector('.alert1');
//         error.style.backgroundColor = '#dc3545';
//         let message = document.createElement('p');
//         message.textContent = 'Passwords do not match.';
//         error.appendChild(message);
//         isValid = false;
//     }
//     if (emailRegex.test(email) != true) {
//         let error = document.querySelector('.alert1');
//         error.style.backgroundColor = '#dc3545';
//         let message = document.createElement('p');
//         message.textContent = 'Please enter a valid email.';
//         error.appendChild(message);
//         isValid = false;
//     }
//     return isValid;
// }

// function registerUser(e) {
//     let myForm = document.getElementById('myForm');
//     e.preventDefault();
//     let error = document.querySelector('.alert1');
//     error.textContent = " "
//     let form = new FormData(myForm);
//     fetch("http://127.0.0.1:5001/register", {method: 'POST', body:form})
//     .then(response => response.json())
//     .then(data => {
//         const isValid = validateForm();
//         if (isValid) {
//             myForm.submit();
//             window.location.href = "http://127.0.0.1:5001/recipes";
//         }
//     })
// }