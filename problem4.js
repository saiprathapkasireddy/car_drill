let inventory=require("./data.js");

function carYears(arr){
    if(Array.isArray(arr)){
    let car_years=arr.map((element)=>{
        return element.car_year;
    })
    return car_years
}
};

module.exports=carYears;

console.log(carYears(inventory));