console.log("hello".length);
console.log("".length);
console.log("Test test".length);

console.log("abc".toUpperCase());
console.log("Hello".toUpperCase());
console.log("123abc".toUpperCase());

console.log("HELLO".toLowerCase());
console.log("გიორგი".toLowerCase());
console.log("123ABC".toLowerCase());

// ობიექტის value-ების შეცვლა

let user3 = { city: "თბილისი" };
user3.city = "ბათუმი";
console.log(user3);

let user5 = { hobby: "ფეხბურთი" };
user5.hobby = "ცურვა";
console.log(user5);

// ობიექტიდან მონაცემის ამოღება

let book = { title: "ვეფხისტყაოსანი", author: "რუსთაველი" };
console.log(book.author);

let phone = { brand: "Samsung", model: "Galaxy" };
console.log(phone.model);

let car = { make: "Toyota", year: 2022 };
console.log(car.make);
