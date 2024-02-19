let inventory=require("./data.js");

function BMWANDAUDiCars(arr){
    let BMW_AUDI=[];
    for(let car of arr){
        BMW_AUDI.push(car.car_make);
    }

    return JSON.stringify(BMW_AUDI);
};

console.log(BMWANDAUDiCars(inventory));