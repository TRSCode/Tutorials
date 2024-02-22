'use server'
import OpenAI from 'openai';

const openai = new OpenAI({
    apiKey:process.env.OPENAI_API_KEY
});

export const generateChatResponse = async (chatMessages) => {
    // console.log(chatMessage);
    try {
        const response = await openai.chat.completions.create({
            messages:[
                {role:'system',content:'You are a helpful assistant.'},
                // {role:'user',content:chatMessage}
                ...chatMessages,
            ],
            model:"gpt-3.5-turbo",
            temperature:0,
        });
        // console.log(response.choices[0].message);
        // console.log(response);
        return response.choices[0].message;

    } catch (error) {
        return null;
    }
};