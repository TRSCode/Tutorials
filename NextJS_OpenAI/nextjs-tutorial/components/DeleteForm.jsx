'use client';
import { deleteTask } from "@/utils/actions"
import { useFormStatus } from "react-dom";


const SubmitButton = () => {
    const {pending} = useFormStatus();
    return (
        <button className="btn btn-error btn-xs" dissabled={pending}>
            {pending? 'pending...': 'delete'}
        </button> 
    )
}

const DeleteForm = ({id}) => {
    return (
        // <div>DeleteForm</div>
        <form action ={deleteTask}>
            <input type="hidden" name="id" value={id} />
            <SubmitButton />
        </form>
    );
};

export default DeleteForm;