// 1. Array creation - მასივის შექმნა
// 2. Array.concat() - ორი ან მეტი მასივის გაერთიანება ახალ მასივში
// 3. delete - ელემენტის წაშლა მასივიდან (მასივი არ ქრება, ელემენტი ხდება undefined)
// 4. Array.pop() - ბოლო ელემენტის ამოღება მასივიდან
// 5. Array.shift() - პირველი ელემენტის ამოღება მასივიდან
// 6. Array.unshift() - ელემენტის ჩასმა მასივის დასაწყისში
// 7. Array.push() - ელემენტის ჩასმა მასივის ბოლოში
// 8. Array.toString() - მასივის ელემენტების გადაქცევა სტრინგად
// 9. Array.splice() - ელემენტების წაშლა, ჩანაცვლება, დამატება კონკრეტულ ინდექსზე


let list1 = [1,2,3,4,5,6,7,8,9,10];
let list2 = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"];

let combinedList = list1.concat(list2);



// =======================================


// delete მეხუთე ინდექსზე ელემენტის შეცვლა
delete combinedList[5];

// ელემენტის ამოღება
combinedList.pop();

// ელემენტის ამოღება 
combinedList.shift();

// პირველ ინდექსზე ჩასვათ "ვანო"
combinedList[1] = "ვანო";

// სიაში ბოლოში ჩავსვათ "მოთიაშვილი"
combinedList.push("მოთიაშვილი");

let resultString = combinedList.toString();


console.log(resultString);

// სამი სიის შექმნა
let arr1 = [1, 2, 3];
let arr2 = ['a', 'b', 'c'];
let arr3 = [true, false, null];

// პირველის შეერთება 
let combined12 = arr1.concat(arr2);

let combined123 = combined12.concat(arr3);

combined123.splice(2, 4);

delete combined123[2];

console.log(combined123[combined123.length - 1]);
