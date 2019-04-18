// function settingUpFood() {
//     var foods = document.querySelector("#omelets").innerHTML;
//     var template = Handlebars.compile(foods);
//     for (index in BREAKFAST.foods) {
//         let food = BREAKFAST.foods[index];
//         var html = template({
//             index: index,
//             food: food
//         });
//         document.querySelector("#omeletsTemplate").insertAdjacentHTML("beforeend", html);
//     }
// }

// settingUpFood()


function settingUpProjects() {
    var projects = document.querySelector('#omelets').innerHTML;
    console.log(projects)
    var template = Handlebars.compile(projects);
    console.log(BREAKFAST.foods)
    for (index in BREAKFAST.foods) {
        console.log(index)
        let project = BREAKFAST.foods[index];
        var html = template({
            index: index,
            project: project
        });
        document
            .querySelector('#omeletsTemplate')
            .insertAdjacentHTML('beforeend', html);
    }
}


settingUpProjects()