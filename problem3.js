//let inventory=require("./data.js")

function carModels(arr){
    if(Array.isArray(arr)){
    let car_models=arr.map((element)=>{
        return element.car_model;
    });
    car_models.sort();
    return car_models;
}
};

module.exports=carModels;

//console.log(carModels(inventory));