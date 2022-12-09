function pizzaOven (crustType, sauceType, cheeses, toppings) {
    var pizza = {};
    pizza.crustType = crustType; 
    pizza.sauceType = sauceType; 
    pizza.cheeses = cheeses; 
    pizza.toppings = toppings; 
    return pizza;
}

var pizza1 = pizzaOven("deep dish", "traditional", ["mozzarella"], ["pepperoni", "sausage"]);
console.log(pizza1);
var pizza2 = pizzaOven("hand tossed", "marinara", ["mozzarella", "feta"], ["mushrooms", "olives", "onions"]);
console.log(pizza2);
var pizza3 = pizzaOven("thin crust", "white sauce", ["mozzarella"], ["onion", "chicken"]);
console.log(pizza3);
var pizza4 = pizzaOven("hand tossed", "vodka sauce", ["mozzarella"], ["sausage", "onion"]);
console.log(pizza4);

function randomPizza (crustType, sauceType, cheeses, toppings) {
    var pizza = {}; 
    crustType = ["thin crust", "deep dish", "hand tossed"];
    sauceType = ["marinara", "alfredo", "vodka sauce"];
    cheeses = ["mozzarella", "parmesan", "ricotta", "gouda", "provolne"];
    toppings = ["onions", "sausage", "mushrooms", "garlic", "olives"]
    pizza.crustType = crustType[Math.floor(Math.random()*2)]; 
    pizza.sauceType = sauceType[Math.floor(Math.random()*2)]; 
    pizza.cheeses = [cheeses[Math.floor(Math.random()*4)], cheeses[Math.floor(Math.random()*4)]];
    pizza.toppings = [toppings[Math.floor(Math.random()*4)], toppings[Math.floor(Math.random()*4)], toppings[Math.floor(Math.random()*4)]];
    return pizza;
}

console.log(randomPizza())