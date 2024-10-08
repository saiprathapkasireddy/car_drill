//let inventory=require("./data.js");

function carsOlderThanYear(arr,year){
    if(Array.isArray(arr)&&year){
    let older_cars=arr.filter((element)=>{
        if(element.car_year<year){
            return element;
        }
    })
    return older_cars.length;
}
};

module.exports=carsOlderThanYear;

//console.log(carsOlderThanYear(inventory,2000));