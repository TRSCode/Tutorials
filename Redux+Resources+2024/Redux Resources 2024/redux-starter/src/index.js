function greeting() {
    // return "Good Morning!"
    return function() {
        return "Good Morning!"
    }
}

// let message = greeting
// message() // "Good Morning!"
// greeting() // "Good Morning!"

// console.log(message) // ƒ greeting() { return "Good Morning!" }

// function printMessage(anFunction) {
//     console.log(anFunction())
// }

// printMessage(greeting)

let anFunction = greeting()
let message = anFunction()