var displayDiv = document.querySelector("#display");
var arr = [];

function press(number) {
    displayDiv.innerText = number;
    arr.push(number);
}

function setOP(element) {
    operator = element;
    arr.push(operator);
}

function clr() {
    arr = [];
    displayDiv.innerText = 0;
}

function calculate() {
    var newValue = "";
    for(var i=0; i<arr.length; i++) {
        newValue += arr[i];
    }
    result = eval(newValue);
    console.log(result);
    displayDiv.innerText = result;
    arr = [result];
}
