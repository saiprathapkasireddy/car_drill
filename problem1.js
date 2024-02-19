let inventory=require("./data.js");

function carDetails(object,id){
    for(let car of object){
        if (car.id===id){
            return `car ${id} is a ${car.car_year} ${car.car_make} ${car.car_model}`
        }
    }
};

console.log(carDetails(inventory,33));