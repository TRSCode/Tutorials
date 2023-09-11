import { Button, Col, Container, Row } from 'react-bootstrap';
import 'bootstrap/dist/css/bootstrap.min.css';
import { Configuration } from 'openai'
// import { OpenAIAPI } from 'openai-api';
import { useState } from 'react';

const configuration = new Configuration ({
  apiKey: process.env.REACT_APP_OPENAI_KEY
})

// const openai = new OpenAIAPI({
//   key: process.env.REACT_APP_OPENAI_KEY
// });

function App() {
  const [questionType, setQuestionType] = useState('general')
  const [cbResponse, setCbResponse] = useState('')
  const [userInput, setUserInput] = useState('')
  const [isLoading, setIsLoading] = useState(false)

  return (
    <Container className='mt-3'>
      {/* hello world {process.env.REACT_APP_OPENAI_KEY.slice(0,5)} */}
      <Row>
        {['general', 'translate','weather'].map(el=>{
          return (
            <Col key={el}>
              <Button variant="primary" onClick={()=>{}}>{el}</Button>
            </Col>
          )
        })}
      </Row>
    </Container>
  );
}

export default App;
