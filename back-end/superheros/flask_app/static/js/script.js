function searchForHero(e) {
    e.preventDefault();
    var searchForm = document.getElementById('searchForm');
    var form = new FormData(searchForm);
    fetch('http://127.0.0.1:5001/search', {method:'POST', body:form})
    .then(res => res.json())
    .then(data => {
        let container = document.querySelector(".container");
        container.classList.remove("error");
        container.innerHTML = " ";
        if (data["results"]) {
            for (var i=0; i<data["results"].length; i++) {
                let container = document.querySelector(".container");
                let hero = document.createElement("div");
                hero.style.backgroundColor = "gray";
    
                let hero_img = document.createElement("img");
                hero_img.src = data["results"][i]["image"]["url"];
    
                let name = document.createElement("p");
                name.setAttribute("class", "name")
                name.textContent = data["results"][i]["name"];
    
                let human = document.createElement('p');
                human.setAttribute("class", "human")
                human.textContent = "A.K.A " + data["results"][i]["biography"]["full-name"];
                
                hero.appendChild(hero_img);
                hero.appendChild(name);
                hero.appendChild(human);
                container.appendChild(hero);
            }
        }
    else if (data["error"]) {
        let container = document.querySelector(".container")
        container.classList.add("error")
        let container_text = document.createElement('p');
        container_text.textContent = "Character with given name not found.";
        container_text.style.color = "yellow";
        container.appendChild(container_text);
    }
    })
}