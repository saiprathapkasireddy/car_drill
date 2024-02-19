let inventory=require("./data.js");

function carsOlderThanYear(arr,year){
    let older_cars=[];
    for(let car of arr){
        if(car.car_year<year){
            older_cars.push(car.car_model)

        }
    }
    return older_cars.length;
};

console.log(carsOlderThanYear(inventory,2000));