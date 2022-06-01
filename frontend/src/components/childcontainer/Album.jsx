
// React
import { Link } from "react-router-dom";
// Redux
import { connect } from "react-redux";
// Styles
import {showAlbum} from "../../redux/actions/main.actions.js"
import "../../public/assets/css/childcontainer/Album.scss"

function Album(props) {
    
    const showImages = ()=>{
        props.showAlbum(props.currentimg)
    }

    return (
        <>
            <div className="wrapper" onClick={showImages}>
                <Link to="/" className="card">
                    <div className="card__title">
                        {props.name}
                    </div>
                    <div className="card__wrapper">
                        {
                            props.currentimg.slice(0, 4).map((item) => {
                                return  <img key={item.id} src={item.link} alt={item.tag}/>
                            })
                        }
                    </div>
                </Link>
            </div>
        </>
        
    );
}

const mapDispatchToProps = {
    showAlbum,
}

export default connect(null, mapDispatchToProps)(Album);
