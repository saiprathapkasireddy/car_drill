//let inventory=require("./data.js");

function carYears(arr){
    if(Array.isArray(arr)){
    let car_years=[]
    for(let car of arr){
        car_years.push(car.car_year);

    }
    return car_years
}
};

module.exports=carYears;

//console.log(carYears(inventory));