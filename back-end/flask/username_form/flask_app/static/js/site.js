
function getUsers(){
    fetch('http://127.0.0.1:5000/users')
        .then(res =>  res.json())
        .then(data => {
            console.log(data)
            var users = document.getElementById('users');
            for( let i = 0; i < data.length; i++){
                let row = document.createElement('tr');

                let name = document.createElement('td');
                name.innerHTML = data[i].user_name;
                row.appendChild(name);
                
                let email = document.createElement('td');
                email.innerHTML = data[i].email;
                row.appendChild(email);
                users.appendChild(row);
            }
        })
}
getUsers();

function submitUser() {
    var myForm = document.getElementById('myForm');
    e.preventDefault();
    var form = new FormData(myForm);
    fetch("http://127.0.0.1:5000/create/user", {method: 'POST', body:form})
    .then(response => response.json())
    .then(data => console.log(data))
}

// function search(e) {
//     e.preventDefault();
//     var searchForm = document.getElementById('searchForm')
//     var form = new FormData(searchForm);
//     fetch('http://127.0.0.1:5000/search', {method: 'POST', body: form})
//     .then(res => res.json())
//     .then(data => console.log(data))
// }

