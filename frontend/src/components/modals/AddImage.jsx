// React
import { useState } from 'react';
// Redux
import { connect } from 'react-redux';
import { addImage } from '../../redux/actions/main.actions';
// Components
import {
    Button,
    Form,
    FormGroup,
    Input,
    Modal, ModalHeader, ModalBody, ModalFooter,
    Label,
    } from 'reactstrap'
// Api
import myFetchData from "../../services/FetchData.js"

const AddImage = ({album,addImage}) =>{

    const [message,setMessage] = useState('')

    const [form, setValues] = useState({
        username: '',
    });
    
    const handleInput = event => {
        setValues({
          ...form,
          [event.target.name]: event.target.value
        })
    }

    const handleSubmit = event => {
        event.preventDefault();
        const getResponse = async () => {
            const response = await myFetchData.request("auth/","POST",form)
            return response
        }
       
        getResponse()
        .then(response => {
            if (response.authentication){
                loginRequest(response.data);
                setMessage('')
                modalSession(false)
            }
            else
                setMessage(response.message)
        })
        .catch((error) => console.log(error))
    }

    return (
        <>
            <Modal isOpen={mlogin}>
                <ModalHeader>
                    Login
                </ModalHeader>
                <ModalBody>
                    {
                        Object.keys(message).length>0?
                        <p className="alert mt-2 alert-danger">{message}</p>:
                        ""
                    }
                    <Form onSubmit={handleSubmit}>
                        <FormGroup>
                            <Label>Email</Label>
                            <Input 
                                name="username" 
                                className="form-control mt-2"
                                value={form.email} 
                                type="email"
                                placeholder="Entry email@email.com"
                                onChange={handleInput}></Input> 
                        </FormGroup>
                        <FormGroup>
                            <Label>Password</Label>
                            <Input 
                                name="password"
                                className="form-control mt-2"
                                type="password"
                                placeholder="Entry yout password"
                                onChange={handleInput}></Input> 
                        </FormGroup>
                        <Button> Continue </Button>
                    </Form>
                </ModalBody>
                <ModalFooter>
                    <Button onClick={()=> modalSession(false)}> Return </Button>
                </ModalFooter>
            </Modal>
        </>
    )
}

const mapStateToProps = state => {
    return {
      album: state.album
    };
};

const mapDispatchToProps = {
    addImage
}
  
export default connect(mapStateToProps, mapDispatchToProps)(AddImage);