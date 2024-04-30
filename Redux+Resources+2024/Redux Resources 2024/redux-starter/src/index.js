import store from './store'
import {addTask, removeTask} from './action'

const unsubscribe = store.subscribe(() => {
    console.log("Updated", store.getState())
})

store.dispatch(addTask("Task 1"))
store.dispatch(addTask("Task 2"))
console.log(store.getState())

unsubscribe()

store.dispatch(removeTask(1))
console.log(store.getState())