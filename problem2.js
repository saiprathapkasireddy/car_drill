let inventory=require("./data.js");

function lastCar(arr){
    for(let car of arr){
        if(car.id===arr.length){
            return `last car is a ${car.car_make} ${car.car_model}`
        }
    }
}

console.log(lastCar(inventory));