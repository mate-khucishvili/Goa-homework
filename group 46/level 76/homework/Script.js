// 1

console.log("True");
console.log(!true);      
console.log(!1);          
console.log(!"text");     
console.log(![]);         
console.log(!{});         

console.log("False");
console.log(!false);
console.log(!0);         
console.log(!"");         
console.log(!null);       
console.log(!undefined);  


// 2

let qula = Math.floor(Math.random() * 101);
let hedegi = "";

if (qula >= 90) {
  hedegi = "Grade A";
} else if (qula >= 80) {
  hedegi = "Grade B";
} else if (qula >= 70) {
  hedegi = "Grade C";
} else if (qula >= 60) {
  hedegi = "Grade D";
} else {
  hedegi = "Grade F";
}

console.log(`Score: ${qula}, Result: ${hedegi}`);

// 3
let num = Math.floor(Math.random() * 11);
let result = num > 5 ? num : num * num;

console.log(`Number: ${num}, Result: ${result}`);

// 4 
let saxeli = "Giorgi";
let sabolo_hedegi = saxeli.length > 5 ? "this is my friend" : saxeli;

console.log(`Name: ${saxeli}, Output: ${sabolo_hedegi}`);
