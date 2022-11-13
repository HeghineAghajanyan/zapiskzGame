let cards = [];
let heading =[];
let imgDiv = [];
let img = [];

let names = ["", "Ross", "Joe", "Phoebe"];
let images = ["", "st1.png", "st2.png", "st3.png"];

function setAttribute(class1, card) {
    return undefined;
}

for (let i = 1; i <= 3; i++)
{
    cards[i] = document.createElement('div');
    cards[i] = setAttribute('class', 'card');
    cards[i] = setAttribute('id', 'card-${i}');

    imgDiv[i] = document.createElement('div');
    imgDiv[i].setAttribute('id', 'img-${i}');


    heading[i] = document.createElement('h1');
    heading[i] = setAttribute('id', 'head-${i}');
    heading[i].innerHTML = names [i];
    
    imgDiv[i].appendChild(img[i]);
    cards[i].appendChild(imgDiv[i]);
    cards[i].appendChild(heading[i]);

    cardsContainer[i].appendChild(cards[i]);

}
