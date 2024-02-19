let inventory=require("./data.js")

function carModels(arr){
    let car_models=[];
    for(let car of arr){
        car_models.push(car.car_model);
    }
    car_models.sort();
    return car_models
};

console.log(carModels(inventory));