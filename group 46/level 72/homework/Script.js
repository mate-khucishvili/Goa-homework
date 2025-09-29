// = ნასწავლი მეთოდები და მაგალითები =

// Math.random() — აბრუნებს შემთხვევით რიცხვს 0-დან 1-მდე
console.log(Math.random());
console.log(Math.random());

// Math.floor() — ამრგვალებს ქვემოთ
console.log(Math.floor(4.9));
console.log(Math.floor(7.1));

// Math.ceil() — ამრგვალებს ზემოთ
console.log(Math.ceil(4.1));
console.log(Math.ceil(7.8));

// Math.round() — ამრგვალებს უახლოეს მთლიან რიცხვამდე
console.log(Math.round(4.4));
console.log(Math.round(4.5));

// Math.pow(x, y) — აყავს x რიცხვი y ხარისხში
console.log(Math.pow(2, 3));
console.log(Math.pow(5, 2));

// = 2) Scope JavaScript-ში =
/*
Scope ნიშნავს ცვლადის ხილვადობის არეს
Global Scope — ცვლადი ხელმისაწვდომია ყველგან
Function Scope — ცვლადი ხელმისაწვდომია მხოლოდ ფუნქციის შიგნით
Block Scope — ცვლადი ხელმისაწვდომია მხოლოდ ბლოკში { }
*/

let globus = "გლობალური ცვლადი";

function testScope() {
  let fuVar = "ფუნქციის შიგნით";
  console.log(fuVar);
}

{
  let blkVar = "ბლოკის შიგნით";
  console.log(blkVar);
}

console.log(globus);

// = 3) 100-ის ფარგლებში რენდომული რიცხვი =
let rand100 = Math.floor(Math.random() * 100);
console.log("რენდომული რიცხვი (0-99):", rand100);

// = 4)
let randomia = Math.ceil(Math.random() * 5); // 1-5
let cula = Math.pow(randomia, 2);
console.log("რიცხვი 1-5:", randomia);
console.log("მისი კვადრატი:", cula);

// = 5) Math.random() + ასაკი =
let persAge = Math.floor(Math.random() * 20); // 0-19
let person = {
  firstName: "ანა",
  lastName: "წიკლაური",
  age: persAge
};

console.log("პერსონის ობიექტი:", person);
