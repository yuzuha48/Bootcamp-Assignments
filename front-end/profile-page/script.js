var editElement = document.querySelector("#name");

function editProfile() {    
    editElement.innerText = "Jennifer Lawrence";
}

var num = 2;
var connectionRequests = document.querySelector("#num");

var userElement = document.querySelector("#todd");

function removeUser() {
    userElement.remove();
    num--; 
    connectionRequests.innerText = num;
}

var userElement2 = document.querySelector("#phil");

function removeUser2() {
    userElement2.remove();
    num--; 
    connectionRequests.innerText = num;
}

var num2 = 418;
var yourConnections = document.querySelector("#num2")

function addConnection() {
    num2++;
    yourConnections.innerText = num2;
}
