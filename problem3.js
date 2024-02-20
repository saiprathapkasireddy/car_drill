//let inventory=require("./data.js")

function carModels(arr){
    if(Array.isArray(arr)){
    let car_models=[];
    for(let car of arr){
        car_models.push(car.car_model);
    }
    car_models.sort();
    return car_models
}
};

module.exports=carModels;

//console.log(carModels(inventory));