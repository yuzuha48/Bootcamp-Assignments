var cookieElement = document.querySelector("#cookie");

function removeCookie() {
    cookieElement.remove();
}

function convertTemp(element) {
    tempList = document.querySelectorAll(".temperature")
    tempList.forEach(tempList => {
        var highTempString = tempList.querySelector(".high").textContent
        var lowTempString = tempList.querySelector(".low").textContent
        if(element.value == "°F") {
            var high = Math.round((parseInt(highTempString) * 9/5) + 32)
            var low = Math.round((parseInt(lowTempString) * 9/5) + 32)
        }
        else {
            var high = Math.round((parseInt(highTempString) - 32) * 5/9) 
            var low = Math.round((parseInt(lowTempString) -32 ) * 5/9)
        }
        tempList.querySelector(".high").textContent = high.toString() + "°"
        tempList.querySelector(".low").textContent = low.toString() + "°"
    }) 
}  

function getWeather(lat, lon) {
    fetch(`https://api.openweathermap.org/data/2.5/weather?lat=${lat}&lon=${lon}&appid=8e219f0cd017d8624876764c47790259`)
        .then(res =>  res.json())
        .then(data => {
            console.log(data)
            var tempToday = document.querySelector('.today')
            var unit = document.querySelector(".selectTemp")
            if (unit.value == '°C') {
                var high = Math.round(data["main"].temp_max - 273.15)
                var low = Math.round(data["main"].temp_min - 273.15)
            }
            else if (unit.value == '°F') {
                var high = Math.round((data["main"].temp_max - 273.15) * 1.8 + 32)
                var low = Math.round((data["main"].temp_min - 273.15) * 1.8 + 32)
            }
            tempToday.querySelector(".high").textContent = high.toString() + "°"
            tempToday.querySelector(".low").textContent = low.toString() + "°"

            var image = document.querySelector(".image")
            var description = document.querySelector(".description")

            if (data["weather"][0].main == "Rain") {
                image.src = "assets/some_rain.png"
            }
            if (data["weather"][0].main == "Clouds") {
                image.src = "assets/some_clouds.png"
            }
            if (data["weather"][0].main == "Clear") {
                image.src = "assets/some_sun.png"
            }
            else {
                image.src = "assets/some_clouds.png"
            }
            description.textContent = data["weather"][0].main.toLowerCase()
        })
}

getWeather(37.3387, -121.8853)

function getCity(element) {
    document.querySelector(".city").textContent = element.innerText
}



