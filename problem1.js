//let inventory=require("./data.js");

function findCarByID(arr,id){
    if(Array.isArray(arr)&&id){
    let res="";
    arr.forEach((element)=>{
        if(element.id===id){
            res=`car ${id} is a ${element.car_year} ${element.car_make} ${element.car_model}`
        }
    });
    return res;
}
};

module.exports=findCarByID;

//console.log(findCarByID(inventory,50));