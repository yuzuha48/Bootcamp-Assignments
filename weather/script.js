var cookieElement = document.querySelector("#cookie");

function removeCookie() {
    cookieElement.remove();
}


var highElement1 = document.querySelector(".high1");
var highElement2 = document.querySelector(".high2");
var highElement3 = document.querySelector(".high3");
var highElement4 = document.querySelector(".high4");
var lowElement1 = document.querySelector(".low1");
var lowElement2 = document.querySelector(".low2");
var lowElement3 = document.querySelector(".low3");
var lowElement4 = document.querySelector(".low4");

var currentTemp = [24, 27, 21, 26, 18, 19, 16, 21];
var newTemp = [];

function convertTemp(element) {
    if(element.value == "°F") {
        for(var i=0; i<currentTemp.length; i++) {
            newTemp[i] = (currentTemp[i] * 9/5) + 32;
        }
        highElement1.innerText = parseInt(newTemp[0]) + "°";
        highElement2.innerText = parseInt(newTemp[1]) + "°";
        highElement3.innerText = parseInt(newTemp[2]) + "°";
        highElement4.innerText = parseInt(newTemp[3]) + "°";
        lowElement1.innerText = Math.ceil(newTemp[4]) + "°";
        lowElement2.innerText = parseInt(newTemp[5]) + "°";
        lowElement3.innerText = Math.ceil(newTemp[6]) + "°";
        lowElement4.innerText = Math.ceil(newTemp[7]) + "°";
    }
    else {
        highElement1.innerText = currentTemp[0] + "°";
        highElement2.innerText = currentTemp[1] + "°";
        highElement3.innerText = currentTemp[2] + "°";
        highElement4.innerText = currentTemp[3] + "°";
        lowElement1.innerText = currentTemp[4] + "°";
        lowElement2.innerText = currentTemp[5] + "°";
        lowElement3.innerText = currentTemp[6] + "°";
        lowElement4.innerText = currentTemp[7] + "°";
    }
}