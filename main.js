// function solve(a, b) {
// 	if(a == b) {
//     console.log('=')
//     }
//   	else if(a < b) {
//     console.log('<');
//     }
//     else{
// 	console.log('>')
//     }
// }
// solve(0,-5)

// function solve(a, b) {
//     let yi = a*1+b*1
//     yi.toString()
//     console.log(yi, typeof(yi))
// }
// solve('4','6')

// function solve(a, b) {
// 	if(a > 0 && b > 0){
//       let summ = a*1+b*1
//       let txt = summ.toString()
//       console.log(txt, typeof(txt));
//     }
// }
// solve('5','4')


// 6-masala Dasturchilar kunini topish

// let list = [4,45,'asdsadasda']
// list.map((e)=> e)

// function solve(year) {
// 	if(year % 4 == 0 && year % 400 == 0){
// 		console.log(`12/09/${year}`)    	
//     }else{
//   		console.log(`13/09/${year}`)
//     }
// }
// solve(2016)

// let serie = "A465187";
// let check = 0;
// for (let i = 0; i < serie.length; i++){
//     if((serie[0] == "A") && (typeOf(serie) == "number") && (serie.length == 6)) {
//         check+=1
//     }
// }
// console.log(check);

// for (let index = 0; index < array.length; index++) {
//     const element = array[index];
    
// }

// year = prompt()
// if (10000 > year > 0 ){
//     if (year % 400 == 0 || year % 4 == 0 && year % 100 != 0 ){
//         if (0 < year <= 9 ){
//             console.log(`12/09/000{year}`)
//         }else if (10 <= year <= 99 ){
//             console.log(`12/09/00{year}`)
//         }else if (100 <= year <= 999 ){
//             console.log(`12/09/0{year}`)
//         }else {
//             console.log(`12/09/{year}`)
//         }
//     }else{
//         if (0 < year <= 9 ){
//             console.log(`13/09/000{year}`) 
//         }else if( 10 <= year <= 99 ){
//             console.log(`13/09/00{year}`)
//         }else if ( 100 <= year <= 999 ){
//             console.log(`13/09/0{year}`)
//         }else {
//             console.log(`13/09/{year}`)
//         }
//     }
// }


// let n = 3
// let text = 'l;dsfaj a;sjf a ioewriopewrkdfjl dfdlfkjg'
// for (let i = 0; i<text.length; i++){
//     if(i.length != n){
//         i.split('').reverse().join('');
//     }
// }
// console.log(text);


// let ages = prompt()
let a = ages.split(" ")[0];
let b = ages.split(" ")[1];

if(a > b && (1 < a < 100) && (1 < b < 100) ){
    let year = 0
    while (a / b != 2.0 ){
        a+=1
        b+=1
        year+=1
    console.log(year)
    }
}else{
    console.log(-1)
}