//let inventory=require("./data.js");

function BMWANDAUDiCars(arr){
    if(Array.isArray(arr)){
        let BMW_AUDI=arr.reduce((acc,cv)=>{
            if(cv.car_make==="Audi" || cv.car_make==="BMW"){
                acc.push(cv.car_model)
            }
            return acc;
        },[]);

    return JSON.stringify(BMW_AUDI);
}
};

module.exports=BMWANDAUDiCars;

//console.log(BMWANDAUDiCars(inventory));