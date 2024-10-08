let inventory=require("./data.js");

function lastCar(arr){
    if(Array.isArray(arr)){
        let res='';
        arr.forEach((element)=>{
            if(element.id===arr.length){
                res=`The last car is a ${element.car_make} ${element.car_model}`
            }
        });
        return res;
    
    }
}


module.exports=lastCar;

console.log(lastCar(inventory));