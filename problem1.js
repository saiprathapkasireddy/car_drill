//let inventory=require("./data.js");

function findCarByID(arr,id){
    if(Array.isArray(arr)&&id){
    for(let car of arr){
        if (car.id===id){
            return `car ${id} is a ${car.car_year} ${car.car_make} ${car.car_model}`
        }
    }
}
};

module.exports=findCarByID;

//console.log(carDetails(inventory,33));