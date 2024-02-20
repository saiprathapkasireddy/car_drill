//let inventory=require("./data.js");

function lastCar(arr){
    if(Array.isArray(arr)){
    for(let car of arr){
        if(car.id===arr.length){
            return `last car is a ${car.car_make} ${car.car_model}`
        }
    }
}
}

module.exports=lastCar;

//console.log(lastCar(inventory));