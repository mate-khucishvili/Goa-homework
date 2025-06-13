// 1

let number = prompt("შეიყვანე რიცხვი:");
number = Number(number);

if (number % 2 === 0) {
  alert("ლუწია");
} else {
  alert("კენტია");
}



// 2

let age_1 = prompt("შეიყვანე ასაკი:");
age_1 = Number(age_1);

if (age_1 < 18) {
  alert("თქვენ მიიღეთ 50%-იანი ფასდაკლება.");
} else {
  alert("თქვენ არ მიიღეთ ფასდაკლება.");
}


// 3
let age_2 = prompt("შეიყვანე ასაკი:");
age_2 = Number(age_2);

if (age_2 < 18) {
  alert("თქვენ მიიღეთ 50%-იანი ფასდაკლება.");
} else if (age_2 === 18) {
  alert("თქვენ მიიღეთ 25%-იანი ფასდაკლება.");
} else {
  alert("თქვენ არ მიიღეთ ფასდაკლება.");
}


// 4 
//ახსნა: როდის არის ცვლადი true ან false (ვრცლად)
// JavaScript-ში შემდეგი მნიშვნელობები ითვლება Falsy ანუ false-ად:
// false
// 0
// "" (ცარიელი სტრიქონი)
// null
// undefined
// NaN
// ხოლო დანარჩენი true იქნება

// 5 
let name = prompt("შეიყვანე შენი სახელი:");

if (name.length > 6) {
  alert(`hello my friend '${name}'!`);
} else {
  alert(`hello '${name}'!`);
}
