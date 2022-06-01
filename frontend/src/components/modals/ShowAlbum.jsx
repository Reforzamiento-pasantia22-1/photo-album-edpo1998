
// Components
import { connect } from 'react-redux'
import {
    Button,
    FormGroup,Input,Label,
    Modal, ModalHeader, ModalBody,
    } from 'reactstrap'
import { showAlbum } from '../../redux/actions/main.actions'

import "../../public/assets/css/modals/ShowAlbum.scss"

const ShowAlbum = ({album,showAlbum}) =>{

    const closeModal =()=> showAlbum([])
    
    return (
        <>
            <Modal isOpen={album.length>0?true:false} size="lg" className='ModalStyle'>
                <ModalHeader>
                <FormGroup className='NavSearch'>
                    <Label>Busqueda</Label>
                    <Input
                    name="search" 
                    
                    />
                    <Button onClick={closeModal}> Search </Button>
                    <Button onClick={closeModal}> Return </Button>
                </FormGroup>
                   
                </ModalHeader>
                <ModalBody>
                   <div className='container'>
                    {
                        album.map(imagen =>{
                            return(
                                <img 
                                key={imagen.id}
                                className="item" 
                                src={imagen.link}
                                alt={imagen.tag}
                                />
                            )
                        })
                    }
                   </div>
                </ModalBody>
            </Modal>
        </>
    )


}

const mapDispatchToProps = {
    showAlbum,
}


const mapStateToProps = state => {
    return {
      album: state.album
    };
};


export default connect(mapStateToProps, mapDispatchToProps)(ShowAlbum);