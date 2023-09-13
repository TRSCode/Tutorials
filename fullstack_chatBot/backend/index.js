import {Configuration, OpenAIApi} from 'openai';
import express from 'express';
import cors from 'cors';
import bodyParser from 'body-parser';

const app = express();
const port = 8000;
app.use(bodyParser.json());
app.use(cors());

const configuration = new Configuration({
    organization: "org-4UIaVBbyo3oLFd22lmYGpSs4", 
    apiKey: "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"
})
const openai = new OpenAIApi(configuration);

app.listen(port, () => {
    console.log(`Server is running on port ${port}`);
});