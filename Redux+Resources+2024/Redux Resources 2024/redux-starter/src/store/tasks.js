import { createAction } from "@reduxjs/toolkit";

// Action Types Section
// const ADD_TASK = "ADD_TASK";
// const REMOVE_TASK = "REMOVE_TASK";
// const TASK_COMPLETED = "TASK_COMPLETED";

// Actions Section
export const addTask = createAction("ADD_TASK");
export const removeTask = createAction("REMOVE_TASK");
export const completedTask = createAction("TASK_COMPLETED");
console.log(addTask.type)

// export const addTask = (task) => {
//     return {type: ADD_TASK, payload: {task: task}}
// }

// export const removeTask = (id) => {
//     return {type: REMOVE_TASK, payload: {id: id}}
// }

// export const completedTask = (id) => {
//     return {type: TASK_COMPLETED, payload: {id: id}}
// }

// export const fetchTodo = () => {
//     return async function (dispatch, getState) {
//         const response = await fetch("https://jsonplaceholder.typicode.com/todos/1")
//         console.log(response)
//     }
// }

export const fetchTodo = () => async (dispatch) => {
        const response = await fetch(
            "https://jsonplaceholder.typicode.com/todos/1"
        );
        const task = await response.json();
        dispatch(addTask(task.title));
}

// Reducer Section
let id = 0;

export default function reducer(state=[], action) {
    switch(action.type){
        case addTask.type:
            return [
                ...state,
                {
                    id: ++id,
                    task: action.payload.task,
                    completed: false,
                }
            ]
        case removeTask.type:
            return state.filter(task => task.id !== action.payload.id)

        case completedTask.type:
            return state.map(task => task.id === action.payload.id ? {
                ...task,
                completed: true
            }: task)

        default:
            return state
    }
}