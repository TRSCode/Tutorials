import {produce} from "immer";

const book = {
    author: "Robert Kiyosaki",
    book: {
        name: "Rich Dad Poor Dad",
        price: "$8",
        rating: 4.7,
    },
};

const newBook = produce(book, (draftState) =>{
    draftState.book.price = "$10";
    draftState.book.rating =4.8;
})

console.log(newBook);

const arrayOfBooks = ["Book1", "Book2", "Book3"];
