async function gitUser(user) {
    if (user) {
        var response = await fetch(`https://api.github.com/users/${user}`);
        var coderData = await response.json();
        var result = `${coderData.name} has ${coderData.followers} followers <div><img src="${coderData.avatar_url}" alt="user's image"></div>`;
        document.getElementById("user_info").innerHTML = result
        return coderData;
    }
}

function getData() {
    fetch('http://localhost:5000/get_data')
    .then(response => response.json())
    .then(data => console.log(data))
}

getData();