

function BMWANDAUDiCars(arr){
    if(Array.isArray(arr)){
    let BMW_AUDI=[];
    for(let car of arr){
        BMW_AUDI.push(car.car_make);
    }

    return JSON.stringify(BMW_AUDI);
}
return [];
};

module.exports=BMWANDAUDiCars;