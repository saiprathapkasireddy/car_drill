let inventory=require("./data.js");

function carYears(arr){
    let car_years=[]
    for(let car of arr){
        car_years.push(car.car_year);

    }
    return car_years
};

console.log(carYears(inventory));