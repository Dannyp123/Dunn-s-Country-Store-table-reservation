function settingUpOmelets() {
    var foods = document.querySelector("#omelets").innerHTML;
    console.log(foods);
    var template = Handlebars.compile(foods);
    console.log(BREAKFAST.omelets);
    for (index in BREAKFAST.omelets) {
        console.log(index);
        let omelets = BREAKFAST.omelets[index];
        console.log(omelets.name)
        var html = template({
            index: index,
            omelets: omelets
        });
        document
            .querySelector("#omeletsTemplate")
            .insertAdjacentHTML("beforeend", html);
        console.log(document.querySelector("#omeletsTemplate"));
    }
}

function settingUpPlates() {
    var plate = document.querySelector("#plates").innerHTML;
    console.log(plate);
    var template = Handlebars.compile(plate);
    console.log(BREAKFAST.plates);
    for (index in BREAKFAST.plates) {
        console.log(index);
        let plates = BREAKFAST.plates[index];
        console.log(plates.name)
        var html = template({
            index: index,
            plates: plates
        });
        document
            .querySelector("#platesTemplates")
            .insertAdjacentHTML("beforeend", html);
    }
}

settingUpOmelets();
settingUpPlates()