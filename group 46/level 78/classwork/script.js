let age = (prompt("Enter your age:"));
if (age <= 14) {
    console.log("you are kid");
} else if (age <= 18) {
    console.log("you are not adult yet");
} else {
    console.log("you are adult");
}

let name = prompt("Enter your name:");
if (name) {
    console.log(`Hello, ${name}!`);
} else {
    name = "guest";
    console.log(`Hello, ${name}!`);
}

let userName = prompt("Enter your name:");
let userAge = (prompt("Enter your age:"));
if (userAge <= 18) {
    console.log(`you are not adult yet '${userName}'!`);
} else {
    console.log(`Hello '${userName}'!`);
}
