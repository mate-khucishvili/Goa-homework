// 1) მაქსიმუმი და მინიმუმი 
let nums = [3, 8, 1, 10, 5];
console.log(Math.max(...nums)); 
console.log(Math.min(...nums)); 

// 2) შემთხვევითი რიცხვი 0-10 და დამრგვალება
let ricxvebi = Math.random() * 10;
console.log(Math.round(ricxvebi));

// 3) უარყოფითი რიცხვი დადებითში
let negativ = -6;
console.log(Math.abs(negativ));

// 4) ათწილადი რიცხვი მაღლა და დაბლა დამრგვალება
let ricxvi = 4.3;
console.log(Math.ceil(ricxvi));  // მაღლა
console.log(Math.floor(ricxvi)); // დაბლა

// 5) რიცხვი 4 ხარისხში
let n = 2;
console.log(n ** 4);

// 6) მათემატიკური დამრგვალება
let num = 5.7;
console.log(Math.round(num));

// 7) 
// Scope — ნიშნავს ცვლადის მოქმედების ზონა:
// global (გარე) function (ფუნქციაში) block (if, for ში)
