// 1. შევქმნათ ორი სია
let numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10];             // ციფრები
let strings = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"]; // სტრინგები

// 2. გავაერთიანოთ ეს ორი სია
let ertadsaboloo = numbers.concat(strings); 

// 3. მეხუთე ინდექსზე შევცვალოთ ელემენტი undefined-ით delete-ის გამოყენებით
delete ertadsaboloo[5]; 

// 4. ამოვაგდოთ ბოლო ელემენტი
ertadsaboloo.pop();

// 5. ამოვაგდოთ პირველი ელემენტი
ertadsaboloo.shift();

// 6. პირველ ინდექსზე ჩავამატოთ "ვანო"
ertadsaboloo.splice(1, 0, "ვანო");

// 7. ბოლოში ჩავამატოთ მოთიაშვილი
ertadsaboloo.push("მოთიაშვილი");


let result = ertadsaboloo.join(", "); 

// ვსო დასრულდა პაკა
console.log(result);
