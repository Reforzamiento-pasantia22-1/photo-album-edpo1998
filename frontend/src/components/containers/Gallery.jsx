
// React
import { useEffect } from "react";
// Redux
import { connect } from "react-redux";
// Components
import Album from "../childcontainer/Album";
//Utils
import {galleryRequest} from "../../redux/actions/main.actions.js"
// Api
import myFetchData from "../../services/FetchData.js"
//Styles
import "../../public/assets/css/components/Gallery.scss"

function Gallery({user,gallery,galleryRequest}) {

    const hasUser = Object.keys(user).length>0

    useEffect(() => {
        const getResponse = async (userid) => {
            const response = await myFetchData.request("gallery/gallery/get_All_Albums/?id="+userid,"GET")
            return response
        } 
        if(hasUser){
            getResponse(user.id)
            .then(response => galleryRequest(response.body.gallery))
            .catch((error) => console.log(error))
        }
    }, [])

    return (
        <div className="Gallery">
            {
                gallery.map( album=>{
                    return(
                        <Album 
                            key={album.id } 
                            id={album.id} 
                            name={album.album_name} 
                            currentimg={album.images}
                        />
                    )
                })
            }
        </div>
    );
}

const mapStateToProps = state => {
    return {
      user: state.user,
      gallery: state.gallery
    };
};

const mapDispatchToProps = {
    galleryRequest
}

export default connect(mapStateToProps, mapDispatchToProps)(Gallery);
